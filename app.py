from flask import Flask, render_template, request, jsonify
import algo.map as map

# Peta Utama
themap = map.Map()
themap.createLantai('plantai1')
themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
themap.createRuangan('plantai1',(0,9),2,3,'ATK')
themap.createGalon('plantai1','plantai11',90,17,2)
themap.createGalon('plantai1','plantai12',80,27,7)
themap.printLantai('plantai1')

# END ALGO
# app run script
app = Flask(__name__)

# app routes
@app.route('/')
def index():
    return render_template('index.html',data=[],lantai='P1')

@app.route('/p2')
def p2() :
    return render_template('index.html',data=[],lantai='P2')

# menerima posisi player
@app.route('/send_position', methods=['POST'])
def receive_position():
    # ngambil x,y dan lantai dari web
    data = request.json
    x = data['x']
    y = data['y']
    lantai = data['lantai']
    themap.setUserLoc(x,y)

    # lokasi web dari user
    print('posisi x',x)
    print('posisi y',y)
    print('lantai', lantai)

    #findBestLocation algo
    bestLoc = themap.findBestLoc()
    print(bestLoc)

    # Process the position data as needed
    msg = 'Position received successfully' + str(x) + ' y : '+ str(y) + ' lantai '+ lantai  
    response = {'message': msg, 'bestLoc' : bestLoc}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)