module recievesend(input MOSI , clk, cs, rst, rdy, dn, 
						 output MISO, 
						 output reg [3:0]lds,
						 output reg start);
						 
			logic mosi;
			
			assign mosi = ~cs&MOSI;
			
			handshake hs(clk, rst, rdy, dn, start);
			SPregister regist(mosi, clk, lds);
			flipflop ff(mosi, clk, MISO);
	
	
endmodule