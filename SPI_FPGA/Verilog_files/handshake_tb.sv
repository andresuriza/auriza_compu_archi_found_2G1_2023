module handshake_tb();
	
	logic clk, rst, rdy, dn;
	reg st;
	
	handshake hsk(clk, rst, rdy, dn, st);
	
	initial begin 
		clk = 0;
		rst = 0;
		rdy = 0;
		dn = 0;
		#40
		clk = 1;
		dn = 0;
		#40
	   clk = 0;
		rst = 1;
		rdy = 0;
		dn = 0;
		#40
		clk = 1;
		dn = 0;
		#40
		clk = 0;
		rst = 0;
		rdy = 0;
		dn = 0;
		#40
		clk = 1;
		dn = 0;
		#40
		clk = 0;
		rdy = 1;
		dn = 0;
		#40
		clk = 1;
		dn = 0;
		#40
		clk = 0;
		rdy = 0;
		dn = 1;
		#40
		clk = 1;
		dn = 1;
		#40
		clk = 0;
		dn = 0;
		#40
		clk = 1;
		dn = 0;
	end
	

endmodule