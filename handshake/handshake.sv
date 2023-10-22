module handshake
(
   input      clk,
   input      rst_l,    
   input      ready,
   input      done,
   output reg start
);

   reg [1:0] state;
   wire state0, state1, state2;

   // Lógica para determinar si estamos en el estado 0
   assign state0 = (state == 0);

   // Lógica para determinar si estamos en el estado 1
   assign state1 = (state == 1);

   // Lógica para determinar si estamos en el estado 2
   assign state2 = (state == 2);

   always @(posedge clk or negedge rst_l) begin
      if (!rst_l) begin
         state <= 2'b00;
         start <= 1'b0;
      end
      else begin
         // Lógica combinacional para la máquina de estados
         state <= (state2 & !(done & state1 & state2)) |
                   (state1 & (done & !state2)) |
                   (state0 & (ready & !state1));
         
         // Lógica para la señal de inicio
         start <= (state0 & (ready & !state1));
      end
   end
endmodule
