module pwm_tb;

    reg clk;
    reg [3:0] binary_input;
    reg motor_speed;

    // Instanciar el módulo pwm_controller
    pwm pwm_inst (
        .clk(clk),
        .binary_input(binary_input),
        .motor_speed(motor_speed)
    );

    // Generar un reloj
    always begin
        #1 clk = ~clk;
    end

    // Establece un patrón de entrada
    initial begin
        clk = 0;

        // Cambia el número binario de entrada en un bucle para simular diferentes casos
        for (int i = 0; i <= 9; i = i + 1) begin
            binary_input = i;
            #150; // Espera un tiempo antes de cambiar el número binario
        end

        #50 $finish;
    end

endmodule
