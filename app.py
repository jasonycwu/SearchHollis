# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-07-24 04:47:04
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-08-13 10:43:52

import os
import sys
from flask import Flask, request, render_template, send_from_directory
from flaskwebgui import FlaskUI

# adds the root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from src.searchHollis import searchHollis


app = Flask(__name__)
# ui = FlaskUI(app=app, server="flask", width=800, height=500)

INTERFACE_FOLDER = os.path.join(os.path.dirname(__file__), "interface")
app.template_folder = os.path.join(INTERFACE_FOLDER, "templates")
app.static_folder = os.path.join(INTERFACE_FOLDER, "static")
UPLOAD_FOLDER = os.path.join(INTERFACE_FOLDER, "uploads")
DOWNLOAD_FOLDER = os.path.join(INTERFACE_FOLDER, "downloads")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)


def run_search_hollis(input_file_path, output_file_path, column_indices=None):
    searchHollis(input_file_path, output_file_path, column_indices=column_indices)
    return os.path.basename(output_file_path)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part in the request"

        file = request.files["file"]

        # checks if user submitted an empty file
        if file.filename == "":
            return "No file selected"

        column_indices = {
            "ISBN": request.form.get("isbn_index"),
            "TITLE": request.form.get("title_index"),
            "AUTHOR": request.form.get("author_index"),
            "PUBLISHER": request.form.get("publisher_index"),
            "PUB_YEAR": request.form.get("publish_year_index"),
        }

        # clears files within the download and upload folders to free space
        clear_folder(app.config["DOWNLOAD_FOLDER"])
        clear_folder(app.config["UPLOAD_FOLDER"])

        # save the uploaded file to the UPLOAD_FOLDER directory
        uploaded_file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(uploaded_file_path)

        # create the path for the output file in the DOWNLOAD_FOLDER
        output_file_path = os.path.join(
            app.config["DOWNLOAD_FOLDER"],
            f"{os.path.splitext(file.filename)[0]}_processed.csv",
        )

        # run backend code
        run_search_hollis(
            os.path.join(app.config["UPLOAD_FOLDER"], file.filename),
            output_file_path,
            column_indices,
        )

        processed_filename = os.path.basename(output_file_path)
        return render_template("download.html", processed_filename=processed_filename)

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
    # ui.run()
