# singularity_hackathon

Food Recognition Model


This is a web app that allows to accept food images and help identify type of food, it's confidence for type identification,
Nutritional category(Green/Yellow/Red) and some info about that food-recipe.


This is written in Python 3.7 version. Create a conda python virtual enevironemnt

--conda create food_recognition
--conda activate food_recognition


and install dependencies in that environment from text file requirements.txt by command.
-- pip install requirements.txt


First of all run the HTTP server in Python by command
--python -m http.server

this command runs the http server by utilizing index.html from root directory of this project. 
the HTTP server will run on localhost and port 8000 by default.


Now, run the backend flask application by command
--python app.py

this will run the POST request backend API at endpoint 'infer_image' on localhost and at port 5000.


Open the app url - http://localhost:8000/ in browser and upload sample image from directory 'img_data'. 
Please make sure the Sample image or test image to be uploaded need to be present in the directory 'img_data'.


See below demo UI image::

<img width="945" alt="sing_hack_demo" src="https://user-images.githubusercontent.com/25390594/227732582-b96af906-e717-40e8-8ed7-c2b8044df826.png">

