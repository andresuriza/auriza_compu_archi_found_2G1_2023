module recievesend_tb();

	logic mosi,clk,cs;
	reg [3:0] lds;
	wire miso;
	
	recievesend misomosi(mosi,clk,cs,miso,lds);
	
	initial begin
	
	mosi = 1;
	clk = 0;
	cs = 0;
	#40
	mosi = 1;
	clk = 1;
	#40
	mosi = 0;
	clk = 0;
	#40
	mosi = 0;
	clk = 1;
	#40
	mosi = 1;
	clk = 0;
	#40
	mosi = 1;
	clk = 1;
	#40
	mosi = 1;
	clk = 0;
	#40
	mosi = 1;
	clk = 1;
	end

endmodule