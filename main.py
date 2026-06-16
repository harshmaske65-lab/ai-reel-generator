from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "user_uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():

    myid = uuid.uuid1()

    if request.method == "POST":

        rec_id = request.form.get("uuid")
        desc = request.form.get("text")

        print("UUID:", rec_id)
        print("Description:", desc)

        folder_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            rec_id
        )

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Save description once
        with open(
            os.path.join(folder_path, "desc.txt"),
            "w",
            encoding="utf-8"
        ) as f:
            f.write(desc)

        # Save uploaded files
        for key, file in request.files.items():

            if file:

                filename = secure_filename(file.filename)

                file.save(
                    os.path.join(folder_path, filename)
                )

                print("Saved:", filename)

    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


app.run(debug=True)