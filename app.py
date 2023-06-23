from flask import Flask, render_template, request, jsonify, session
import algo.mapping as mapping
import pprint

# Peta Besar
themap = mapping.Map()
#Jalan ke galon dalam bentuk koordinat [0,2],[0,3]
# themap.add_edge_petaUkp('plantai1','plantai2',5)
# themap.add_edge_petaUkp('wlantai1','plantai1',10)

# Peta per lantai
# P lantai 1
themap.createLantai('plantai1','P')
# bagian kiri
themap.createRuangan('plantai1',(0,0),7,5,'KANTIN')
themap.createRuangan('plantai1',(8,0),2,3,'ATK')
themap.createRuangan('plantai1',(0,8),10,2,'KURSI')
# bagian tengah
themap.createRuangan('plantai1',(11,0),6,1,'TOILET')
themap.createRuangan('plantai1',(12,1),4,1,'LIFT')
themap.createRuangan('plantai1',(11,8),6,2,'TANGGA')
themap.createRuangan('plantai1',(17,3),1,2,'MEJA')
themap.createRuangan('plantai1',(16,6),2,1,'MEJA')
# bagian kanan
themap.createRuangan('plantai1',(18,0),6,5,'LAB FISIKA')
themap.createRuangan('plantai1',(24,1),1,4,'LIFT')
themap.createRuangan('plantai1',(19,6),2,1,'MEJA')
themap.createRuangan('plantai1',(22,6),2,1,'MEJA')
themap.createRuangan('plantai1',(25,6),2,1,'MEJA')
themap.createRuangan('plantai1',(28,6),2,1,'MEJA')
themap.createRuangan('plantai1',(18,8),7,2,'KURSI')
themap.createRuangan('plantai1',(26,9),1,1,'Tangga') # tangga
themap.createRuangan('plantai1',(28,8),7,2,'LAB T. INDUSTRI')
themap.createRuangan('plantai1',(35,8),2,2,'UPPK')
themap.createRuangan('plantai1',(37,8),2,2,'KONSELING')
themap.createRuangan('plantai1',(26,0),9,2,'LAB T. INDUSTRI')
themap.createRuangan('plantai1',(36,0),3,2,'TOILET')
themap.createRuangan('plantai1',(35,3),2,1,'MEJA')
# galon p lt 1
themap.createGalon('plantai1','plantai11',90,17,2)
themap.createGalon('plantai1','plantai12',80,27,7)
themap.printLantai('plantai1')

# P lantai 2
themap.createLantai('plantai2','P')
# bagian kiri
themap.createRuangan('plantai2',(0,0),3,4,'P.204')
themap.createRuangan('plantai2',(3,0),4,4,'LAB SI')
themap.createRuangan('plantai2',(7,0),3,4,'LAB PG')
themap.createRuangan('plantai2',(0,6),3,4,'P.203')
themap.createRuangan('plantai2',(3,6),3,4,'P.202')
themap.createRuangan('plantai2',(6,6),2,4,'LAB STUDIO')
themap.createRuangan('plantai2',(8,6),2,4,'LAB MOBDEV')
# bagian tengah
themap.createRuangan('plantai2',(10,4),1,1,'') # tiang
themap.createRuangan('plantai2',(12,4),1,1,'') # tiang
themap.createRuangan('plantai2',(13,3),2,3,'MEJA')
themap.createRuangan('plantai2',(15,4),1,1,'') # tiang
themap.createRuangan('plantai2',(16,3),1,3,'MEJA')
themap.createRuangan('plantai2',(17,4),1,2,'LOKER')
themap.createRuangan('plantai2',(11,0),6,1,'TOILET')
themap.createRuangan('plantai2',(12,1),4,1,'LIFT')
themap.createRuangan('plantai2',(11,8),6,2,'TANGGA')
themap.createRuangan('plantai2',(10,9),1,1,'') # sambungan kiri tangga
themap.createRuangan('plantai2',(17,9),1,1,'') # sambungan kanan tangga
# bagian kanan
themap.createRuangan('plantai2',(18,0),5,2,'LAB JK')
themap.createRuangan('plantai2',(23,0),5,2,'LAB SC')
themap.createRuangan('plantai2',(18,8),7,2,'LAB MM')
themap.createRuangan('plantai2',(28,0),11,8,'PUSKOM P')
themap.createRuangan('plantai2',(27,8),12,2,'LAB PRODI T. MESIN')
themap.createRuangan('plantai2',(26,9),1,1,'') # tangga
themap.createRuangan('plantai2',(23,4),2,2,'LIFT')
themap.createRuangan('plantai2',(26,4),1,2,'MEJA')
# galon p lt 2
themap.createGalon('plantai2','plantai21',50,9,4)
themap.createGalon('plantai2','plantai22',75,27,7)

# P lantai 2
themap.createLantai('wlantai1','W')
themap.printAllLantai()

print(themap.daftarRuangan[1])

# app run script
app = Flask(__name__)
app.secret_key = 'secretKery'
# hapus session
# @app.before_request
# def clear_session():
#     if not request.path.startswith('/static'):
#         session.pop('hasilPath', None)

# app routes
@app.route('/')
def index():
    if 'hasilPath' in session:
        hasilPath = session['hasilPath']
    else:
        session['hasilPath'] = []
        hasilPath = session['hasilPath']
    print('session ',session['hasilPath'])
    return render_template(
        'index.html',
        ruangans=themap.daftarRuangan,
        peta=themap.lantai,
        lantai='plantai1',
        hasilPath=hasilPath,
    )

@app.route('/p2')
def p2() :
    if 'hasilPath' in session:
        hasilPath = session['hasilPath']
    else:
        session['hasilPath'] = []
        hasilPath = session['hasilPath']
    print('session ',session['hasilPath'])

    return render_template('index.html',ruangans=themap.daftarRuangan,peta=themap.lantai,lantai='plantai2',hasilPath=hasilPath)

# menerima posisi player
@app.route('/send_position', methods=['POST'])
def receive_position():
    print("______ SEND POSITION ____ FIND BEST LOC")
    # ngambil x,y dan lantai dari web
    data = request.json
    x = data['x']
    y = data['y']
    lantai = data['lantai']
    themap.setUserLoc(x,y,lantai)

    # lokasi user dari web
    print('posisi x',x)
    print('posisi y',y)
    print('lantai', lantai)

    #findBestLocation algo
    bestLoc = themap.findBestLoc()
    print("user", themap.user.x, themap.user.y)
    
    dataHasil = themap.constructAPath() #waktu convert path data aslinya keubah yg di themap.lantai error
    print('Data hasil',dataHasil)
    hasilPath = dataHasil[2]
    print('hasilPath', hasilPath)
    hasilPath = themap.convertPathToWeb(hasilPath)
    for i in hasilPath:
        print('gedung ',i['gedung'])
        print('lantai ',i['lantai'])
        print('x ',i['x'])
        print('y ',i['y'])

    
    if 'hasilPath' in session:
        session['hasilPath'] = hasilPath
    else:
        session['hasilPath'] = []
        session['hasilPath'] = hasilPath

    print('session ',session['hasilPath'])

    # Process the position data as needed
    msg = 'Position received successfully' + str(x) + ' y : '+ str(y) + ' lantai '+ lantai  
    response = {'message': msg, 'bestLoc' : bestLoc, 'hasilPath' : session['hasilPath']}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)