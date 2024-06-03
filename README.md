# My HAM10000 Skin-cancer-lesion analyser
Skin-cancer-lesion-analyzer


<br>

![WEB UI](https://github.com/MangleshKumar1/MyHam-Skin-lesionHAM10000-Skin-cancer-lesion-analyser/assets/97977847/65f35530-01c5-4eb8-8bf5-fe26642ad616)

<br>

This is a prototype can tell patients, doctors and lab technologists the two highest probability diagnoses for a given skin lesion. It could help them quickly identify high risk patients and speed up their workflow. The app will produce a result in less than 3 seconds. To ensure privacy, user submitted images are pre-processed and analyzed locally and are never uploaded to an external server. 

This app is powered by Artifical Intelligence. My goal for this project was to build an end to end solution - starting with model creation and ending with a live web app. Users are able to submit a picture of a skin lesion and get an instant prediction. 

The app is able to classify 7 types of skin lesions as described in this paper:<br>
**bcc - Basal cell carcinoma** 
It is a prevalent type of  skin cancer originating in the basal 
cells of the epidermis, which rarely spreads but can cause 
significant harm if not addressed.  <br>
**akiec– Actinic and intraepithelial Carcinoma (Bowen’s 
disease)** 
Actinic keratosis results from prolonged exposure to 
sunlight and is more common in individuals over 40 years old. <br>
**bkl- Benign keratosis**
This inclusive category includes seborrheic keratoses, 
which could be viewed as a condensed form of seborrheic 
keratoses, alongside lichen-planus-like keratoses. <br>
**df- Dermatofibroma**   
Dermatofibromas are benign skin growths that can 
develop as a response to minor injury or as an allergic reaction. 
They typically appear as brown lesions with a central area of 
fibrosis visible under dermatoscopy. <br>
**mel - Melanoma**
Melanoma is a type of cancer originating from 
melanocytes and can present in various forms. When detected 
early, it can be treated surgically. <br>
**nv- Melanocytic nevi**  
Melanocytic nevi, also known as moles, are harmless 
developments of melanocytes that may manifest in various 
sizes and configurations. Their appearance can vary 
significantly under dermatoscopic examination. <br>
**vasc- Vascular skin lesion**  
Vascular Skin Lesion. Vascular lesions are caused by 
numerous or enlarged blood vessels beneath the skin, often 
giving the skin a reddish appearance due to the visible vessels. 
These lesions come in various sizes and shapes, including 
broken capillaries and cherry angiomas, and can be treated 
using different technologies.<br>

The HAM10000 Dataset: A Large Collection of Multi-Source Dermatoscopic Images of Common Pigmented Skin Lesions<br>
https://arxiv.org/abs/1803.10417


The entire model building and training process is described in this Kaggle kernel:<br>
https://www.kaggle.com/code/mangleshkumar/myham1000-skin-lesion-cancer-analyser

The python code to build and train the model is included in the Jupyter notebook. All the javascript, css and html files are also freely available here. The trained model is also available.


<hr>
