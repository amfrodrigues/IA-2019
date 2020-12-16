#IMPORTS 
from classes import *
import copy


#FUNCTIONS
def getCity(name,list_city):
    for city in list_city:
        if (city.name == name):
            return city


def printIteration2(count_iterations,list_path):
    print(" {} -> ".format(count_iterations), end="")
    print("\t | {} - [{}] |".format(list_path[0].name,list_path[0].cost))
    
def printIteration(count_iterations, list_path):
    print(" {} -> ".format(count_iterations), end="")
    for path in list_path:
        print("\t | {}-[{}] |".format(path.name, path.cost), end="")
    print("\n")


def printPath(count_iterations, path_found):
    print("PATH FOUND IS -> ", end="")
    for city_name in path_found:
        print(" {}  ".format(city_name), end="")
    print("with {} iterations".format(count_iterations)) 

def printIterationsDepth(count_iterations,list_path):
    print("{} ->".format(count_iterations),end="")
    for path in list_path:
        print("\t| {}-[{}]-({}) |".format(path.name,path.cost,path.depth),end="")
    print("\n")

def printPathDepth(count_iterations,path_found):
    print("PATH FOUND IS -> ", end="")
    for city_name in path_found.name[::-1]:
        print(" {}  ".format(city_name), end="")
    print("in depth {} with {} iterations".format(path_found.depth,count_iterations))
    
def bubbleSortByCost(list_path):
    n = len(list_path)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if list_path[j].cost > list_path[j+1].cost:
                list_path[j], list_path[j+1] = list_path[j+1], list_path[j]
                swapped = True
        if swapped == False:
            break

def getDistanceToFaro(city_name, map_distance_faro):
    for city in map_distance_faro:
        if(city.name==city_name):
            return city.distance
    return -1

def checkExistingPath(city_name,list_path):
    for path in list_path:
        if (path.name[0] == city_name):
            return True
    return False 
