# coding=utf-8

########################################################################################################################
####                                  Trabalho Inteligencia Artificial - Agentes de Busca                           ####
####                                  Aluno: Daniel Rosendo de Souza                                                ####
####                                  Professor: Ajalmar                                                            ####
####                                  Arquivo Classes - Arquivo que contém as classes do projeto                    ####
########################################################################################################################

class Problema(object):

    def __init__(self, inicio, objetivo=None, acao=None):
        self.inicio = inicio
        self.objetivo = objetivo
        self.acao = acao

    def teste_de_obj(self, noEstado):
        return noEstado == self.objetivo

    def acoes(self, noEstado):
        return list(self.acao[noEstado])

class No(object):

    def __init__(self, estado, pai=None, custo_caminho=0, valor=None):
        self.estado = estado
        self.pai = pai

        if pai:
            self.action = pai.estado + " -> " + estado

        self.custo_caminho = custo_caminho
        self.valor = valor
        self.profundidade = 0

        if pai:
            self.profundidade = pai.profundidade + 1

    def __repr__(self):
        return self.estado + ", " + self.action


class ataques(object):
    def __init__(self, ataques=[], estado=[]):
        self.ataques = ataques
        self.estados = estado

        if estado:
            self.ataques, self.qtdAtaques = self.contadorDeAtaques(estado)

    def adicionarAtk(self,i, j):
        self.ataques.append((i,j))

    def printAttacks(self):
        d = {}

        for i in self.ataques:
            if i[0] in d:
                d[i[0]].append(i)
            else:
                d[i[0]] = [i]

        for i in d:
            s = "{}: (".format(i)
            for x in d[i]:
                if not x == d[i][-1]:
                    s = s + x[0] + "<->" + x[1] + ") ("
                else:
                    s = s + x[0] + "<->" + x[1] + ")"
            print (s)

    def contadorDeAtaques(self, estado):
        atks = []
        count = 0
        tam = len(estado)
        a = [x+estado[x] for x in range(tam)]
        b = [x-estado[x] for x in range(tam)]

        for i in range(tam-1):
            for j in range(i+1, tam):
                if estado[i] == estado[j]:
                    k, l = str(estado[i]) + str(i), str(estado[j]) + str(j)
                    atks.append((k,l))
                    count = count + 1
                if a[i] == a[j]:
                    k, l = str(a[i]-i) + str(i), str(a[j]-j) + str(j)
                    atks.append((k,l))
                    count = count + 1
                if b[i] == b[j]:
                    k, l = str(i - b[i]) + str(i), str(j - b[j]) + str(j)
                    atks.append((k, l))
                    count = count + 1
        return atks, count

