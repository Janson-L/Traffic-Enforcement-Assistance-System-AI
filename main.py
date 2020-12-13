from flask import Flask, request, jsonify
import base64
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from modelloader import LPR

import json

app = Flask(__name__)

def base64ToImg(base64Img):
    # img=base64.b64decode(base64Img)
    # print("Finised base64 Conversion")
    # return img
    with open("tempImage.jpg", "wb") as fh:
        fh.write(base64.b64decode(base64Img))

@app.route("/", methods=["POST"])
def CarPlateRecognition():
    base64ToImg(request.json['img'])
    licensePlateJson=LPR.plateNoRecognition()
    os.remove("tempImage.jpg")
    
    return licensePlateJson

if __name__ == "__main__":
    app.run(debug = True)
    #app.run(debug = True,host="0.0.0.0",port=5000) Production use this