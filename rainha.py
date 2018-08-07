from classes import ataques

alphabet = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
            10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
            20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}

def imprimirTabuleiro(estado, index=0):
    objAtks = ataques(estado=estado)

    if objAtks.qtdAtaques:
        print ("Ataques")
        objAtks.printAttacks()

    if index == 0:
        imprimirTabuleiro0(estado)

    elif index == 1:
        imprimirTabuleiro1(estado)

    else:
        imprimirTabuleiro2(estado)

def imprimirTabuleiro0(estado):
    tamEstado = len(estado)

    s = ""

    for i in (x for x in range(tamEstado)):
        s = s + " __{}__".format(alphabet[i])
    print s

    for i in range(tamEstado):
        s = ""
        print "|     " * tamEstado + "|"

        for x in estado:
            if x == i:
                s = s + "|  {}  ".format("x")
            else:
                s = s + "|  {}  ".format(" ")
        print s + "|" + str(i)
        print "|_____" * tamEstado + "|"

def imprimirTabuleiro1(estado):
    tamEstado = len(estado)
    s = ""

    for i in (x for x in range(tamEstado)):
        s = s + " _{}_".format(i)
    print s

    for i in range(tamEstado):
        s = ""
        for x in estado:
            if x == i:
                s = s + "|_{}_".format("x")
            else:
                s = s + "|_{}_".format("_")
        print s + "|" + str(i)

def imprimirTabuleiro2(estado):
    def troca(a, b):
        aux = a
        a = b
        b = aux
        return a, b

    a, b = "*", " "
    tamEstado = len(estado)

    s = ""

    for i in (x for x in range(tamEstado)):
        s = s + " __{}__".format(i)
    print s

    for i in range(tamEstado):
        s = ""
        print "|" + ("{}".format(a) * 5 + "|" + "{}".format(b) * 5 + "|") * (tamEstado / 2)
        for x in estado:
            a, b = troca(a,b)
            if x == i:
                s = s + "|" + "{}".format(b) * 2 + "{}".format("x") + "{}".format(b) * 2
            else:
                s = s + "|" + "{}".format(b) * 2 + "{}".format(b) + "{}".format(b) * 2
        print s + "|" + str(i)
        print "|" + ("{}".format(a) * 5 + "|" + "{}".format(b) * 5 + "|") * (tamEstado / 2)
        a, b = troca(a, b)