import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/result',methods=['POST'])
def result():
    '''
    For rendering results on HTML GUI
    
    '''
    df = pd.read_csv("frequent.csv")
    features = request.form.get('FrequentPurchases')
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)
    output = df[df.antecedents == features]["consequents"][:1]
    s = output.to_string(index = False)
    return render_template('form.html', prediction_text=s)
    #return render_template('form.html', prediction_text=features)


if __name__ == "__main__":
    app.run(debug=True)
    
    

