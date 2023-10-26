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
   wire reset_trigger;

   // Lógica para determinar si estamos en el estado 0
   assign state0 = (state == 2'b00);

   // Lógica para determinar si estamos en el estado 1
   assign state1 = (state == 2'b01);

   // Lógica para determinar si estamos en el estado 2
   assign state2 = (state == 2'b10);

   // Lógica combinacional para determinar si el reinicio debe ocurrir
   assign reset_trigger = (!rst_l) | (state2 & !done & !ready);

   always @(posedge clk) begin
      // Lógica para el estado siguiente
      state <= (state1 & done) | (state2 & !(ready & state1 & done));

      // Lógica para la señal de inicio
      start <= state0 & ready;

      // Lógica para el reinicio basado en la lógica combinacional
		// Utilizando un mux para asignar valores a 'state' y 'start'
		{state, start} <= reset_trigger ? {2'b00, 1'b0} : {state, start};

   end
endmodule