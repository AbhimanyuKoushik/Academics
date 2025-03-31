import random  # Import the random module to generate random numbers.
random.seed(42)  # Set the seed for the random number generator to ensure reproducible results.

def amountwon(p):
    # This function simulates a series of coin tosses until a 'winning' condition is met.
    # The parameter 'p' represents the probability threshold for a winning toss.
    tosscount = 1  # Initialize the toss counter to 1, representing the first coin toss.
    while True:  # Begin an infinite loop that will continue until a win condition is satisfied.
        randomnumber = random.random()  # Generate a random floating-point number between 0.0 and 1.0.
        if randomnumber <= p:
            # Check if the random number is less than or equal to the probability 'p'.
            # If the condition is true, it represents a winning toss.
            # The payout is computed as 2 raised to the power of the current toss count.
            return 2 ** tosscount  # Return the payout based on the number of tosses taken.
        else:
            tosscount += 1  # If the win condition is not met, increment the toss count and repeat the loop.

def Expectation(m):
    # This function calculates the expected value (average payout) over 'm' simulated games.
    expect = 0  # Initialize the cumulative sum of all payouts to zero.
    for i in range(m):
        # Run a loop for 'm' iterations, where each iteration represents one game simulation.
        expect += amountwon(0.5)
        # For each game, call the 'amountwon' function with a win probability of 0.5
        # and add the resulting payout to the cumulative sum.
    return (expect / m)  # Compute the average payout by dividing the total sum by the number of games 'm'.

# Define a list of different simulation sizes to see how the expected value converges with more trials.
m_values = [100, 10000, 1000000]

for m in m_values:
    # Iterate through each simulation size in the list.
    expectation = Expectation(m)
    # Calculate the expected payout for the current number of simulations.
    print(f"Expected value for m = {m}: {expectation}")
    # Print out the expected value, clearly indicating the number of simulations used.
