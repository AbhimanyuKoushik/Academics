module top_module (
    input  wire [7:0] in1,
    input  wire [7:0] in2,
    input  wire       carryin,
    output wire [7:0] out,
    output wire       carryout
);
    
    wire [8:0] tempcarryout;
    assign tempcarryout[0] = carryin;

    genvar i;
    generate
        for (i = 0; i < 8; i = i + 1) begin : adderloop
            adder1 addonebit(in1[i], in2[i], tempcarryout[i], out[i], tempcarryout[i+1]);
        end
    endgenerate

endmodule

module adder1 (
    input  wire in1,
    input  wire in2,
    input  wire carryin,
    output wire out,
    output wire carryout
);
    assign out = carryin ^ (in1 ^ in2);
    assign carryout = ((~(carryin) & (in2 & in1))) | ((carryin & (in1 | in2)));
endmodule
