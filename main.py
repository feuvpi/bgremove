import os
from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file specified", 400
        file = request.files["file"]
        if file.filename == "":
            return "No file selected", 400
        if file:
            input_image = Image.open(file.stream)
            output_image = remove(
                input_image,
                post_process_mask=True,
                post_process_mask_steps=5,
                alpha_matting=True,
                alpha_matting_foreground_threshold=0.3,  # Increase this value
                alpha_matting_background_threshold=0.1,  # Decrease this value
                strength=0.4,  # Reduce the strength
                format="PNG",
                quality=100,
            )

            img_io = BytesIO()
            output_image.save(img_io, "PNG")
            img_io.seek(0)
            return send_file(
                img_io,
                mimetype="image/png",
                as_attachment=True,
                download_name="nobg.png",
            )
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5100)


def select_image():
    # Prompt user to select an image file
    image_path = input("Please enter the path of the image file: ").strip()

    # Check if the file exists
    if os.path.isfile(image_path):
        remove_background(image_path)
    else:
        print("Invalid file path. Please make sure the file exists.")


def remove_background(image_path):
    output = remove(image_path)
    output.save("out.png")


# if __name__ == "__main__":
#     select_image()
