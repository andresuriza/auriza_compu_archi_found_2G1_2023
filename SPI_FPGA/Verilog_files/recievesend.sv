module recievesend(input MOSI , clk, cs, rst, rdy, dn, 
						 output MISO, 
						 output reg [3:0]lds,
						 output reg start,
						 output reg speed);
						 
			logic mosi;
			
			assign mosi = ~cs&MOSI;
			
			pwm p(clk,lds,speed);
			handshake hs(clk, rst, rdy, dn, start);
			SPregister regist(mosi, clk, lds);
			flipflop ff(mosi, clk, MISO);
	
	
endmodule