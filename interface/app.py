# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-07-24 04:47:04
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-27 03:36:17

import os
import sys
import shutil
from flask import Flask, request, render_template, send_from_directory

# adds the root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.searchHollis import searchHollis


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

DOWNLOAD_FOLDER = "downloads"
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)


def run_search_hollis(input_file_path, output_file_path):
    searchHollis(input_file_path, output_file_path)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part in the request"

        file = request.files["file"]

        # checks if user submitted an empty file
        if file.filename == "":
            return "No file selected"

        # clears files within the download and upload folders to free space
        clear_folder(app.config["DOWNLOAD_FOLDER"])
        clear_folder(app.config["UPLOAD_FOLDER"])

        # save the uploaded file to the UPLOAD_FOLDER directory
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

        # create the path for the output file in the DOWNLOAD_FOLDER
        output_file_path = os.path.join(
            app.config["DOWNLOAD_FOLDER"],
            f"{os.path.splitext(file.filename)[0]}_processed.csv",
        )

        run_search_hollis(
            os.path.join(app.config["UPLOAD_FOLDER"], file.filename), output_file_path
        )

        return f"File successfully uplaoded and processed <a href='/download/{os.path.basename(output_file_path)}'>Download processed file</a>."

    # if the method is GET, render the upload form
    return render_template("upload.html")


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], filename)


if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    app.run(debug=True)
