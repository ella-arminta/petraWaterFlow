from flask import Flask, render_template, request, jsonify

class Area:
    def __init__(self,x,y,width,heigth,jenis,color,floor,gedung):
        self.x = x
        self.y = y
        self.w = width
        self.h = heigth
        self.jenis = jenis
        self.color = color
        self.floor = floor
        self.gedung = gedung

areas = [
    Area(20,30,10,30,'jalan','red',4,'P'),
    Area(40,30,10,30,'jalan','blue',4,'P'),
    Area(50,30,10,30,'galon','yellow',4,'P'),
    Area(50,30,10,30,'Gedung P','yellow',4,'P'),
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