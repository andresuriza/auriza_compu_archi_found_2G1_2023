module flipflop_tb();

	logic clock, D1;
	wire Q1, notQ1;
	
	flipflop ff(D1, clock, Q1, notQ1);
	
	initial begin
	
	D1=0;
	clock=0;
	
	#40
	
	D1=0;
	clock=1;
	
	#40
	
	D1=1;
	clock=0;
	
	#40
	
	D1=1;
	clock=1;
	
	end

endmodule