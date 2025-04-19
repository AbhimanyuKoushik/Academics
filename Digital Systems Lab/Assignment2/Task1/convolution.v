`timescale 1ns/1ps

module top_module (
    input  [3:0] in1 [7:0],
    input  [3:0] in2 [7:0],
    output reg [3:0] out [14:0]
);

    integer a, b;
    reg [7:0] temp;

    always @(*) begin
        for (a = 0; a < 15; a = a + 1)
            out[a] = 4'd0;

        for (a = 0; a < 8; a = a + 1) begin
            for (b = 0; b < 8; b = b + 1) begin
                temp = in1[a] * in2[b];
                out[a + b] = out[a + b] + temp[3:0];
            end
        end
    end


endmodule