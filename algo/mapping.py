import algo.findBestLoc as fb # -> run app.py 
# import findBestLoc as fb # -> run map.py 
import algo.astar as ast
import copy
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
        self.user = User(7, 0, 'plantai1')

        # object dr User
        self.arrHasil = []

        # self.petaUkp = agl.Peta()
        self.hasilJalanWeb = []
        self.heu = []

# Peta UKP
    def setHasilJalanWeb(self,array):
        self.hasilJalanWeb = array
    
    def getHasilJalanWeb(self):
        return self.hasilJalanWeb
    
    
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
    def setUserLoc(self,x,y,lantai):
        self.user.x = x
        self.user.y = y
        self.user.lantai = lantai

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
    
        #convert to 0 1 for a*
    def convertPath(self,lantai):
        flr = lantai.copy()
        self.printAllLantai()
        for x in range(len(flr)):
                for y in range(len(flr[0])):
                    if flr[x][y] > 1 :
                        flr[x][y] = 1
        return flr

    def createPath(self):
            # beda lantai tambahan 2 baris
            # beda gedung tambahan 2 column

            self.arrHasil = []
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
            
            for key,val in self.gedung.items():
                temparr = []
                for namalantai in val :
                    temp2arr = []
                    temp2arr = copy.deepcopy(self.lantai[namalantai]) #[:] buat bikin new object supaya self.lantai gk ikutan keganti
                    temp2arr = self.convertPath(temp2arr)
                    temparr = addBottom(temparr, temp2arr)
                if(len(self.arrHasil) == 0):
                    self.arrHasil = addBottom(self.arrHasil,temparr)
                else: 
                    self.arrHasil = addRight(self.arrHasil,temparr)
                temparr = []
            x = self.user.x
            y = self.user.y

             # goal coords
            xGoal, yGoal= self.findBestLoc()
            print(x, y, xGoal, yGoal)
            #convert to index for a*
            self.arrHasil[y][x] = 2
            print(xGoal, yGoal)
            print(self.arrHasil[yGoal][xGoal])
            self.arrHasil[yGoal][xGoal] = 3

            # print(self.arrHasil)
            # for row in self.arrHasil:
            #     print(' '.join(map(str, row)))

            return self.arrHasil


    # add Goal disini setelah user self-pick
    def constructAPath(self):
        newPath = self.createPath() #waktu create path keubah array aslinya error
       
        data = ast.a_star(newPath)
        
        flippedPath = []
        for path in data["path"]:
            flippedPath.append([(coord[1], coord[0]) for coord in path])
        print(flippedPath)
        return flippedPath
    

    def getHeu(self):
        newPath = self.createPath()
        data = ast.a_star(newPath)
        self.heu = data["heu"]

        gedungTemp = []
        counter = 0
        for key,val in self.gedung.items():
            temp = [counter,key]
            counter+=1
            gedungTemp.append(temp)
        
        for i in range(len(self.heu)):
            x = self.heu[i][0]
            y = self.heu[i][1]
            data = self.convertCoordinateToWeb((x,y))
            self.heu[i][0] = data['x']
            self.heu[i][1] = data['y']
            strLantai = data['gedung'].lower()+'lantai'+str(data['lantai'])
            self.heu[i].append(strLantai)

        
        return self.heu
    
    def returnHeu(self):
        return self.heu
    
    # buat array yang gabungan jadi array perlantai dan pergedung baut di webnya
    def convertPathToWeb(self,path):
        newPath = []
        for i in range(len(path)): 
            pathi = path[i]
            x,y = pathi
            data = self.convertCoordinateToWeb((x,y))
            newPath.append(data)
        
        # for i in newPath:
        #     print('gedung ',i['gedung'])
        #     print('lantai ',i['lantai'])
        #     print('x ',i['x'])
        #     print('y ',i['y'])
        return newPath
    
    def convertCoordinateToWeb(self,arrCoor):
        gedungTemp = []
        counter = 0
        for key,val in self.gedung.items():
            temp = [counter,key]
            counter+=1
            gedungTemp.append(temp)

        x,y = arrCoor
        data = {
            "gedung" : 'P',
            "lantai" : 1,
            "x": 0,
            "y": 0,
        }
        countX = 0
        countY = 1

        # beda gedung
        while(x > 38):
            countX+=1
            x -= 39

        # beda lantai
        while(y > 9):
            countY+=1
            y -= 10
        data['gedung'] = gedungTemp[countX][1]
        data['lantai'] = countY
        data["x"] = x
        data["y"] = y
        return data

# TestCase   
# themap = Map()

