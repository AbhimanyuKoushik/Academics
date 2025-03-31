#define F_CPU 16000000UL

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <stdbool.h>

/*------------------ Millis Timer ------------------*/
volatile unsigned long millis_count = 0;
ISR(TIMER0_COMPA_vect) {
    millis_count++;
}

unsigned long currentMillis(void) {
    unsigned long m;
    cli();
    m = millis_count;
    sei();
    return m;
}

/*------------------ Button Definitions ------------------*/
#define NUM_BUTTONS 7
volatile uint8_t *buttonPinRegs[NUM_BUTTONS] = { &PINC, &PINC, &PINC, &PINC, &PINC, &PINC, &PINB };
uint8_t buttonBits[NUM_BUTTONS] = { 0, 1, 2, 3, 4, 5, 5 };  // A0-A5, D13

unsigned long lastButtonPress[NUM_BUTTONS] = {0};
volatile uint8_t buttonState = 0xFF;
const unsigned long debounceDelay = 200;

/*------------------ Decoder and Display Definitions ------------------*/
volatile uint8_t *decoderPort = &PORTB;               // Decoder: 8,9,10,11 (PORTB)
const uint8_t decoderBits[4] = {0, 1, 2, 3};          // PB0, PB1, PB2, PB3

volatile uint8_t *displayPortRegs[6] = { &PORTD, &PORTD, &PORTD, &PORTD, &PORTD, &PORTD };
const uint8_t displayBits[6] = {7, 6, 5, 4, 3, 2};   // Cathodes: 2-7

/*------------------ Time Variables ------------------*/
volatile uint8_t hours = 23;
volatile uint8_t minutes = 59;
volatile uint8_t seconds = 50;

/*------------------ Mode Flags ------------------*/
volatile unsigned long previousMillisTime = 0;
const unsigned long interval = 1000;
volatile bool timerMode = false;
volatile bool clockHalted = false;

/*------------------ Function Prototypes ------------------*/
void checkButtons(void);
void incrementHour(void);
void decrementHour(void);
void incrementMinute(void);
void decrementMinute(void);
void incrementSecond(void);
void toggleTimerMode(void);
void resetClock(void);
void incrementTime(void);
void decrementTime(void);
void displayTime(void);
void showDigit(uint8_t digit, uint8_t displayIndex);

/*------------------ Main Function ------------------*/
int main(void) {
    /* Timer Initialization */
    TCCR0A = (1 << WGM01);
    TCCR0B = (1 << CS01) | (1 << CS00);
    OCR0A = 249;
    TIMSK0 = (1 << OCIE0A);
    sei();

    /* Set Display Pins as Output */
    DDRD |= 0b11111100;   // PD2 - PD7 for cathodes

    /* Set Decoder Pins as Output */
    DDRB |= 0b00001111;    // PB0 - PB3 for decoder

    /* Set Button Pins as Input with Pull-up */
    DDRC &= 0b11000000;    // A0 - A5 as input (PC0 - PC5)
    PORTC |= 0b00111111;   // Enable pull-up resistors
    DDRB &= ~(1 << PB5);   // D13 as input
    PORTB |= (1 << PB5);   // Enable pull-up

    while (1) {
        unsigned long now = currentMillis();
        checkButtons();

        if (!clockHalted && (now - previousMillisTime >= interval)) {
            previousMillisTime = now;
            if (timerMode) {
                decrementTime();
            } else {
                incrementTime();
            }
        }

        displayTime();
    }
    return 0;
}

/*------------------ Button Handling ------------------*/
void checkButtons(void) {
    uint8_t currentState = 0;
    for (uint8_t i = 0; i < NUM_BUTTONS; i++) {
        currentState |= ((*buttonPinRegs[i] & (1 << buttonBits[i])) ? 0 : 1) << i;
    }

    uint8_t changes = buttonState ^ currentState;
    uint8_t presses = changes & currentState;
    
    for (uint8_t i = 0; i < NUM_BUTTONS; i++) {
        if ((presses & (1 << i)) && (currentMillis() - lastButtonPress[i] > debounceDelay)) {
            lastButtonPress[i] = currentMillis();
            void (*actions[])() = {incrementHour, decrementHour, incrementMinute,
                                   decrementMinute, toggleTimerMode, incrementSecond, resetClock};
            actions[i]();
        }
    }
    buttonState = currentState;
}

/*------------------ Time Updates ------------------*/
void incrementTime(void) {
    seconds++;
    if (seconds > 59) {
        seconds = 0;
        minutes++;
        if (minutes > 59) {
            minutes = 0;
            hours++;
            if (hours > 23) {
                hours = 0;
            }
        }
    }
}

void decrementTime(void) {
    if (seconds == 0) {
        seconds = 59;
        if (minutes == 0) {
            minutes = 59;
            if (hours == 0) {
                hours = 23;
            } else {
                hours--;
            }
        } else {
            minutes--;
        }
    } else {
        seconds--;
    }
}

/*------------------ Adjustment Functions ------------------*/
void incrementHour(void) {
    hours = (hours == 23) ? 0 : hours + 1;
}

void decrementHour(void) {
    hours = (hours == 0) ? 23 : hours - 1;
}

void incrementMinute(void) {
    minutes = (minutes == 59) ? 0 : minutes + 1;
}

void decrementMinute(void) {
    minutes = (minutes == 0) ? 59 : minutes - 1;
}

void incrementSecond(void) {
    seconds = (seconds == 59) ? 0 : seconds + 1;
}

void toggleTimerMode(void) {
    timerMode = !timerMode;
    clockHalted = false;
    previousMillisTime = currentMillis();
}

void resetClock(void) {
    hours = 0;
    minutes = 0;
    seconds = 0;
    clockHalted = true;
}

/*------------------ Display Functions ------------------*/
void displayTime(void) {
    uint8_t digits[6];

    // Hours
    digits[0] = hours / 10;
    digits[1] = hours % 10;

    // Minutes
    digits[2] = minutes / 10;
    digits[3] = minutes % 10;

    // Seconds
    digits[4] = seconds / 10;
    digits[5] = seconds % 10;

    for (uint8_t i = 0; i < 6; i++) {
        showDigit(digits[i], i);
        _delay_ms(1);
    }
}

void showDigit(uint8_t digit, uint8_t displayIndex) {
    // Set decoder pins according to digit's binary value
    for (uint8_t i = 0; i < 4; i++) {
        if (digit & (1 << i)) {
            *decoderPort |= (1 << decoderBits[i]);
        } else {
            *decoderPort &= ~(1 << decoderBits[i]);
        }
    }

    // Turn off all display cathodes
    for (uint8_t i = 0; i < 6; i++) {
        *displayPortRegs[i] &= ~(1 << displayBits[i]);
    }

    // Enable the selected cathode
    *displayPortRegs[displayIndex] |= (1 << displayBits[displayIndex]);
}
