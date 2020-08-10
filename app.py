"""
Created on Fri Aug  7 01:23:37 2020

@author: Rohit Mehta
"""

from flask import Flask,render_template,url_for,request
import pickle

def word_divide_char(inputs):
    characters=[]
    for i in inputs:
        characters.append(i)
    return characters
    
loaded_model=pickle.load(open('Xgboost Algorithm.pkl', 'rb'))

vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])

def predict():
    
    
    int_features = [str(x) for x in request.form.values()]
  
    final_features=vectorizer.transform(int_features)
    
    my_prediction = loaded_model.predict(final_features)
    
    if my_prediction == 0:
        output = 'Weak Strength Password'
    elif my_prediction == 1:
        output = 'Medium Strength Password'
    else:
        output = 'Strong Strength Password'
        

    return render_template('home.html', prediction_text=format(output))
    


if __name__ == '__main__':
    
    app.run(debug=True)
