#IMPORTS
from classes import *

#FUNCTIONS
def loadCityMap(filename,listcity):
    file = open(filename,"r")
    for line in file: 
        added = 0  #checks if is a new city or a existing one
        line_split = line.split(",") # [0] = city ,[1] = neighbour,[2] = distance
        for city in listcity:
            if(city.name == line_split[0]):
                city.addChild(line_split[1],int(line_split[2]))
                added = 1
                break
        if(added == 0):
            newcity = City(line_split[0])
            newcity.addChild(line_split[1],int(line_split[2]))
            listcity.append(newcity)

def loadMapDistanceFaro(filename, map_distance_faro):
    file = open(filename,"r")
    for line in file:
        line_split = line.split(",") #[0]-city name ,[1]-distance
        map_distance_faro.append(MapDistanceFaro(line_split[0], int(line_split[1])))

def printCityMap(listcity):
    for city in listcity:
        print("City : ",city.name)
        print("Neighbours:")
        for child in city.child:
            print("\t {} - {}".format(child.name, child.cost))

def printMapDistanceFaro(map_distance_faro):
    for content in map_distance_faro:
        print("City {} is {} distance from Faro".format(content.name,content.distance))
