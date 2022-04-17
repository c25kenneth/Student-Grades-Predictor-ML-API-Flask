
from flask import Flask, request, make_response
import pickle
import pandas as pd

data = pd.read_csv('student-mat.csv', sep=';')
data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

pickle_in = open('model.pickle', 'rb')
linear = pickle.load(pickle_in)

app = Flask(__name__)

@app.route('/api/predict/<G1>/<G2>/<studytime>/<failures>/<absences>', methods=['PUT'])
def predict(G1, G2, studytime, failures, absences):
    if request.method == 'PUT':
        pred = linear.predict([ [G1, G2, studytime, failures, absences] ])
        return str(pred)

@app.route('/api/intro', methods=['GET'])
def getIntro():
    return 'Welcome to the API! This API uses Machine Learning to predict the 3rd grade of a student based on their first 2 grades, their studytime, failures, and absences. Enter that into to restpoint /api/predict. You can also make a get request to api/getData to get the first few rows of the dataset!'

@app.route('/api/getData/', methods=['GET'])
def getData():
    if request.method == 'GET':
        return str(data.head())

if __name__ == '__main__':
    app.run(debug=True)