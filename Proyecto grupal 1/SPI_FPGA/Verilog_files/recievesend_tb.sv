module recievesend_tb();

	logic mosi,clk,cs,rst,rdy,dn;
	reg [3:0] lds;
	reg speed, start;
	wire miso;
	
	recievesend misomosi(mosi,clk,cs,rst,rdy,dn,miso,lds,start,speed);
	
	always begin
        #1 clk = ~clk;
    end
	
	initial begin
	
	clk = 0;
	
	for (int i = 0; i <= 3; i = i + 1) begin
            mosi = 1;
            #150; // Espera un tiempo antes de cambiar el número binario
        end

        #50 $finish;
	end

endmodule