// test_top_module.v
`timescale 1ns/1ps
module test_top_module;

  reg [3:0] in;
  wire [1:0] out;
  wire valid;

  // Instantiate the design under test (DUT)
  top_module dut (
    .in(in),
    .out(out),
    .valid(valid)
  );

  integer i;  // Declare loop variable

  initial begin
    $display(" in  | valid | out ");
    $display("-----|-------|------");
    
    for (i = 0; i < 16; i = i + 1) begin
      in = i[3:0];  // assign lower 4 bits
      #1; // wait for logic to settle
      $display("%b |   %b   | %b", in, valid, out);
    end

    $finish;
  end

endmodule
