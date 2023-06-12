import math

class Location:
    def __init__(self, name, galon, x, y):
        self.usr = User
        self.name = name
        self.galon = galon
        self.start_x = usr.x
        self.start_y = usr.y
        self.x = x
        self.y = y
        self.utility = self.calculate_util()
        self.distance = self.calculate_distance()

    def calculate_distance(self):
        return math.sqrt(pow((self.x - self.start_x),2) + pow((self.y - self.start_y),2))

    def calculate_util(self):
        distance_utility = 1 / (self.calculate_distance() + 1)
        water_quality_utility = self.galon / 100
        return distance_utility + water_quality_utility


class Algo:
    def __init__(self):
        self.locs = []
    
    def add_loc(self, location):
        self.locs.append(location)

    def choose_loc(self):
        # highest = float("-inf")
        # best = None

        # for locs in self.locs:
        #     if locs.utility > highest:
        #         highest = locs
            
        # return highest.name    
        # 
        return sorted(self.locs, key=lambda x: (x["dist"])) 
    
    # def calculateUtil(self):
    #     normalizedDistance = []
    #     normalizedGalon = []
    #     utility = []

    #     for locs in self.locs:
    #        normalizedDistance.append(self.get_highest*locs.distance) 
    #        normalizedGalon.append(100*locs.galon)

    #     for norm in normalizedDistance:
    #         utility.append(norm-normalizedGalon/norm-normalizedDistance)

    #     return utility
                       
           

        
    
class User :
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
findBestRoute = Algo()
usr = User(0,30)

loc1 = Location("1", 70, 100, 35)
loc2 = Location("2", 80, 5, 20)
loc3 = Location("3", 20, 50, 30)
loc4 = Location("4", 70, 40, 20)
loc5 = Location("5", 75, 5, 70)

print(loc1.calculate_distance())
print(loc2.calculate_distance())
print(loc3.calculate_distance())
print(loc4.calculate_distance())
print(loc5.calculate_distance())

print()

print(loc1.calculate_util())
print(loc2.calculate_util())
print(loc3.calculate_util())
print(loc4.calculate_util())
print(loc5.calculate_util())

findBestRoute.add_loc(loc1)
findBestRoute.add_loc(loc2)
findBestRoute.add_loc(loc3)
findBestRoute.add_loc(loc4)
findBestRoute.add_loc(loc5)

best_route = findBestRoute.choose_loc()
print(best_route)
print()







    