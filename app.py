from flask import Flask, render_template, request, jsonify
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
    # Process the position data as needed
    msg = 'Position received successfully' + str(x) + ' y : '+ str(y) + ' lantai '+ lantai  
    response = {'message': msg}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)