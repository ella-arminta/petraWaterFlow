import algo.findBestLoc as fb # -> kalo dirun di app.py pake ini
# import findBestLoc as fb # -> kalo dirun di map.py pake ini
import algo.astar as ast
# import astar as ast
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

class Ruangan:
     def __init__(self,namaLantai,namaRuangan,koordinat,width,height):
          self.namaRuangan = namaRuangan
          self.namaLantai = namaLantai
          x,y = koordinat
          self.startX = x
          self.startY = y
          self.width = width
          self.height = height
     
class Map():
    def __init__(self) -> None:
        self.lantai = {}
        self.countRuangan = 0
        self.daftarRuangan = {}
        self.galon = []
        self.user = User(14,0)

    def getLantai(self,namaLantai):
         return self.lantai[namaLantai]

    def createLantai(self,namaLantai):
        self.lantai[namaLantai] =  [[0] * 39 for _ in range(10)]

    # setRuangan((xKoor,Y,koor),3,2) jadi parameter pertama masukin x dan y, parameter kedua panjangnya parameter 
    def createRuangan(self,namaLantai,kiriatas,width,height,namaRuangan):
        self.countRuangan += 1
        self.daftarRuangan[self.countRuangan] = Ruangan(namaLantai,namaRuangan,kiriatas,width,height)

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

    def getUserLoc(self):
        return self.user

    def findBestLoc(self):
        findBest = fb.Algo()
        # add lokasi galon
        for g in self.galon:
            # newGalon =Galon(g.namaLantai,g.namaGalon,g.isigalon,g.x,g.y)
            loc1 = fb.Location(g.namaLantai,g.namaGalon,g.isigalon,g.x,g.y,self.user)
            
            print(loc1.calculate_util())
            findBest.add_loc(loc1)
        #     self.galon.append(g)

        return findBest.choose_loc()
    
    def createPath(self, lantai):
        flr = self.lantai[lantai]
    
        for x in range(len(flr)):
            for y in range(len(flr[0])):
                if flr[x][y] > 1 :
                    flr[x][y] = 1

        flr[7][2]= 2
        flr[3][20]=3
        # for row in flr:
        #     print(*row)

        return flr
    
    def findPath(self, lantai):
        newPath = self.createPath(lantai)
        path = ast.a_star(newPath)
        
        # if path is None:
        #     print('No path found!')


themap = Map()
themap.createLantai('plantai1')
themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
themap.createRuangan('plantai1',(0,9),2,3,'ATK')
# themap.createRuangan('plantai1', (0, 15), 5, 10, 'NONGKI')
themap.createGalon('plantai1','plantai11',90,17,2)
themap.createGalon('plantai1','plantai12',80,27,7)
themap.createGalon('plantai1','plantai13', 100, 20,4)
themap.printLantai('plantai1')
print('best:',themap.findBestLoc())
# themap.findPath('plantai1')