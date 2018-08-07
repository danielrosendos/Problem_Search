# coding=utf-8
########################################################################################################################
####                                  Trabalho Inteligencia Artificial - Agentes de Busca                           ####
####                                  Aluno: Daniel Rosendo de Souza                                                ####
####                                  Professor: Ajalmar                                                            ####
####                                  Arquivo agente_Teste - Arquivo que de teste do projeto                        ####
########################################################################################################################

from agentesDeBusca import BFS, DFS, DFSV, IDS, DLS, UCS
from classes import Problema
from worlds import map_romania
from worlds import vaccum_world as vaccum
from rainha import imprimirTabuleiro
from solver import solver

INIT_MAP = "Arad"
GOAL_MAP = "Bucharest"
NUMBER_OF_ITERATIONS = 10
INIT_VACCUM = "ESS"
GOAL_VACCUM = "DSL"

print("-----------------TABELA MAPA DA ROMENIA----------------------")
print("_____________________________________________________________")
print("| BFS |", BFS(Problema(INIT_MAP, GOAL_MAP, map_romania)), "|")
print("_____________________________________________________________")
print("| DLS |", DLS(Problema(INIT_MAP, GOAL_MAP, map_romania), NUMBER_OF_ITERATIONS), "|")
print("_____________________________________________________________")
print("| IDS |", IDS(Problema(INIT_MAP, GOAL_MAP, map_romania)), "|")
print("_____________________________________________________________")
print("| DFS |", DFS(Problema(INIT_MAP, GOAL_MAP, map_romania)), "|")
print("_____________________________________________________________")
print("| UCS |", UCS(Problema(INIT_MAP, GOAL_MAP, map_romania)), "|")



print("-----------------TABELA APIRADOR DE PÓ----------------------")
print("_____________________________________________________________")
print("| BFS |", BFS(Problema(INIT_VACCUM, GOAL_VACCUM, vaccum)), "|")
print("_____________________________________________________________")
print("| DLS |", DLS(Problema(INIT_VACCUM, GOAL_VACCUM, vaccum), NUMBER_OF_ITERATIONS), "|")
print("_____________________________________________________________")
print("| IDS |", IDS(Problema(INIT_VACCUM, GOAL_VACCUM, vaccum)), "|")
print("_____________________________________________________________")
print("| DFS |", DFSV(Problema(INIT_VACCUM, GOAL_VACCUM, vaccum)), "|")
print("_____________________________________________________________")
print("| UCS | Mundo aspirador de pó da erro, pois não possui custo de caminho \n")
print("| UCS |", UCS(Problema(INIT_VACCUM, GOAL_VACCUM, vaccum)), "|")

