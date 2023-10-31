module pwm (
    input clk,                    
    input [3:0] binary_input,    
    output speed    
);

reg [7:0] counter = 0;       
wire [7:0] duty_cycle;       

assign duty_cycle = binary_input * 10; 


always @(posedge clk) 
    counter <= (counter < 100) ? counter + 1 : 0;

assign speed = (counter < duty_cycle) ? 1 : 0;

endmodule



