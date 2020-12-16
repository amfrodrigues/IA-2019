#IMPORTS
from util import *
from classes import *

#FUNCTIONS 
def searchWithCustoUniforme(start ,end,list_city):#searchs using cost based algorith receives (start point ,end point,list of citys)
    list_path = [] #empty list 
    list_path.append(Path(start,0)) # puts the starting object on the list
    count_iterations = 0
    printIteration(count_iterations,list_path)
    while (list_path[0].name[0] != end):
        count_iterations += 1
        doAlgorithmCustoUniforme(list_path,list_city) # execute the algorith  
        if(not list_path):
            break
        bubbleSortByCost(list_path); # orders the list by cost
        printIteration2(count_iterations,list_path) # print info of iterations break point here to stop iterations
        
    if(not list_path):
        print("PATH NOT FOUND")
    else:
        printPath(count_iterations,list_path[0].name[::-1])
        
def doAlgorithmCustoUniforme(list_path,list_city): # path search algorith 
    new_list_city = copy.deepcopy(list_city)
    old_cost = list_path[0].cost
    city = getCity(list_path[0].name[0],new_list_city)
    for child_city in city.child: # add neighbours to the valid path 
        new_path = Path(child_city.name,(child_city.cost+old_cost))
        new_path.name.extend(list_path[0].name)
        list_path.append(new_path)
    # deletes the path first because isnt valid and was used on the algorith
    del list_path[0]
        

