module pwm (
    input clk,
    input [3:0] binary_input,
    output reg motor_speed
);
    reg [3:0] counter;

	always @(posedge clk) begin
			counter <= (counter == 4'b1111) ? 4'b0 : counter + 1;
	end

    // Lógica combinacional para determinar el duty cycle del motor
    always @* begin
        // Utilizando mux para asignar valores a 'motor_speed'
        motor_speed = (counter <= binary_input) ? 1'b1 : 1'b0;
    end
	 
   // Initialize counter
    initial begin
        counter = 4'b0000;
    end

endmodule


