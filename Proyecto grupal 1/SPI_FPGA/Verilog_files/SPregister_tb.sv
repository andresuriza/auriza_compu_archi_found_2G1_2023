module SPregister_tb();
	logic mosi,clock;
	reg[3:0] lds, msj;
	
	SPregister regist(mosi,clock,lds,msj);
	
	initial begin
	
		mosi=1;
		clock=0;
		#40
		mosi=1;
		clock=1;
		#40
		mosi=0;
		clock=0;
		#40
		mosi=0;
		clock=1;
		#40
		mosi=1;
		clock=0;
		#40
		mosi=1;
		clock=1;
		#40
		mosi=1;
		clock=0;
		#40
		mosi=1;
		clock=1;
	
	end


endmodule