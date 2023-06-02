# from flask import Flask,jsonify

# app = Flask(__name__)

# @app.route("/")
# def index():
# 	return jsonify({"msg":"hello deploy from glitch"})

# if __name__ == "__main__":
# 	app.run()

from flask import Flask

from flask import request

import firebase_admin
from firebase_admin import credentials, storage

# import time
import json
import numpy as np
import cv2
import face_recognition


cred = credentials.Certificate("./key.json")
app = firebase_admin.initialize_app(cred, {"storageBucket": "fir-storageproject-959b2.appspot.com"})
# db = firestore.client()
# print(blob1.name.split("/"))
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def students():
    data = {}
    img = str(request.args.get("student"))
    bucket = storage.bucket()
    blob1 = list(bucket.list_blobs(prefix="students/"+"img18.jpg"))[0]
    print(blob1)
    arr = np.frombuffer(blob1.download_as_string(), np.uint8)  # array of bytes
    img = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555) # actual image
    print(img)
    test = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(test)[0]
    print(encodings)

    # blob1 = list(bucket.list_blobs())[1]
    # print(blob1.name.split("/"))

    # arr = np.frombuffer(blob1.download_as_string(), np.uint8)  # array of bytes
    # img = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555) # actual image
    # print(img)
    # bucket = storage.bucket()
    # students = list(bucket.list_blobs(prefix="students/"))
    # print(students)
    # count = 1
    # data = {}
    # for std in students:
    #     if (len(std.name.split("/")[-1]) == 0):
    #         continue
    #     data["name"+str(count)] = std.name.split("/")[-1]
    #     count+=1
    data['name1']=img
    data['encodings']=encodings
    json_dump = json.dumps(data)
    return json_dump
print(True)


