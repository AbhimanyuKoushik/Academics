`timescale 1ns/1ps

module test_counter;

    reg clk, reset, enable;
    wire [3:0] count;
    
    // Instantiate the DUT (Device Under Test)
    top_module dut (
        .clk(clk),
        .reset(reset),
        .enable(enable),
        .count(count)
    );
    
    // Clock generation: toggles every 5ns
    always #5 clk = ~clk;
    
    initial begin
        // Dump waveform data to counter.vcd
        $dumpfile("test_logic_working.vcd");
        $dumpvars(0, test_counter);
        
        // Initialize signals
        clk = 0;
        reset = 1;
        enable = 0;
        #10;
        
        // Release reset and enable the counter
        reset = 0;
        enable = 1;
        
        // Run for 20 clock cycles
        repeat (20) begin
            #10;
            $display("Time: %0t ns | Count: %b", $time, count);
        end
        
        // Disable the counter and finish simulation
        enable = 0;
        #10;
        $finish;
    end

endmodule
