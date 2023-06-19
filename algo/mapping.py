# import algo.findBestLoc as fb # -> kalo dirun di app.py pake ini
import findBestLoc as fb # -> kalo dirun di map.py pake ini
# import algo.astar as ast
import astar as ast
import math

class User :
     def __init__(self,x, y, lantai):
        self.x = x
        self.y = y
        self.lantai = lantai

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
    def __init__(self):
        
        # Contoh struktur lantai
        # self.lantai = {
        #   "plantai1" : [[11100000],[11000000],[0000111]] 0-> itu jalan 1 -> itu gedung
        # }
        self.lantai = {}
        
        # total jumlah ruangan yg ada digedung dan lantai manapun
        self.countRuangan = 0
        self.daftarRuangan = {}

        # self.galon = [object dr galon, object dr galon]
        self.galon = []

        # object dr User
        self.user = User(14,0,'plantai1')

        # self.gedung {
        # "nama gedung" : ["namalantai","namalantai"]
        #   "P" : [''plantai1','plantai2'] # ->
        # }

    def getLantai(self,namaLantai):
         return self.lantai[namaLantai]

    def createLantai(self,namaLantai,namaGedung):
        self.createGedung(namaGedung,namaLantai)
        # self.lantai[namaLantai] =  [[0] * 39 for _ in range(10)]
        newFloor =  [[0] * 39 for _ in range(10)]
        if namaLantai not in self.lantai or len(self.lantai) == 0:
            self.lantai[namaLantai] = newFloor
        else:
            self.lantai[namaLantai].append(newFloor)
    
    # vee ini create gedung bentuk e gini ya nanti : 
    # self.gedung {
        # "nama gedung" : ["namalantai","namalantai"]
    #   "P" : [''plantai1','plantai2'] # ->
    # }
    def createGedung(self, namaGedung,namaLantai):
        if namaGedung not in self.gedung:
            self.gedung[namaGedung] = []
        self.gedung[namaGedung].append(namaLantai)

    def getLantaisFromGedung(self,namaGedung):
        # jadi kalau mau liat di gedung P ada lantai apa aja pake ini. nti keluar array of nama lantai.
        return self.gedung[namaGedung]

    # code lama : 
    # def createGedung(self, namaGedung, namaLantai):
    #     arrLantai = self.lantai[namaLantai]
    #     for i in len(arrLantai):
    #         self.gedung[namaGedung] = self.lantai[namaLantai]
            

    # setRuangan((xKoor,Y,koor),3,2) jadi parameter pertama masukin x dan y, parameter kedua panjangnya parameter 
    def createRuangan(self,namaLantai,kiriatas,width,height,namaRuangan):
        self.countRuangan += 1
        self.daftarRuangan[self.countRuangan] = Ruangan(namaLantai,namaRuangan,kiriatas,width,height)

        
        x, y = kiriatas
    
        for i in range(width-1):
            for j in range(height-1):
                # print(self.lantai[namaLantai])
                self.lantai[namaLantai][x+i][y+j] = self.countRuangan

    def printLantai(self,namaLantai):
        for row in self.lantai[namaLantai]:
            print(*row)

    def printAllLantai(self):
         for key, value in self.lantai.items():
            print(key)
            for row in value:
                print(' '.join(str(cell) for cell in row))
            print()

    def printGedung(self, namaGedung):
        for row in self.gedung[namaGedung]:
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
            
        lantaiAsal = self.user.lantai
        lantaiAsal = 'plantai1'
        lantaitujuan = 'plantai2'
        self.createPath(lantaiAsal,lantaitujuan)

        # findBest = fb.Algo()
        # # add lokasi galon
        # for g in self.galon:
        #     loc1 = fb.Location(g.namaLantai,g.namaGalon,g.isigalon,g.x,g.y,self.user)
            
        #     print(loc1.calculate_util())
        #     findBest.add_loc(loc1)


        # return findBest.choose_loc()
    
    # def createPath(self,lantaiasal,lantaitujuan):
    #         # cek beda gedung gak
    #         # # cek beda lantai gk
    #         # print(self.lantai)
    #         flr = self.lantai[lantaiasal]
    #         flr2 = self.lantai[lantaitujuan]
    #         print(flr)
    #         print(flr2)
    #         # for x in range(len(flr)):
    #         #     for y in range(len(flr[0])):
    #         #         if flr[x][y] > 1 :
    #         #             flr[x][y] = 1

    #         flr[7][2]= 2
    #         flr[3][20]=3
    #         # for row in flr:
    #         #     print(*row)

    #         return flr
    
    # def findPath(self, lantai):
    #     newPath = self.createPath(lantai, lantaitu)
    #     path = ast.a_star(newPath)
        
        # if path is None:
        #     print('No path found!')


themap = Map()
themap.createLantai('plantai1', 'P')
themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
themap.createRuangan('plantai1',(0,9),2,3,'ATK')

# themap.createRuangan('plantai1', (0, 15), 5, 10, 'NONGKI')
themap.createGalon('plantai1','plantai11',90,17,2)
themap.createGalon('plantai1','plantai12',80,27,7)
themap.createGalon('plantai1','plantai13', 100, 20,4)
# themap.printLantai('plantai1')
# print('best:',themap.findBestLoc())
# themap.findPath('plantai1')

themap.createLantai('plantai2', 'P')
themap.createRuangan('plantai2',(0,0),7,5,'KANTIN')
themap.createRuangan('plantai2',(0,7),2,5,'ATK')
# themap.createRuangan('plantai1', (0, 15), 5, 10, 'NONGKI')
# themap.createGalon('plantai2','plantai21',90,17,2)
# themap.createGalon('plantai2','plantai22',80,27,7)
# themap.createGalon('plantai2','plantai23', 100, 20,4)
themap.printAllLantai()
themap.printGedung('P')
# themap.findBestLoc()
# themap.printLantai('plantai2')
# print('best:',themap.findBestLoc())
# themap.findPath('plantai1')




# RETURN PATH DLM BENTUK ARRAY OF COORDINATES
# FIGURE OUT BEDA LANTAI