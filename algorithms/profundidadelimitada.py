#IMPORTS
from classes import *
from util import *

#FUNCTIONS
def searchWithProfundidadeLimitada(start,end,list_city,limit_search): # search using depth based algorith receives (start point,end point,city,limit depth) receives limit depth so it can be used for progressive depth search algorith 
    list_path = []
    list_path.append(PathDepth(start,0,0))
    count_iterations = 0
    printIterationsDepth(count_iterations, list_path)
    while(list_path[0].name[0] != end):
        count_iterations +=1
        if(list_path[0].depth < limit_search):
            doAlgorithmProfundidadeLimitada(list_path, list_city, limit_search)
        else:
            del(list_path[0])
        if (not list_path):
            break
        printIterationsDepth(count_iterations,list_path)
    if(not list_path):
        print("PATH NOT FOUND")
    else:
        printPathDepth(count_iterations,list_path[0])
        
def doAlgorithmProfundidadeLimitada(list_path,list_city,limit_search):
    new_list_city = copy.deepcopy(list_city)
    old_cost = list_path[0].cost
    old_depth = list_path[0].depth
    old_trajectory = copy.copy(list_path[0].name)
    city = getCity(list_path[0].name[0],new_list_city)
    #delete path searched because all associated variables are already saved
    del(list_path[0])
    for child_city in city.child:
        new_path = PathDepth(child_city.name,child_city.cost+old_cost,old_depth+1)
        new_path.name.extend(old_trajectory)
        list_path.insert(0,new_path)
        
        
