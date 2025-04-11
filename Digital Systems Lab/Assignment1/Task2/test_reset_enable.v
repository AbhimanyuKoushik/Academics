`timescale 1ns/1ps
module test_reset_enable;

    reg clk, reset, enable;
    wire [3:0] count;
    
    // Instantiate the DUT (Device Under Test)
    top_module dut (
        .clk(clk),
        .reset(reset),
        .enable(enable),
        .count(count)
    );
    
    // Clock generation: 10 ns period (toggle every 5 ns)
    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end
    
    initial begin
        // Dump waveform data for debugging
        $dumpfile("test_reset_enable.vcd");
        $dumpvars(0, test_reset_enable);
        
        // --- Phase 1: Assert reset, enable off ---
        reset = 1; 
        enable = 0;
        #20;  // Wait 20 ns; counter should be 0
        
        // --- Phase 2: Release reset, keep enable off ---
        reset = 0;
        #50;  // Wait 50 ns; since enable is low, count should not change
        
        // --- Phase 3: Enable counter ---
        enable = 1;
        #100; // Wait 100 ns; observe count changes (counter toggles/increments)
        
        // --- Phase 4: Assert reset while counter is enabled ---
        reset = 1;
        #20;  // With reset asserted, counter should go to 0 immediately
        reset = 0;
        #50;  // Wait 50 ns to observe post-reset behavior
        
        $finish;
    end

endmodule
