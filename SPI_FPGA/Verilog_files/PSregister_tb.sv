module PSregister_tb();
	reg[3:0] message;
	logic clock, ld;
	wire dat;
	
	PSregister out(message,clock,ld,dat);
	
	initial begin
	
	message = 4'b1110;
	clock = 0;
	ld = 1;
	#40
	clock = 1;
	ld = 0;
	#40
	clock = 0;
	ld = 1;
	#40
	clock = 1;
	#40
	clock = 0;
	#40
	clock = 1;
	#40
	clock = 0;
	#40
	clock = 1;
	#40
	clock = 0;
	#40
	clock = 1;
	#40
	clock = 0;
	#40
	clock = 1;
	#40
	clock = 0;
	
	end
	

endmodule