from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Define the folder where the model is stored
# folder_name = "Models"
# path =os.path.join(os.getcwd(),folder_name)

with(open('DT_Dating_score.pkl',"rb")) as model_file:
    model = pickle.load(model_file)




@app.route("/")
def greet1():
    return "Welcome MR X"

@app.route("/predict",methods = ["GET"])
def predict_note_authentication():
    """
    ["Gender","PurchasedVIP","Income","Children","Age","Attractiveness"]
    """
    input_cols = ["Gender","PurchasedVIP","Income","Children","Age","Attractiveness"]

    list1 = [float(request.form[i]) for i in input_cols]
    for i in input_cols:
        val = request.args.get(i)
        list1.append(eval(val))

    prediction = model.predict([list1])
    print(prediction)
    return "Hello The answer is"+str(abs((prediction)))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
