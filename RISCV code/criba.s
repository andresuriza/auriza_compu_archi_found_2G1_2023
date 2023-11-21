.data
    n: .word 10
    primo: .string " es primo\n"
    
.text
main:
    li x1, 2 # i = 2
    li x2, 1 # resta
    li x3, 0 # valor inicial 
    li x8, 2 # Numero 2
    lw x7, n # limite
    addi x7, x7(1)
    sub x4, x3, x2 # n-1
 
Criba:
     beq x3, x7, Exit # Si v inicial == v final, termine
     j EsPrimo
          
EsPrimo:
    beq x3, x0, NoEsPrimo # Ignorar 0
    beq x3, x2, NoEsPrimo # Ignorar 1
    beq x3, x8, SiEsPrimo # 2 siempre es primo
    
    beq x1, x4, SiEsPrimo # Si i es igual a n-1, parar
    rem x5, x3, x1 # n % i
    beq x5, x0, NoEsPrimo # Si n % i es 0, parar
    addi x1, x1, 1 # i++
    j EsPrimo

NoEsPrimo:
    li x1, 2 # i = 2
    addi x3, x3, 1 # valor inicial +1
    sub x4, x3, x2 # n-1
    j Criba

SiEsPrimo:
    mv a0, x3
    li a7, 1
    ecall
    la a0, primo
    li a7, 4
    ecall
    j NoEsPrimo # Continuar con algoritmo
 
Exit:
    li a7, 10
    ecall