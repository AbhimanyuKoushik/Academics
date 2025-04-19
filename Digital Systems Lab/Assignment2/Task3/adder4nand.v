`timescale 1ns/1ps

module nandgate (input in1, input in2, output out);
    assign #1 out = ~(in1 & in2);
endmodule

module top_module ( input  wire [3:0] in1, input  wire [3:0] in2, input  wire carryin,
    output wire [3:0] out, output wire carryout);
    
    wire [4:0] tempcarryout;
    assign tempcarryout[0] = carryin;

    genvar i;
    generate
        for (i = 0; i < 4; i = i + 1) begin : adderloop
            adder1 addonebit(in1[i], in2[i], tempcarryout[i], out[i], tempcarryout[i+1]);
        end
    endgenerate

    assign carryout = tempcarryout[4];

endmodule

module adder1 ( input in1, input in2, input carryin,
        output out, output carryout);  
    wire a,b,c,d,e,f,g,h;

    nandgate nand1(in1, in2, a);
    nandgate nand2(in1, a, b);
    nandgate nand3(in2, a, c);
    nandgate nand4(b, c, d);
    nandgate nand5(carryin, d, e);
    nandgate nand6(d, e, f);
    nandgate nand7(carryin, e, g);
    nandgate nand8(f, g, out);
    nandgate nand9(a, e, carryout);    
endmodule
