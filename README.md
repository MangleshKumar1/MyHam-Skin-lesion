# My HAM10000 Skin-cancer-lesion analyser
Skin-cancer-lesion-analyzer


<br>

![WEB UI](https://github.com/MangleshKumar1/MyHam-Skin-lesionHAM10000-Skin-cancer-lesion-analyser/assets/97977847/65f35530-01c5-4eb8-8bf5-fe26642ad616)

<br>

This is a prototype can tell patients, doctors and lab technologists the two highest probability diagnoses for a given skin lesion. It could help them quickly identify high risk patients and speed up their workflow. The app will produce a result in less than 3 seconds. To ensure privacy, user submitted images are pre-processed and analyzed locally and are never uploaded to an external server. 

This app is powered by Artifical Intelligence. My goal for this project was to build an end to end solution - starting with model creation and ending with a live web app. Users are able to submit a picture of a skin lesion and get an instant prediction. 

The app is able to classify 7 types of skin lesions as described in this paper:<br>



The HAM10000 Dataset: A Large Collection of Multi-Source Dermatoscopic Images of Common Pigmented Skin Lesions<br>
https://arxiv.org/abs/1803.10417


The entire model building and training process is described in this Kaggle kernel:<br>
https://www.kaggle.com/code/mangleshkumar/myham1000-skin-lesion-cancer-analyser

The python code to build and train the model is included in the Jupyter notebook. All the javascript, css and html files are also freely available here. The trained model is also available.


<hr>

<br>
**app.py**<br>
This code is a Flask web application that serves a machine learning model for predicting skin lesion types from uploaded images. Here's a breakdown of how it works:<br>

Imports and Initialization: The necessary libraries for image processing, machine learning, and web serving are imported. The Flask application is initialized, and CORS (Cross-Origin Resource Sharing) is enabled to allow requests from any origin.<br><br>

Model Loading: The pre-trained machine learning model (model.h5) is loaded into memory.<br><br>

Lesion Classes Dictionary: A dictionary mapping the predicted class indices to human-readable lesion descriptions is defined.<br><br>

Model Prediction Function: The model_predict function processes an input image to the required format (224x224 pixels), preprocesses it using MobileNet V2 preprocessing, and predicts the class probabilities using the loaded model.<br><br>

Home Route (/): Renders the main HTML page (index.html) when accessed via a GET request.<br><br>

Prediction Route (/predict): Handles file uploads via POST requests. The uploaded file is saved, and the model_predict function is called to generate predictions. The top two predictions with their probabilities are extracted and returned as a JSON response.<br><br>

Running the App: The application is set to run in debug mode when the script is executed directly.<br><br>

In summary, this application allows users to upload images of skin lesions and receive predictions on the lesion types along with their probabilities, leveraging a pre-trained deep learning model.



All the requirements is given in requirements in requirements.txt file to run the code locally in pc. We need to setup the python in VS code.
