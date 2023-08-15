# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-07-24 04:47:04
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-08-15 16:37:25

import os
import sys
import time
from flask import (
    Flask,
    request,
    render_template,
    send_from_directory,
    redirect,
    url_for,
)

# adds the root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from src.searchHollis import searchHollis


app = Flask(__name__)

INTERFACE_FOLDER = os.path.join(os.path.dirname(__file__), "interface")
app.template_folder = os.path.join(INTERFACE_FOLDER, "templates")
app.static_folder = os.path.join(INTERFACE_FOLDER, "static")
UPLOAD_FOLDER = os.path.join(INTERFACE_FOLDER, "uploads")
DOWNLOAD_FOLDER = os.path.join(INTERFACE_FOLDER, "downloads")

COLUMN_INDICES = {
    "ISBN": "A",
    "TITLE": "B",
    "AUTHOR": "C",
    "PUBLISHER": "D",
    "PUB_YEAR": "E",
}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)


def run_search_hollis(
    input_file_path, output_file_path, BOOK_COUNT, column_indices
) -> str:
    result = searchHollis(
        input_file_path,
        output_file_path,
        BOOK_COUNT,
        column_indices=app.config["COLUMN_INDICES"],
    )
    return result


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part in the request"
        # checks if user submitted an empty file
        file = request.files["file"]
        if file.filename == "":
            return "No file selected"

        # get user entered column indices
        app.config["COLUMN_INDICES"] = {
            "ISBN": request.form.get("isbn_index"),
            "TITLE": request.form.get("title_index"),
            "AUTHOR": request.form.get("author_index"),
            "PUBLISHER": request.form.get("publisher_index"),
            "PUB_YEAR": request.form.get("publish_year_index"),
        }

        # clears files within the download and upload folders to free space
        clear_folder(app.config["DOWNLOAD_FOLDER"])
        clear_folder(app.config["UPLOAD_FOLDER"])
        # reset BOOK_COUNT
        app.config["BOOK_COUNT"] = 0

        # config input file name and path
        INPUT_FILENAME = file.filename
        INPUT_FILE_PATH = os.path.join(app.config["UPLOAD_FOLDER"], INPUT_FILENAME)
        # save input file
        file.save(INPUT_FILE_PATH)

        # config output file name and path
        OUTPUT_FILENAME = f"{os.path.splitext(INPUT_FILENAME)[0]}_processed.csv"
        OUTPUT_FILE_PATH = os.path.join(app.config["DOWNLOAD_FOLDER"], OUTPUT_FILENAME)

        return render_template(
            "processing.html",
            INPUT_FILENAME=INPUT_FILENAME,
            OUTPUT_FILENAME=OUTPUT_FILENAME,
            BOOK_COUNT=app.config["BOOK_COUNT"],
        )

    # if the method is GET, render the upload form
    return render_template("upload.html")


@app.route(
    "/processing/<INPUT_FILENAME>/<OUTPUT_FILENAME>/<BOOK_COUNT>",
    methods=["GET", "POST"],
)
def processing(INPUT_FILENAME, OUTPUT_FILENAME, BOOK_COUNT):
    print(f"LOGGER: in processing route")
    print("book count before=", app.config["BOOK_COUNT"])

    INPUT_FILE_PATH = os.path.join(app.config["UPLOAD_FOLDER"], INPUT_FILENAME)
    OUTPUT_FILE_PATH = os.path.join(app.config["DOWNLOAD_FOLDER"], OUTPUT_FILENAME)

    print("FML", INPUT_FILE_PATH, OUTPUT_FILE_PATH)

    # run backend code
    result = run_search_hollis(
        INPUT_FILE_PATH,
        OUTPUT_FILE_PATH,
        app.config["BOOK_COUNT"],
        app.config["COLUMN_INDICES"],
    )
    print("RESULT", result)
    app.config["BOOK_COUNT"] = result[1]
    print("book count after=", app.config["BOOK_COUNT"])

    return result[0]


@app.route("/download_page/<OUTPUT_FILENAME>")
def download_page(OUTPUT_FILENAME):
    print(f"LOGGER: in download_page route")
    return render_template("download.html", OUTPUT_FILENAME=OUTPUT_FILENAME)


@app.route("/download/<OUTPUT_FILENAME>")
def download_file(OUTPUT_FILENAME):
    print(f"LOGGER: in download_file route")
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], OUTPUT_FILENAME)


@app.route("/killtime")
def killTime():
    print(f"Killing time for LibraryCloud Limit")
    return "home"


if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    app.run(debug=True)
