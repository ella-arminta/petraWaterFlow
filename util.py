class Location:
    def __init__(self, name, kondisi, koordinat):
        self.name = name
        self.kondisi = kondisi
        self.start = 0
        self.koordinat = koordinat
        self.utility =self.calculate_utility()

    def calculate_distance(self, start, end):
        # Calculate the distance between two positions (e.g., using Euclidean distance)
        # Modify this function based on your specific problem's distance calculation
        # return (self.koordinat[0][0]-self.start[0][0]) * 2 + (self.koordinat[0][1]-self.start[0][1]) * 2 * 0.5
        return self.koordinat-self.start *2 * 0.5

    def calculate_utility(self):
        # Calculate the utility of a node based on distance and water quality
        # Modify this function based on your specific problem's utility calculation
        distance_utility = 1 / (self.calculate_distance(self.start, self.koordinat) + 1)
        water_quality_utility = self.kondisi / 100
        return distance_utility + water_quality_utility


class Algo:
    def __init__(self):
        self.locs = []
    
    def add_loc(self, location):
        self.locs.append(location)

    def choose_action(self):
        highest = float("-inf") #positive infinity
        best = []

        for locs in self.locs:
            if locs.utility > highest:
                highest = locs.utility
                best.append(locs.name)

        return best
    
# class User :
#     def __init__(self,lokasi):
#         self.lokasi = lokasi


# class Galon:
#     def __init__(self, kondisi):
#         self.location = Location
#         self.kondisi = kondisi
    
#     def update_isi(name, newKondisi):
#         self.kondisi = newKondisi
    
findBestRoute = Algo()
# usr = User(0)

loc1 = Location("1", 80, 25)
loc2 = Location("2", 30,30)
loc3 = Location("3", 100,50)
loc4 = Location("4", 70, 30)
loc5 = Location("5", 75, 10)
print(loc1.calculate_utility())
print(loc2.calculate_utility())
print(loc3.calculate_utility())
print(loc4.calculate_utility())
print(loc5.calculate_utility())

print(loc1.calculate_distance(loc1.start, loc1.koordinat))
print(loc2.calculate_distance(loc2.start, loc2.koordinat))
print(loc3.calculate_distance(loc3.start, loc3.koordinat))
print(loc4.calculate_distance(loc4.start, loc4.koordinat))
print(loc5.calculate_distance(loc5.start, loc5.koordinat))

findBestRoute.add_loc(loc1)
findBestRoute.add_loc(loc2)
findBestRoute.add_loc(loc3)
findBestRoute.add_loc(loc4)
findBestRoute.add_loc(loc5)
best_route = findBestRoute.choose_action()
print(best_route)
# jarak_user = usr.lokasi - best_route.
print()







    