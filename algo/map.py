import algo.findBestLoc as fb # -> kalo dirun di app.py pake ini
# import findBestLoc as fb # -> kalo dirun di map.py pake ini
import math
class User :
            def __init__(self,x, y):
                self.x = x
                self.y = y
class Galon:
     def __init__(self,namaLantai,namaGalon,isigalon,x,y):
          self.isigalon = isigalon
          self.namaLantai = namaLantai
          self.namaGalon = namaGalon
          self.x = x
          self.y = y

class Map():
    def __init__(self) -> None:
        self.lantai = {}
        self.countRuangan = 0
        self.daftarRuangan = {}
        self.galon = []
        self.user = User(0,0)

    def getLantai(self,namaLantai):
         return self.lantai[namaLantai]

    def createLantai(self,namaLantai):
        self.lantai[namaLantai] =  [[0] * 39 for _ in range(10)]

    # setRuangan((xKoor,Y,koor),3,2) jadi parameter pertama masukin x dan y, parameter kedua panjangnya parameter 
    def createRuangan(self,namaLantai,kiriatas,width,height,namaRuangan):
        self.countRuangan += 1
        self.daftarRuangan[self.countRuangan] = namaRuangan
        lantai = self.lantai[namaLantai]
        x, y = kiriatas
        for i in range(width):
            lantai[x][y+i] = self.countRuangan
            for j in range(height):
                lantai[x+j][y+i] = self.countRuangan

    def printLantai(self,namaLantai):
        for row in self.lantai[namaLantai]:
            print(*row)
    
    def createGalon(self,namaLantai,namaGalon,isigalon,x,y):
        # print('isigalon ',isigalon)
        # print('x',x)
        # print('y',y)
        # print(self.lantai[namaLantai][y])
        self.lantai[namaLantai][y][x] = -1
        self.galon.append(Galon(namaLantai,namaGalon,isigalon,x,y))
        pass

    def setUserLoc(self,x,y):
        self.user.x = x
        self.user.y = y

    def findBestLoc(self):
        findBest = fb.Algo()

        # add lokasi galon
        for g in self.galon:
             loc1 = fb.Location(g.namaLantai,g.namaGalon,g.isigalon,g.x,g.y,self.user)
             findBest.add_loc(loc1)

        return findBest.choose_loc()
            
        


# themap = Map()
# themap.createLantai('plantai1')
# themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
# themap.createGalon('plantai1','plantai11',90,17,2)
# themap.createGalon('plantai1','plantai12',80,27,7)
# themap.printLantai('plantai1')
# print(themap.findBestLoc())