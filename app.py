from __future__ import division,print_function
import sys
import os
import glob
import re
import numpy as np
from PIL import Image as pil_image       # for operations on images


#KERAS

import keras
print(keras.__version__)

import tensorflow
print(tensorflow.__version__)
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import Model,load_model
from keras.preprocessing import image


#flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

from tensorflow.keras.metrics import categorical_accuracy, top_k_categorical_accuracy

def top_2_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=2)


lesion_classes_dict ={
    0: 'Melanocytic nevi',
    1: 'Melanoma-Cancerous',
    2: 'Benign keratosis-like lesions',
    3: 'Basal cell carcinoma-Cancerous',
    4: 'Actinic keratoses',
    5: 'Vascular lesions',
    6: 'Dermatofibroma'
}

def model_predict(img_path, Model):
    img = image.load_img(img_path, target_size=(224, 224))
    #img = np.asarray(pil_image.open('img').resize((120,90)))
    #x=np.asarray(img.tolist())
    x=image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    # Be careful how your tarined model deals with the input
    # otherwise, it won't make correct prediction!
    
    # x=preprocess_input(x,mode='caffe')
    preds=Model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    #Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, Model)

        # Process your result for human readable
        pred_class = preds.argmax(axis=-1)
        #pred_class = decode_predictions(preds, top=1)
        pr = lesion_classes_dict[pred_class[0]]
        result = str(pr)
        return result 
    return None

if __name__ == '__main__':
    app.run(debug=True)
