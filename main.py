from flask import Flask, render_template,request
import uuid

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
#create page
@app.route("/create",methods=["GET","Post"])
def create():
    if request.method == "POST":
        print("FORM:", request.form)
        print("FILES:", request.files)
        print("FILE1:", request.files.get("file1"))
    
    return render_template("create.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)