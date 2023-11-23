
x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31 = range(32)
n = 10

def lw(reg, mem):
    return mem[reg]


def addi(reg, value):
    reg += value
    return reg


def sub(reg1, reg2):
    reg1 - reg2
    return reg1


def rem(reg1, reg2):
    reg1 % reg2
    return reg1


def main():
    global x1, x2, x3, x4, x5, x6, x7, x8, n
    x1 = 2
    x2 = 1
    x3 = 0
    x8 = 2
    x7 = lw(x7, [n-1])
    x7 = addi(x7, 1)
    x4 = sub(x3, x2)

def criba():
    if x3 == x7:
        return
    else:
        esPrimo()

def esPrimo():
    global x1, x2, x3, x4, x5, x6, x7, x8, n
    if x3 == x0 or x3 == x2:
        NoEsPrimo()
    if x3 == x8 or x1 == x4:
        SiEsPrimo()

    x5 = rem(x3, x1)

    if x5 == x0:
        NoEsPrimo()
    x1 = addi(x1,1)
    esPrimo()

def NoEsPrimo():
    global x1, x3, x4, x2
    x1 = 2
    x3 = addi(x3,1)
    x4 = sub(x3, x2)
    criba()


def SiEsPrimo():
    print(x3 + " es primo")
    NoEsPrimo()

main()
criba()