`timescale 1ns/1ps

module testbench;
    // Unpacked-array inputs and outputs
    reg  [3:0] in1 [7:0];
    reg  [3:0] in2 [7:0];
    wire [3:0] out [14:0];

    // Instantiate the DUT
    top_module dut (
        .in1(in1),
        .in2(in2),
        .out(out)
    );

    integer i;

    initial begin
        // Generate VCD waveform file
        $dumpfile("wave.vcd");
        $dumpvars(0, testbench);
        
        for (i = 0; i < 15; i = i + 1) begin
            $dumpvars(0, out[i]);
        end

        $display("\n=== Test Case 1: Simple values ===");
        // load in1 = {1,2,3,4,5,6,7,8}
        // load in2 = {8,7,6,5,4,3,2,1}
        in1[0]=4'd1; in1[1]=4'd2; in1[2]=4'd3; in1[3]=4'd4;
        in1[4]=4'd5; in1[5]=4'd6; in1[6]=4'd7; in1[7]=4'd8;
        in2[0]=4'd8; in2[1]=4'd7; in2[2]=4'd6; in2[3]=4'd5;
        in2[4]=4'd4; in2[5]=4'd3; in2[6]=4'd2; in2[7]=4'd1;
        #10;  // let combinational logic settle
        for (i = 0; i < 15; i = i + 1) begin
            $display("out[%0d] = %0d", i, out[i]);
        end

        $display("\n=== Test Case 2: All ones ===");
        //load in1 = {1,1,1,1,1,1,1,1}
        //load in2 = {1,1,1,1,1,1,1,1}
        for (i = 0; i < 8; i = i + 1) begin
            in1[i] = 4'd1;
            in2[i] = 4'd1;
        end
        #10;
        for (i = 0; i < 15; i = i + 1) begin
            $display("out[%0d] = %0d", i, out[i]);
        end

        $display("\n=== Test Case 3: Alternating values ===");
        //load in1 = {0,1,0,1,0,1,0,1}
        //load in2 = {1,0,1,0,1,0,1,0}
        for (i = 0; i < 8; i = i + 1) begin
            in1[i] = (i % 2) ? 4'd1 : 4'd0;
            in2[i] = (i % 2) ? 4'd0 : 4'd1;
        end
        #10;
        for (i = 0; i < 15; i = i + 1) begin
            $display("out[%0d] = %0d", i, out[i]);
        end

        // Finish simulation
        $finish;
    end
endmodule
