# import algo.findBestLoc as fb # -> run app.py 
import findBestLoc as fb # -> run map.py 
# import algo.astar as ast
import astar as ast


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
        self.user = User(14,0,'plantai1')

        # self.petaUkp = agl.Peta()

# Peta UKP
    def add_edge_petaUkp(self,area1:str,area2:str,cost):
        self.petaUkp.add_edge(area1,area2,cost)

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
    
    def getGedungDariLantai(self,lantai):
        for key, value in self.gedung.items():
            if lantai in value:
                return key
        return None


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
    def createRuangan(self,namaLantai,kiriatas,width,height,namaRuangan):
        self.countRuangan += 1
        self.daftarRuangan[self.countRuangan] = Ruangan(namaLantai,namaRuangan,kiriatas,width,height)

        x,y = kiriatas
    
        for i in range(height):
            for j in range(width):
                # print(self.lantai[namaLantai])
                # print('koordinat ',(x+j),' ',(y+i))
                # self.printLantai('plantai2')
                self.lantai[namaLantai][y+i][x+j] = self.countRuangan
    
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
    
# USER
    def setUserLoc(self,x,y):
        self.user.x = x
        self.user.y = y

    def getUserLoc(self):
        return self.user

# ALGORITMA
    def findBestLoc(self):            
        # importing from findBestLoc
        findBest = fb.Algo()

        # add lokasi galon
        for g in self.galon:
            loc1 = fb.Location(g.namaLantai,g.namaGalon,g.isigalon,g.x,g.y,self.user)

            print(loc1.calculate_util())
            findBest.add_loc(loc1)
            
        galonTerbaik = findBest.choose_loc()
        print('best galon : ', galonTerbaik.namaGalon)

        return galonTerbaik.x, galonTerbaik.y
    
        # self.createPath()
    
        #convert to 0 1 for a*
    def convertPath(self,lantai):
        flr = lantai
        for x in range(len(flr)):
                for y in range(len(flr[0])):
                    if flr[x][y] > 1 :
                        flr[x][y] = 1

        return flr

    def createPath(self):
            # beda lantai tambahan 2 baris
            # beda gedung tambahan 2 column
            # masukin semua gedung ke 1 array

            arrHasil = []
            width = 39
            def addBottom(arraytujuan,array):
                # tambaham 2 baris
                # arrZero = [0]*len(array)
                # arraytujuan.extend(arrZero)
                # arraytujuan.extend(arrZero)

                # tambah array lantai
                arraytujuan.extend(array)
                return arraytujuan

            def addRight(arraytujuan,array):
                rows = len(arraytujuan)
                cols = width
                for i in range(len(array)):
                    arraytujuan[i].extend(array[i])
                    arraytujuan[i] += [8] * (cols - len(array[i]))

                # supaya gk bolong
                for i in range(len(arraytujuan)):
                    print('loop ',i,'count ',len(arraytujuan[i]))
                    if len(arraytujuan[i]) < len(arraytujuan[0]):
                        count = len(arraytujuan[0]) - len(arraytujuan[i])
                        for j in range(count):
                            arraytujuan[i].append(1)
                return arraytujuan
            
            # print(self.gedung)
            for key,val in self.gedung.items():
                temparr = []
                for namalantai in val :
                    temp2arr = self.convertPath(self.lantai[namalantai])
                    temparr = addBottom(temparr, temp2arr)
                if(len(arrHasil) == 0):
                    arrHasil = addBottom(arrHasil,temparr)
                else: 
                    # tambahan = [['x' for _ in range(2)] for _ in range(len(arrHasil))]
                    # arrHasil = addRight(arrHasil,tambahan)
                    arrHasil = addRight(arrHasil,temparr)
                temparr = []
                
            x = self.user.x
            y = self.user.y

             # goal coords
            xGoal, yGoal= self.findBestLoc()

            #convert to index for a*
            arrHasil[y][x] = 2
            print(xGoal, yGoal)
            print(arrHasil[yGoal][xGoal])
            arrHasil[yGoal][xGoal] = 3

            # print(arrHasil)
            # for row in arrHasil:
            #     print(' '.join(map(str, row)))

            return arrHasil


            # pathToFind = []
            # # testing user dan galon
            # # cek beda lantai gk
            # print(self.lantai)
            # flr = self.lantai[lantaiasal]
            # flr2 = self.lantai[lantaitujuan]
            # print(flr)
            # print(flr2)
            # for x in range(len(flr)):
            #    for y in range(len(flr[0])):
            #        if flr[x][y] > 1 :
            #             flr[x][y] = 1

    # add Goal disini setelah user self-pick
    def constructAPath(self):
        newPath = self.createPath()
        data = ast.a_star(newPath)
        print (data["path"])
        return data["path"]
    
    # def getData(self):
    #     newPath = self.createPath()
    #     data = ast.a_star(newPath)

    #     dataFiltered = ast.filterData(data)
    #     print(dataFiltered["g"])
       
        
        


themap = Map()


themap.createLantai('plantai1', 'P')
themap.createLantai('plantai2', 'P')
themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
themap.createRuangan('plantai1',(10,4),4,2,'ATK')
themap.createRuangan('plantai2',(0,0),7,5,'KANTIN')
themap.createRuangan('plantai2',(10,4),4,2,'ATK')


# themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
# themap.createRuangan('plantai1',(0,9),2,3,'ATK')

themap.createGalon('plantai1','galon1',90,17,2)
themap.createGalon('plantai1','galon2',80,27,7)
themap.createGalon('plantai1','galon3', 100, 13,4)

themap.createLantai('wlantai1','W')
themap.createRuangan('wlantai1',(0,0),7,5,'HEHE')

themap.printAllLantai()
themap.printLantai('plantai2')
themap.printAllGalon()

themap.findBestLoc()
themap.createPath()
themap.constructAPath()

# themap.createLantai('plantai2', 'P')
# themap.createRuangan('plantai2',(0,0),7,5,'KANTIN')
# themap.createRuangan('plantai2',(0,7),2,5,'ATK')
# themap.createGalon('plantai2', 'galon4', 100, 7, 5)

# themap.printAllLantai()
# themap.printLantai('plantai1')
# themap.printAllGalon()

# themap.findBestLoc()
