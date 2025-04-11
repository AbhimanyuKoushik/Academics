module top_module(input wire [3:0] in, output wire [1:0] out, output valid);
    assign valid = (|in[3:0]);
    assign out[0] = (in[3] | ((~in[2]) & in[1]));
    assign out[1] = in[3] | in[2];
endmodule