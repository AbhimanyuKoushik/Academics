`timescale 1ns/1ps

module adder8;
    reg  [7:0] in1;
    reg  [7:0] in2;
    reg carryin;
    wire [7:0] out;
    wire carryout;

    top_module dut (
        .in1(in1),
        .in2(in2),
        .carryin(carryin),
        .out(out),
        .carryout(carryout)
    );

    integer i;

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, adder8);

        in1 = 8'd127;
        in2 = 8'd127;
        carryin = 1'b1;

        #10;

        $display("Addition Results for Test case 1:");
        $display("%d(in1)+%d(in2)+%d(carryin)=%d(out)",in1,in2,carryin,out);

        in1 = 8'd0;
        in2 = 8'd0;
        carryin = 1'b1;

        $display("\n");
        #10;

        $display("Addition Results for Test case 2:");
        $display("%d(in1)+%d(in2)+%d(carryin)=%d(out)",in1,in2,carryin,out);

        in1 = 8'd54;
        in2 = 8'd24;
        carryin = 1'b0;

        $display("\n");
        #10;

        $display("Addition Results for Test case 3:");
        $display("%d(in1)+%d(in2)+%d(carryin)=%d(out)",in1,in2,carryin,out);

        $finish;
    end
endmodule
