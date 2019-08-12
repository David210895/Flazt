from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "ADOPTA TU PERRO"
    return render_template("index.html",title=title)

if __name__=="__main__":
    app.run(debug=True,port=8000)