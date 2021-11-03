#Importing the liabraries
import pickle
from flask import Flask, render_template, request

#Global varibles
app = Flask(__name__)
loadedModel = pickle.load(open('KNN Model.pkl', 'rb'))

#Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    alcohol = request.form['alcohol']
    sulphates = request.form['sulphates']
    citric_acid = request.form['citric_acid']
    volatile_acidity = request.form['volatile_acidity']

    prediction = str(loadedModel.predict([[alcohol, sulphates, citric_acid, volatile_acidity]])[0])

    return render_template('index.html', api_output= prediction + " / 10")


#Main function
if __name__ == '__main__':
    app.run(debug=True)