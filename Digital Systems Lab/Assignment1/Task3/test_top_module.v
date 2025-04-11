`timescale 1ns/1ps

module top_module_tb;
  // Declare input as reg (since it will be driven in the testbench) and output as wire.
  reg  [7:0] in;
  wire       out;
  
  // Instantiate the DUT (your top_module)
  top_module uut(
    .in(in),
    .out(out)
  );

  // Optional: Dump waveform data for later viewing in a waveform viewer.
  initial begin
    $dumpfile("top_module_tb.vcd");
    $dumpvars(0, top_module_tb);
  end
  
  // Apply test vectors
  initial begin
    // Monitor time, input, and output.
    $monitor("At time %0t: in = %b, out = %b", $time, in, out);
    
    // Test Case 1: All zeros.
    in = 8'b00000000;  // Even number of ones (0 ones), so parity is even.
    #10;
    
    // Test Case 2: Single 1.
    in = 8'b00000001;  // Odd number of ones (1 one), expected parity bit 1.
    #10;
    
    // Test Case 3: Two 1's.
    in = 8'b00000011;  // Even number of ones (2 ones), expected parity bit 0.
    #10;
    
    // Test Case 4: Pattern alternating.
    in = 8'b10101010;  // Four 1's, expected parity bit 0.
    #10;
    
    // Test Case 5: Block of ones.
    in = 8'b11110000;  // Four 1's, expected parity bit 0.
    #10;
    
    // Test Case 6: Another alternating pattern.
    in = 8'b01010101;  // Four 1's, expected parity bit 0.
    #10;
    
    // End simulation.
    $finish;
  end

endmodule
