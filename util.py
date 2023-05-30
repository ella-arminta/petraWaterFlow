class Location:
    def __init__(self, name, kondisi, koordinat, User):
        self.name = name
        self.kondisi = kondisi
        self.start = User.lokasi
        self.koordinat = koordinat
        self.utility =self.calculate_utility()

    def calculate_distance(self, start, end):
        return self.koordinat-self.start *2 * 0.5

    def calculate_utility(self):
        distance_utility = 1 / (self.calculate_distance(self.start, self.koordinat) + 1)
        water_quality_utility = self.kondisi / 100
        return distance_utility + water_quality_utility


class Algo:
    def __init__(self):
        self.locs = []
    
    def add_loc(self, location):
        self.locs.append(location)

    def choose_loc(self):
        highest = float("-inf") #positive infinity
        best = None

        for locs in self.locs:
            if locs.utility > highest:
                highest = locs.utility
                best = locs.name

        return best
       
    
class User :
    def __init__(self,lokasi):
        self.lokasi = 0


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

findBestRoute.add_loc(loc1)
findBestRoute.add_loc(loc2)
findBestRoute.add_loc(loc3)
findBestRoute.add_loc(loc4)
findBestRoute.add_loc(loc5)

# print(loc1.calculate_distance(loc1.start, loc1.koordinat))
# print(loc2.calculate_distance(loc2.start, loc2.koordinat))
# print(loc3.calculate_distance(loc3.start, loc3.koordinat))
# print(loc4.calculate_distance(loc4.start, loc4.koordinat))
# print(loc5.calculate_distance(loc5.start, loc5.koordinat))

best_route = findBestRoute.choose_loc()
print(best_route)
# jarak_user = usr.lokasi - best_route.
print()







    