import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction1 = model1.predict(final_features)
    prediction2 = model2.predict(final_features)
    league_index = round(prediction1[0], 2)
    level = round(prediction2[0], 2)
    league_dict = {1:"Bronze", 2:"Silver", 3:"Gold", 4:"Platinum", 5:"Diamond", 6:"Master", 7:"Grandmaster", 8:"Professional"}
    league_name = league_dict[league_index]

    return render_template('index.html', 
                           prediction_text= f"Prediction of the player's League (around 0.40 of accuracy): Index : {league_index}, League : {league_name}",
                           prediction_2 = f"Prediction of the player's Level  (around 0.80 of accuracy):  The player is level {level}")

if __name__ == '__main__':
    model1 = pickle.load(open("model1.pickle", "rb"))
    model2 = pickle.load(open("model2.pickle", "rb"))
    app.run(debug=True)