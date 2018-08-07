# coding=utf-8

########################################################################################################################
####                                  Trabalho Inteligencia Artificial - Agentes de Busca                           ####
####                                  Aluno: Daniel Rosendo de Souza                                                ####
####                                  Professor: Ajalmar                                                            ####
####                                  Arquivo agentesDeBusca - Arquivo que contém as funções de Busca               ####
########################################################################################################################

# coding=utf-8
from classes import No
from Queue import PriorityQueue

# SOLUÇÃO
def solucao(no):
    lista = []
    while no:
        lista.append(no.estado)
        no = no.pai
    lista.reverse()
    return lista

# BREADTH-FIRST SEARCH - BUSCA EM LARGURA
def BFS(problema):
    no = No(problema.inicio)

    if problema.teste_de_obj(no.estado):
        return [no.estado]

    borda = [no]
    explorado = set()

    while borda:
        no = borda.pop(0) #FILA
        explorado.add(no.estado)

        for acao in problema.acoes(no.estado):
            filho = No(acao, no)

            if filho not in borda and filho.estado not in explorado:
                if problema.teste_de_obj(filho.estado):
                    return solucao(filho)
                borda.append(filho)

    return None

#DEPTH-FIRST SEARCH - BUSCA EM PROFUNDIDADE
def DFS(problema):
    no = No(problema.inicio)

    if problema.teste_de_obj(no.estado):
        return [no.estado]

    borda = [no]

    while borda:
        no = borda.pop(0) #PILHA

        for acao in problema.acoes(no.estado):
            filho = No(acao, no)

            if filho not in borda:
                if problema.teste_de_obj(filho.estado):
                    return solucao(filho)
                borda.append(filho)
    return None

# DEPTH-FIRST SEARCH W/ LIST OF VISITED - BUSCA EM PROFUNDIDADE COM LISTA DE VISITADOS
def DFSV(problema):
    no = No(problema.inicio)

    if problema.teste_de_obj(no.estado):
        return [no.estado]

    borda = []
    explorado = set()
    borda.append(no)

    while borda:
        no = borda.pop(-1) #PLLHA
        explorado.add(no.estado)

        for acao in problema.acoes(no.estado):
            filho = No(acao, no)

            if filho.estado not in explorado and filho not in borda:
                if problema.teste_de_obj(filho.estado):
                    return solucao(filho)
                if filho.estado not in explorado:
                    borda.append(filho)
    return None

#DEPTH-LIMITED SEARCH - BUSCA EM PROFUNDIDADE LIMITADA
def DLS(problema, limite):
    no = No(problema.inicio)
    return recursivoDLS(no, problema, limite)

def recursivoDLS(no, problema, limite):
    if problema.teste_de_obj(no.estado):
        return solucao(no)

    elif limite == 0:
        return "cutoff"

    else:
        cutoff_occurred = False

        for acao in problema.acoes(no.estado):
            filho = No(acao, no)

            resultado = recursivoDLS(filho, problema, limite-1)

            if resultado == "cutoff":
                cutoff_occurred = True

            elif resultado:
                return resultado
        if cutoff_occurred:
            return "cutoff"

        else:
            return False

#ITERATIVE DEEPENING SEARCH - BUSCA ITERATIVA
def IDS(problema):
    profundidade = 0
    while True:
        resultado = DLS(problema, profundidade)
        if resultado != "cutoff":
            return resultado
        profundidade = profundidade + 1

#UNIFORM-COST-SEARCH - BUSCA DE CUSTO UNIFORME
def UCS(problema):
    no = No(problema.inicio)
    borda = PriorityQueue()
    borda.put((no.custo_caminho, no))
    explorado = set()

    while borda:
        aux = borda.get()
        no = aux[1]

        if problema.teste_de_obj(no.estado):
            return solucao(no)

        explorado.add(no.estado)

        for acao in problema.acoes(no.estado):
            custo_caminho = int(problema.acao[acao][no.estado]) + no.custo_caminho
            filho = No(acao, no, custo_caminho=custo_caminho)

            it = [i for i in borda.queue]

            if (filho.custo_caminho, filho) not in it and filho.estado not in explorado:
                borda.put((filho.custo_caminho, filho))
    return None