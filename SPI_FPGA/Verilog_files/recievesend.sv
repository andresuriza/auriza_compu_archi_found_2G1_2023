module recievesend(input MOSI , clk,
						 output MISO, 
						 output reg [3:0]lds);
						 
		
		 
		 SPregister regist(MOSI, clk, lds);
		 flipflop ff(MOSI, clk, MISO);
	
	
endmodule