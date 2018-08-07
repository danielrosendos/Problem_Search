from classes import No
from Queue import PriorityQueue
from random import randint, random, choice
from math import exp

subValues = lambda l, i, v: l[:i] + [v] + l[i+1:]
f = lambda S: funcCusto(S)

def funcCusto(estado):
    count = 0
    tam = len(estado)
    a = [x + estado[x] for x in range(tam)]
    b = [x - estado[x] for x in range(tam)]

    for i in range(tam-1):
        for j in range(i + 1, tam):
            if estado[i] == estado[j]:
                count = count + 1
            if a[i] == a[j]:
                count = count + 1
            if b[i] == b[j]:
                count = count + 1
    return count

def vizinhos(ocorrencias):
    aux = [x for x in ocorrencias.estado]
    tam = len(aux)
    ns = PriorityQueue()

    for i in range(tam):
        l = [x for x in range(tam) if not aux[i] == x]

        for j in l:
            k = subValues(aux, i ,j)
            objK = funcCusto(k)
            ns.put((objK, k))

    return ns.get()

def sucessorRandom(ocorrencias):
    aux = [x for x in ocorrencias.estado]
    tam = len(aux)
    sucessor = []

    for i in range(tam):
        l = [x for x in range(tam) if not aux[i] == x]

        for j in l:
            k = subValues(aux, i, j)
            sucessor.append(k)

    estado = choice(sucessor)
    custo = funcCusto(estado)
    no = No(estado=estado, valor=custo)
    return no

def TempInicial():
    return randint(50,100)

def Pertuba(S):
    S = No(S)
    return sucessorRandom(S).estado

def Randomiza():
    return random()

def solver(S0, M=1000, P=100, L=10, alpha=0.99):
    S = S0
    T = TempInicial()
    j = 1
    print T
    sucesso = 1
    while (sucesso != 0) and (j <= M):
        i = 1
        sucesso = 0
        print ("Iteracao: " + str(j) + "| Temperatura: " + str(T))
        while (sucesso < L) and (i <= P):
            Si = Pertuba(S)
            deltaFi = f(Si) - f(S)
            if deltaFi <= 0 or exp(-deltaFi / T) > Randomiza():
                S = Si
                print ("Estado: {}".format(str(S)) + " | " + "Iteracao: {}".format(j) + " | " + "Ataques: {}".format(
                    funcCusto(S)))
                sucesso = sucesso + 1
            i = i + 1
        print ("Numero de sucessos: " + str(sucesso))
        T = alpha * T
        j = j + 1

    return S
