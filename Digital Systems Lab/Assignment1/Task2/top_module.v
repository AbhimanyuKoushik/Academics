module top_module(input clk, input reset, input enable, output [3:0] count);

    wire t0, t1, t2, t3;

    assign t0 = enable;
    assign t1 = enable & count[0];
    assign t2 = enable & count[0] & count[1];
    assign t3 = enable & count[0] & count[1] & count[2];   
    
    Tflipflop ff0(clk, t0, reset, count[0]);
    Tflipflop ff1(clk, t1, reset, count[1]);
    Tflipflop ff2(clk, t2, reset, count[2]);
    Tflipflop ff3(clk, t3, reset, count[3]);

endmodule

module Tflipflop(input clk, input T, input reset, output reg Q);

    always @(posedge clk, posedge reset) begin
        if (reset == 1) begin
            Q <= 1'b0;
        end
        else begin
            if (T == 1) begin
                Q <= ~Q;
            end
        end
    end

endmodule
