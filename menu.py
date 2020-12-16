#IMPORTS
from readfiles import *
from algorithms import *

def mainMenu():
    list_city = []
    map_distance_faro = []
    menuCarregarCidades(list_city)
    menuCarregarDistanciaFaro(map_distance_faro)
    menuAlgoritmos(list_city, map_distance_faro)

def menuCarregarCidades(list_city):#carrega as cidades de um ficheiro txt
    print(" \n \t PROGRAMA INICIADO \t ")
    print("\n Qual o nome do ficheiro com as cidades? \n (default : listacidades)")
    filename_cidades = input()
    filename_cidades = filename_cidades+".txt"
    loadCityMap(filename_cidades,list_city)
    print("\n Carregado o ficheiro {} para um map de cidades \n".format(filename_cidades))
    printCityMap(list_city)

def menuCarregarDistanciaFaro(map_distance_faro):#carrega a distancia das cidades a faro de um ficheiro txt
    print("\n Qual o nome do ficheiro com as distancias das cidades a faro \t (default: distancetoFaro)")
    filename_distance_faro = input()
    filename_distance_faro = filename_distance_faro+".txt"
    loadMapDistanceFaro(filename_distance_faro,map_distance_faro)
    print("\n Carregado o ficheiro {} para um map de distancias das cidades a faro \n".format(filename_distance_faro))
    printMapDistanceFaro(map_distance_faro)

def menuAlgoritmos(list_city,map_distance_faro):
    while (True):
        printMenuAlgoritmos()
        opt = int(input())
        if(opt == 1):
            printMenuCustoUniforme(list_city)
        if(opt == 2):
            printMenuProfundidadeLimitada(list_city)
        if(opt == 3):
            printMenuProcuraSofrega(list_city,map_distance_faro)
        if(opt == 4):
            printMenuAStar(list_city,map_distance_faro)
        if(opt == -1):
            print("\n\n \nA ENCERRAR O PROGRAMA")
            break

def printMenuAlgoritmos():
    print("\n\n\nQual o Algoritmo de procura a executar")
    print("\t \t \t MENU ALGORITMOS:\t ")
    print("\t Algoritmos de procura cega")
    print("\t \t 1 - Custo Uniforme ")
    print("\t \t 2 - Profundidade Limitada ")
    print("\t Algoritmos de procura heuristica")
    print("\t \t 3 - Procura Sofrega")
    print("\t \t 4 - A* ")
    print(" \t escolher -1 para sair ")

def printMenuCustoUniforme(list_city):
    print("\n\n\n\n Sera Executado Algoritmo Custo Uniforme")
    print("Qual a cidade inicio ?")
    start = input()
    print("Qual a cidade Fim?")
    end = input()
    print("\n\n EXECUÇAO DO ALGORITMO")
    searchWithCustoUniforme(start, end, list_city)

def printMenuProfundidadeLimitada(list_city):
    print("\n\n\n\n Sera Executado Algoritmo Procura Limitada")
    print("Qual a cidade inicio ?")
    start = input()
    print("Qual a cidade Fim?")
    end = input()
    print("Qual o numero limite de profundidade ? (default : 17 ) ")
    limit = int(input())
    print("\n\n EXECUÇAO DO ALGORITMO")
    searchWithProfundidadeLimitada(start, end, list_city,limit)

def printMenuProcuraSofrega(list_city,map_distance_faro):
    print("\n\n\n\n Sera Executado Algoritmo Procura Sofrega")
    print("Qual a cidade inicio ?")
    start = input()
    print("Qual a cidade Fim? (default : faro )")
    end = input()
    print("\n\n EXECUÇAO DO ALGORITMO")
    searchWithProcuraSofrega(start, end, list_city, map_distance_faro)

def printMenuAStar(list_city,map_distance_faro):
    print("\n\n\n\n Sera Executado Algoritmo A*")
    print("Qual a cidade inicio ?")
    start = input()
    print("Qual a cidade Fim?")
    end = input()
    print("\n\n EXECUÇAO DO ALGORITMO")
    searchWithAStar(start, end, list_city,map_distance_faro)
