module top_module(input wire [7:0] in, output out);
    assign out = ^in;
endmodule