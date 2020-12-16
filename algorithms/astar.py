#IMPORTS
from util import *
from classes import *

#FUNCTIONS
def searchWithAStar(start,end,list_city,map_distance_faro):
    list_path = []
    list_path.append(Path(start,getDistanceToFaro(start,map_distance_faro)))
    count_iterations = 0
    printIteration(count_iterations,list_path)
    while(list_path[0].name[0] != end):
        count_iterations +=1
        doAlgorithAStar(list_path,list_city,map_distance_faro)
        if(not list_path):
            break
        bubbleSortByCost(list_path)
        printIteration(count_iterations,list_path)
    if(not list_path):
        print("PATH NOT FOUND")
    else:
        printPath(count_iterations, list_path[0].name[::-1])

def doAlgorithAStar(list_path, list_city, map_distance_faro):
    new_list_city = copy.deepcopy(list_city)
    new_map_distance_faro = copy.deepcopy(map_distance_faro)
    city = getCity(list_path[0].name[0], new_list_city)
    old_cost = list_path[0].cost - getDistanceToFaro(list_path[0].name[0],new_map_distance_faro)
    for city_child in city.child:
        total_cost = city_child.cost + old_cost + getDistanceToFaro(city_child.name,new_map_distance_faro) 
        new_path = Path(city_child.name,total_cost)
        new_path.name.extend(list_path[0].name)
        list_path.append(new_path)
    del(list_path[0])
