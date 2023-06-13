from flask import Flask, render_template, request, jsonify
import algo.findBestLoc as fbl

# ALGO
class Area:
    def __init__(self,x,y,width,heigth,nama,jenis,floor,gedung):
        self.x = x
        self.y = y
        self.w = width
        self.h = heigth
        self.nama = nama
        self.jenis = jenis
        self.floor = floor
        self.gedung = gedung
class Galon : 
    def __init__(self,x,y,width,heigth,nama,jenis,floor,gedung,kondisi) -> None:
        self.x = x
        self.y = y
        self.w = width
        self.h = heigth
        self.nama = nama
        self.jenis = jenis
        self.floor = floor
        self.gedung = gedung
        self.kondisi = kondisi

areaP1 = [
    # gedung P lt 1 (1637px x 543px)
    #    x  y  w  h        nama jenis(ruangan galon pintu jalan)    floor  gedung
    Area(0,0,24.5,43.46,'KANTIN','ruangan',4,'P1'),
    Area(24.5,0,7.15,21.36,'ATK','ruangan',4,'P1'),
    Area(31.65,0,4,4,'','galon',4,'P1'),

]
areaP2 = [
     # gedung P lt 2 (1637px x 543px)
    #    x  y  w  h        nama jenis(ruangan galon pintu jalan)    floor  gedung
    Area(0,0,9.47,36.46,'P.204','ruangan',4,'P2'),
    Area(9.47,0,13.32,36.46,'LAB SI','ruangan',4,'P2'),   
]

# TODO Buat array areas nya jadi class location 
# Posisi player
x = None
y = None
# END ALGO
# app run script
app = Flask(__name__)

# app routes
@app.route('/')
def index():
    return render_template('index.html',dataAreas=areaP1,lantai='P1')

@app.route('/p2')
def p2() :
    return ''

# menerima posisi player
@app.route('/send_position', methods=['POST'])
def receive_position():
    data = request.json
    x = data['x']
    y = data['y']
    lantai = data['lantai']
    # coding buat nentuin dia di node mana
    print('posisi x',x)
    print('posisi y',y)
    print('lantai', lantai)

    #findBestLocation algo
    user = fbl.User(x,y)
    print(user.x)
    print(user.y)
    loc1 = fbl.Location("1", 70, 100, 35, user)
    loc2 = fbl.Location("2", 80, 5, 20, user)
    print(loc1.calculate_util())
    print(loc2.calculate_util())
    findBest = fbl.Algo()
    findBest.add_loc(loc1)
    findBest.add_loc(loc2)
    print(findBest.choose_loc())

    # Process the position data as needed
    msg = 'Position received successfully' + str(x) + ' y : '+ str(y) + ' lantai '+ lantai  
    response = {'message': msg}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)