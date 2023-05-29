from flask import Flask, render_template

class Area:
    def __init__(self,x,y,width,heigth,color,floor):
        self.x = x
        self.y = y
        self.w = width
        self.h = heigth
        self.color = color
        self.floor = floor

        
class Gedung: 
    def __init__(self, nama, areas):
        self.nama = nama
      

# app run script
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


