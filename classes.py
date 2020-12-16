#CLASSES 
class CityChild:  # class to save child and cost
    def __init__(self, name, cost):  # create child with (name,cost)
        self.name = name
        self.cost = cost

class City:  # class to save the city and  childs+cost
    def __init__(self, name):  # add parent to list of parent
        self.name = name
        self.child = []

    def addChild(self, name, cost):  # add child to the list of childs
        self.child.append(CityChild(name, cost))

    def printChild(self):  # print all childs of city
        for cityP in self.child:
            print("child :", cityP.name, cityP.cost)

class MapDistanceFaro: #class to save distance from a city to Faro
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

class Path:   # class to save paths discovered
    def __init__(self,name,cost):
        self.name = []
        self.name.append(name)
        self.cost = cost

class PathDepth:#class to save path discoved in profundidade limitada 
    def __init__(self,name,cost,depth):
        self.name = []
        self.name.append(name)
        self.cost = cost
        self.depth = depth