# themap.createLantai('plantai1','P')
# # bagian kiri
# themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
# themap.createRuangan('plantai1',(8,0),2,3,'ATK')
# themap.createRuangan('plantai1',(0,8),10,2,'KURSI')
# # bagian tengah
# themap.createRuangan('plantai1',(11,0),6,1,'TOILET')
# themap.createRuangan('plantai1',(12,1),4,1,'LIFT')
# themap.createRuangan('plantai1',(11,8),6,2,'TANGGA')
# themap.createRuangan('plantai1',(17,3),1,2,'MEJA')
# themap.createRuangan('plantai1',(16,6),2,1,'MEJA')
# # bagian kanan
# themap.createRuangan('plantai1',(18,0),6,5,'LAB FISIKA')
# themap.createRuangan('plantai1',(24,1),1,4,'LIFT')
# themap.createRuangan('plantai1',(19,6),2,1,'MEJA')
# themap.createRuangan('plantai1',(22,6),2,1,'MEJA')
# themap.createRuangan('plantai1',(25,6),2,1,'MEJA')
# themap.createRuangan('plantai1',(28,6),2,1,'MEJA')
# themap.createRuangan('plantai1',(18,8),7,2,'KURSI')
# themap.createRuangan('plantai1',(26,9),1,1,'') # tangga
# themap.createRuangan('plantai1',(28,8),7,2,'LAB T. INDUSTRI')
# themap.createRuangan('plantai1',(35,8),2,2,'UPPK')
# themap.createRuangan('plantai1',(37,8),2,2,'KONSELING')
# themap.createRuangan('plantai1',(26,0),9,2,'LAB T. INDUSTRI')
# themap.createRuangan('plantai1',(36,0),3,2,'TOILET')
# themap.createRuangan('plantai1',(35,3),2,1,'MEJA')
# # galon p lt 1
# themap.createGalon('plantai1','plantai11',90,17,2)
# themap.createGalon('plantai1','plantai12',80,27,7)

# # P lantai 2
# themap.createLantai('plantai2','P')
# # bagian kiri
# themap.createRuangan('plantai2',(0,0),3,4,'P.204')
# themap.createRuangan('plantai2',(3,0),4,4,'LAB SI')
# themap.createRuangan('plantai2',(7,0),3,4,'LAB PG')
# themap.createRuangan('plantai2',(0,6),3,4,'P.203')
# themap.createRuangan('plantai2',(3,6),3,4,'P.202')
# themap.createRuangan('plantai2',(6,6),2,4,'LAB STUDIO')
# themap.createRuangan('plantai2',(8,6),2,4,'LAB MOBDEV')
# # bagian tengah
# themap.createRuangan('plantai2',(10,4),1,1,'') # tiang
# themap.createRuangan('plantai2',(12,4),1,1,'') # tiang
# themap.createRuangan('plantai2',(13,3),2,3,'MEJA')
# themap.createRuangan('plantai2',(15,4),1,1,'') # tiang
# themap.createRuangan('plantai2',(16,3),1,3,'MEJA')
# themap.createRuangan('plantai2',(17,4),1,2,'LOKER')
# themap.createRuangan('plantai2',(11,0),6,1,'TOILET')
# themap.createRuangan('plantai2',(12,1),4,1,'LIFT')
# themap.createRuangan('plantai2',(11,8),6,2,'TANGGA')
# themap.createRuangan('plantai2',(10,9),1,1,'') # sambungan kiri tangga
# themap.createRuangan('plantai2',(17,9),1,1,'') # sambungan kanan tangga
# # bagian kanan
# themap.createRuangan('plantai2',(18,0),5,2,'LAB JK')
# themap.createRuangan('plantai2',(23,0),5,2,'LAB SC')
# themap.createRuangan('plantai2',(18,8),7,2,'LAB MM')
# themap.createRuangan('plantai2',(28,0),11,8,'PUSKOM P')
# themap.createRuangan('plantai2',(27,8),12,2,'LAB PRODI T. MESIN')
# themap.createRuangan('plantai2',(26,9),1,1,'') # tangga
# themap.createRuangan('plantai2',(23,4),2,2,'LIFT')
# themap.createRuangan('plantai2',(26,4),1,2,'MEJA')
# # galon p lt 2
# themap.createGalon('plantai2','plantai21',50,9,4)
# themap.createGalon('plantai2','plantai22',75,27,7)

# # # themap.printAllLantai()
# # # themap.printLantai('plantai2')
# # # themap.printAllGalon()

# themap.findBestLoc()
# # themap.createPath()
# print(themap.constructAPath())
# # print(themap.getHeu())