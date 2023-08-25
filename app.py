from flask import Flask, request, render_template
from flask_cors import CORS
import pickle
import base64
from PIL import Image
from io import BytesIO
import numpy as np

model = pickle.load(open('model\model2.pkl','rb'))

app=Flask(__name__)
CORS(app)

@app.route('/')
def home():
     return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
     output = request.get_json()
     decoded_data=base64.b64decode((output[22:]))
     img = Image.open(BytesIO(decoded_data))
     data =  np.asarray(img)
     im = Image.fromarray(data[:,:,3])
     im = im.resize((28,28))
     X_data = np.asarray(im)
     X_data = X_data/255
     X_data = X_data.reshape((-1,784))
     prediction = model.predict(X_data)
     return str(prediction[0])
