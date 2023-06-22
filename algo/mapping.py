import algo.findBestLoc as fb # -> run app.py 
# import findBestLoc as fb # -> run map.py 
import algo.astar as ast
# import astar as ast

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
        # self.gedung {
        # "nama gedung" : ["namalantai","namalantai"]
        #   "P" : [''plantai1','plantai2'] # ->
        # }
        self.gedung = {}
        self.countGedung = 0 

        # Contoh struktur lantai
        # self.lantai = {
        #   "plantai1" : [[11100000],[11000000],[0000111]] 0-> itu jalan 1 -> itu gedung
        # }
        self.lantai = {}
        self.countLantai = 0
        
        # total jumlah ruangan 
        self.countRuangan = 0
        self.daftarRuangan = {}

        # self.galon = [object dr galon, object dr galon]
        self.galon = []

        # object dr User
        self.user = User(0,0,'plantai2')

# GEDUNG
    def printGedung(self, namaGedung):
        if namaGedung in self.gedung:
            for row in self.gedung[namaGedung]:
                print(*row)
    
    def createGedung(self, namaGedung,namaLantai):
        if namaGedung not in self.gedung:
            self.gedung[namaGedung] = []
        self.gedung[namaGedung].append(namaLantai)
        self.countGedung += 1

    def isiGedung(self,namaGedung):
        # jadi kalau mau liat di gedung P ada lantai apa aja pake ini. nti keluar array of nama lantai.
        # "P" : [''plantai1','plantai2'] # -> return arraynya
        return self.gedung[namaGedung]

# LANTAI
    def getLantai(self,namaLantai):
         return self.lantai[namaLantai]

    def createLantai(self,namaLantai,namaGedung):
        self.createGedung(namaGedung,namaLantai)
      
        newFloor =  [[0] * 39 for _ in range(10)]
        if namaLantai not in self.lantai or len(self.lantai) == 0:
            self.lantai[namaLantai] = newFloor
        else:
            self.lantai[namaLantai].append(newFloor)

        self.countLantai +=1

    def printLantai(self,namaLantai):
        print('lantai : ',namaLantai)
        for row in self.lantai[namaLantai]:
            print(*row)

    def printAllLantai(self):
         for key, value in self.lantai.items():
            print(key, ' gedung : ')
            for row in value:
                print(' '.join(str(cell) for cell in row))
            print()
    
# RUANGAN
    # setRuangan((xKoor,Y,koor),3,2) jadi parameter pertama masukin x dan y, parameter kedua panjangnya parameter 
    def createRuangan(self,namaLantai,kiriatas,width,height,namaRuangan):
        self.countRuangan += 1
        self.daftarRuangan[self.countRuangan] = Ruangan(namaLantai,namaRuangan,kiriatas,width,height)

        x, y = kiriatas
    
        for i in range(width-1):
            for j in range(height-1):
                # print(self.lantai[namaLantai])
                self.lantai[namaLantai][x+i][y+j] = self.countRuangan
    
# GALON
    def createGalon(self,namaLantai,namaGalon,isigalon,x,y):
        self.lantai[namaLantai][y][x] = -1
        self.galon.append(Galon(namaLantai,namaGalon,isigalon,x,y))
        pass
    def printAllGalon(self):
        for gal in self.galon:
            print('Nama galon : ', gal.namaGalon)
            print('Lantai : ',gal.namaLantai)
            print('x : ',gal.x)
            print('y : ',gal.y)

    def getGalon(self,namaGalon):
        for gal in self.galon:
            if gal.namaGalon == namaGalon:
                return gal
    
# USER
    def setUserLoc(self,x,y):
        self.user.x = x
        self.user.y = y

    def getUserLoc(self):
        return self.user

# ALGORITMA
    def findBestLoc(self):            
        # importing from the findBestLoc
        # cari lokasi galon terbaik
        findBest = fb.Algo()
        # add lokasi galon
        for g in self.galon:
            loc1 = fb.Location(g.namaLantai,g.namaGalon,g.isigalon,g.x,g.y,self.user)
            
            print(loc1.calculate_util())
            findBest.add_loc(loc1)

        galonTerbaik = self.getGalon(findBest.choose_loc())
        print('best galon : ', galonTerbaik.namaGalon)

    #convert to 0 1 for a*
    def convertPath(self,lantai):
        flr = self.lantai[lantai]
        for x in range(len(flr)):
                for y in range(len(flr[0])):
                    if flr[x][y] > 1 :
                        flr[x][y] = 1

        return flr
    
    def createPath(self, lantaiTujuan):
            lantaiAsal = self.user.lantai
            flr = self.lantai[lantaiAsal]
            flr2 = []

            # cek beda gedung
            if lantaiAsal[0] == lantaiTujuan[0]:
                flr2 = self.lantai[lantaiTujuan]
            
            # cek beda lantai
            if lantaiAsal == lantaiTujuan:
                flr = self.lantai[lantaiAsal]

            #convert for A*
            newFlr = self.convertPath(flr)
            newFlr2= self.convertPath(flr2)
            
            # need goal / object's x,y coord to set the 3 for astar
            x = self.user.x
            y = self.user.y

            # goal coords
            # xGoal 
            # yGoal

            # 
            newFlr[x][y]= 2
            newFlr2[10][20]= 3
       
            return flr

            lantaiAsal = self.user.lantai
    
    def constructAPath(self, goal):
        newPath = self.createPath(goal)
        path = ast.a_star(newPath)
        
        if path is None:
            print('No path found!')


themap = Map()
# themap.createLantai('plantai1', 'P')
# themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
# themap.createRuangan('plantai1',(0,9),2,3,'ATK')

# themap.createGalon('plantai1','galon1',90,17,2)
# themap.createGalon('plantai1','galon2',80,27,7)
# themap.createGalon('plantai1','galon3', 100, 20,4)

# themap.createLantai('plantai2', 'P')
# themap.createRuangan('plantai2',(0,0),7,5,'KANTIN')
# themap.createRuangan('plantai2',(0,7),2,5,'ATK')
# themap.createGalon('plantai2', 'galon4', 100, 7, 5)

# themap.printAllLantai()
# themap.printLantai('plantai1')
# themap.printAllGalon()

# themap.findBestLoc()