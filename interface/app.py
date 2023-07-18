# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-07-18 15:08:12
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-18 16:55:29

from flask import Flask, render_template, request, send_from_directory
import os

UPLOAD_FOLDER = "./uploads"  # path to uploads space
ALLOWED_EXTENSIONS = {"csv"}  # accepted input file extensions


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Homepage
@app.route("/")
def index():
    """
    '/' (aka. Home page):
    This route (index) handles the home page.
    When a user visits the root URL of the application, it automatically
    deletes all files in the UPLOAD_FOLDER to free up space.
    It then renders the index.html template, passing filename=None to the template
    """
    files = os.listdir(app.config["UPLOAD_FOLDER"])

    # TODO: style the homepage (copy Natnael's)
    # TODO: add an upload file mechanism on homepage
    # TODO: build a page for file upload
    # TODO: have the user be able to indicate which index the columns are
    # TODO: once the upload is done, use the file as input (as in backend)
    # TODO: build a mechanism for users to download the output file
    return render_template("index.html")


# File download redirect
@app.route("/downloads/<name>", methods=["GET", "POST"])
def download_file(name):
    """
    '/downloads/<name>':
    This route (download_file) handles the download of CSV files.
    It allows users to download the generated CSV files from the UPLOAD_FOLDER.
    """
    if request.method == "POST" or request.method == "GET":
        return send_from_directory(app.config["UPLOAD_FOLDER"], name)


# runs the webapp
if __name__ == "__main__":
    app.run(debug=True)
