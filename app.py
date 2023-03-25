from PIL import Image
from flask import Flask, request
import json
from transformers import pipeline
import os

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin




app = Flask(__name__)
CORS(app, support_credentials=True)

print("\n\nloading classification model")
food_classifier = pipeline("image-classification", model="nateraw/food")
print("classification model loaded\n\n")

print("loading text generation model")
recipe_generator = pipeline("text-generation", model="mbien/recipenlg")
print("text generation model loaded\n\n")


groups = json.load(open(os.getcwd()+os.sep+"groups.json","r"))

@app.route("/infer_image/", methods=["POST"])
@cross_origin(supports_credentials=True)
def infer_image():
    try:
        input_data = request.get_data()
        input_data = json.loads(input_data)
        print(input_data)
        img_path = os.getcwd()+os.sep+"img_data"+os.sep+input_data["file_path"]
        img = Image.open(img_path)
        res = food_classifier(img)
        generated_text = recipe_generator(" ".join(res[0]["label"].title().split("_")))
        if res:
            return json.dumps([{"Confidence":res[0]["score"],"Food Type":" ".join(res[0]["label"].title().split("_")),"Nutritional Value":groups[res[0]["label"]].title(),"Info":generated_text[0]["generated_text"]}])
    except Exception as e:
        print(e)
        return json.dumps([{"error":"something went wrong - "+ str(e)}])
    

if __name__=='__main__':
    app.run(debug=True)