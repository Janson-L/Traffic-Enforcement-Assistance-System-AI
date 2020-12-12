from flask import Flask, request, jsonify
import base64
app = Flask(__name__)

def base64ToImg(base64Img):
    # img=base64.b64decode(base64Img)
    # print("Finised base64 Conversion")
    # return img
    with open("tempImage.png", "wb") as fh:
        fh.write(base64.b64decode(base64Img))

@app.route("/", methods=["POST"])
def CarPlateRecognition():
    base64ToImg(request.json['img'])
    return "Hello! \n"

if __name__ == "__main__":
    app.run(debug = True)