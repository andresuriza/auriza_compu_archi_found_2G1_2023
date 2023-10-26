module handshake_tb();
   reg clk;         
   reg rst_l;       
   reg ready;       
   reg done;        
   wire start;      


   handshake hsk(
      .clk(clk),
      .rst_l(rst_l),
      .ready(ready),
      .done(done),
      .start(start)
   );

   initial begin

      clk = 0;
      rst_l = 1;
      ready = 0;
      done = 0;
		
		
      #10 rst_l = 0;
      ready = 1;
      done = 0;
      #10
      if (start == 1)
         $display("Handshake iniciado correctamente.");
      else
         $display("Handshake no iniciado.");

		#10 rst_l = 1;
		#10 rst_l = 0;
		ready = 0;
      done = 1;
		#10
		if (start == 1)
         $display("Handshake iniciado correctamente.");
      else
         $display("Handshake no iniciado.");
			
		#10 rst_l = 1;
		#10 rst_l = 0;
		ready = 1;
      done = 1;
		if (start == 1)
         $display("Handshake iniciado correctamente.");
      else
         $display("Handshake no iniciado.");
			
		#10 rst_l = 1;
		#10 rst_l = 0;
		ready = 0;
      done = 0;
		if (start == 1)
         $display("Handshake iniciado correctamente.");
      else
         $display("Handshake no iniciado.");
		
      $finish;
   end

   always #5 clk = ~clk;  // Generación del reloj
endmodule
