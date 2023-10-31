module recievesend(input MOSI , clk, cs, rst, rdy, dn, 
						 output MISO, 
						 output reg [3:0]lds,
						 output reg start,
						 output reg speed);
						 
			logic mosi;
			
			assign mosi = ~cs&MOSI;
			
			timeunit 1ns;
			timeprecision 100ps;
			bit clk2 = 0; 
			 
			always
			  begin 
				 #1000000ns clk2=~clk2;
			  end

			pwm p(clk2,lds,speed);
			handshake hs(clk, rst, rdy, dn, start);
			SPregister regist(mosi, clk, lds);
			flipflop ff(mosi, clk, MISO);
	
	
endmodule