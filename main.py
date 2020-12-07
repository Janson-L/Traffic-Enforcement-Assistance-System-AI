from flask import Flask, request, jsonify
import base64
app = Flask(__name__)

def base64ToImg(base64Img):
    img=base64.b64decode(base64Img)
    print("Finised base64 Conversion")
    return img

@app.route("/", methods=["POST"])
def CarPlateRecognition():
    img = base64ToImg(request.json['img'])
    return "hello \n"

if __name__ == "__main__":
    app.run(debug = True)