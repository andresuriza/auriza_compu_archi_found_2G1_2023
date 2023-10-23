module recievesend(input MOSI , clk, cs,
						 output MISO, 
						 output reg [3:0]lds);
						 
			logic mosi;
			
			assign mosi = ~cs&MOSI;
						 
			SPregister regist(mosi, clk, lds);
			flipflop ff(mosi, clk, MISO);
	
	
endmodule