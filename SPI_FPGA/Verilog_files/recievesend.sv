module recievesend(input MOSI , clk, rst, ready, done, cs,
						 output MISO, start,
						 output reg [3:0]lds);
						 
			logic mosi;
			
			assign mosi = ~cs&MOSI;
			
			handshake hk(clk, rst, ready, done, start);
			SPregister regist(mosi, clk, lds);
			flipflop ff(mosi, clk, MISO);
	
	
endmodule