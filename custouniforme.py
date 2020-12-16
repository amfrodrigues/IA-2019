#IMPORTS
from util import *
from classes import *

#FUNCTIONS 
def searchWithCustoUniforme(inicio ,destino,list_city):
    list_path = [] #empty list 
    city = getCity(inicio,list_city)
    list_path.append(Path(city.name,0)) # puts the starting object on the list
    count_iterations = 1
    printIteration(count_iterations,list_path)
    while (list_path[0].name[0] != destino):
        count_iterations += 1

        doAlgorith(list_path,list_city) # execute the algorith
        del list_path[0] #deletes the path that isnt valid and was used on the algorith
        bubbleSort(list_path); # orders the list by cost
        printIteration(count_iterations,list_path) # print info of iterations break point here to stop iterations
        
        if(not list_path):
            break
    if(not list_path):
        print("PATH NOT FOUND")
    else:
        printPath(count_iterations,list_path[0].name[::-1])
        
def doAlgorith(list_path,list_city): # path search algorith 
    new_list_city = copy.deepcopy(list_city)
    old_cost = list_path[0].cost
    city = getCity(list_path[0].name[0],new_list_city)
    # maybe add check_up for null values 
    for child_city in city.child: # add neighbours to the valid path 
        new_path = Path(child_city.name,(child_city.cost+old_cost))
        new_path.name.extend(list_path[0].name)
        list_path.append(new_path)
        
def bubbleSort(list_path):
    n = len(list_path)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if list_path[j].cost > list_path[j+1].cost:
                list_path[j],list_path[j+1] = list_path[j+1],list_path[j]
                swapped = True
        if swapped == False:
            break
