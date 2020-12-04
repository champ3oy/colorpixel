from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
from colorthief import ColorThief


@app.route("/api/v1/pixel/<number>", methods=["POST"])
def hello_name(number):
    try:
        number = int(number)

        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            uploaded_file.save(uploaded_file.filename)

        color_thief = ColorThief(uploaded_file.filename)
        dominant_color = color_thief.get_color(quality=1)

        palette = color_thief.get_palette(color_count=number if number > 0 else 5)

        response = []

        for pixel in palette:
            response.append({"color": "rgb" + str(pixel)})

        return {"status": "Success", "colors": response}
    except error:
        print(error)
        return {"status": "Failed", "message": "Sorry an error"}


if __name__ == "__main__":
    app.run()