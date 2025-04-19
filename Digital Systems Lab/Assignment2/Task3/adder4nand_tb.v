`timescale 1ns/1ps

module adder4nand_tb;
    // Inputs to DUT
    reg  [3:0] in1;
    reg  [3:0] in2;
    reg        carryin;
    // Outputs from DUT
    wire [3:0] out;
    wire       carryout;

    // For measuring total simulation time
    real start_time;

    // Instantiate the NAND‑only adder
    top_module dut (
        .in1(in1),
        .in2(in2),
        .carryin(carryin),
        .out(out),
        .carryout(carryout)
    );

    integer i, j, k;

    initial begin
        // Record start time
        start_time = $realtime;

        // Enable waveform dumping
        $dumpfile("wave.vcd");
        $dumpvars(0, adder4nand_tb);

        // Test case 1: zero inputs, zero carry
        for (i = 0; i < 16; i = i + 1) begin
            for (k = 0; k < 2; k = k + 1) begin
                for (j = 0; j < 16; j = j + 1) begin
                    in1     = i;
                    in2     = j;
                    carryin = k;
                    #21; // wait for max delay
                    $display("Time=%0t ns | %0d + %0d + %0d = %0d, cout=%b",
                            $time, in1, in2, carryin, out, carryout);
                end
            end
        end

        //Time=310000 ns | 0 + 14 + 1 = 7, cout=1
        //Time=320000 ns | 0 + 15 + 1 = 8, cout=0
        //Time=550000 ns | 1 + 6 + 1 = 4, cout=0
        //Time=630000 ns | 1 + 14 + 1 = 12, cout=0
        //Time=850000 ns | 2 + 4 + 1 = 15, cout=0
        //Time=860000 ns | 2 + 5 + 1 = 0, cout=0
        //Time=940000 ns | 2 + 13 + 1 = 8, cout=0
        //Time=1170000 ns | 3 + 4 + 1 = 4, cout=0
        //Time=1250000 ns | 3 + 12 + 1 = 12, cout=0
        //Time=1470000 ns | 4 + 2 + 1 = 15, cout=0
        //Time=1480000 ns | 4 + 3 + 1 = 0, cout=0
        //Time=1550000 ns | 4 + 10 + 1 = 7, cout=1
        //Time=1560000 ns | 4 + 11 + 1 = 8, cout=0
        
        // Test case 2: mid-range values with carry‑in
        in1     = 4'd2; 
        in2     = 4'd3; 
        carryin = 1'b1; 
        #15;
        $display("Time=%0t ns | Test2: %0d + %0d + %0d = %0d, cout=%b",
                 $time, in1, in2, carryin, out, carryout);

        // Test case 3: overflow scenario
        in1     = 4'd5; 
        in2     = 4'd10; 
        carryin = 1'b0; 
        #10;
        $display("Time=%0t ns | Test3: %0d + %0d + %0d = %0d, cout=%b",
                 $time, in1, in2, carryin, out, carryout);

        // Print total simulation time
        $display("\nTotal simulation time: %0t ns", $realtime - start_time);

        $finish;
    end
endmodule
