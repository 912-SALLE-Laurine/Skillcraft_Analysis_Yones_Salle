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
    output1 = round(prediction1[0], 2)
    output2 = round(prediction2[0], 2)
    league = "bronze"

    return render_template('index.html', 
                           prediction_text= f'Prediction of the league index (40% of accuracy) : Index : {output1}, League : {league}',
                           prediction_2 = f'Prediction of the Level of the player :  The player is level {output2}')

if __name__ == '__main__':
    model1 = pickle.load(open("model1.pickle", "rb"))
    model2 = pickle.load(open("model2.pickle", "rb"))
    app.run(debug=True)