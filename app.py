from flask import Flask, render_template, request, jsonify

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

areas = [
    # gedung P lt 1 (1637px x 543px)
    #    x  y  w  h        nama jenis(ruangan galon pintu jalan)    floor  gedung
    Area(0,0,24.5,43.46,'KANTIN','ruangan',4,'P1'),
    Area(24.5,0,7.15,21.36,'ATK','ruangan',4,'P1'),

    # gedung P lt 2 (1637px x 543px)
    #    x  y  w  h        nama jenis(ruangan galon pintu jalan)    floor  gedung
    Area(0,0,9.47,36.46,'P.204','ruangan',4,'P2'),
    Area(9.47,0,13.32,36.46,'LAB SI','ruangan',4,'P2'),
    
]
# Posisi player
x = None
y = None

# app run script
app = Flask(__name__)

# Tempat"nya 


@app.route('/')
def index():
    return render_template('index.html',dataAreas=areas)

@app.route('/p2')
def p2() :
    return ''

@app.route('/send_position', methods=['POST'])
def receive_position():
    data = request.json
    x = data['x']
    y = data['y']
    
    # Process the position data as needed
    response = {'message': 'Position received successfully'}
    # coding buat nentuin dia di node mana
    print('posisi x',x)
    print('posisi y',y)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)