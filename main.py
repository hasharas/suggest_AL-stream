import pickle
import numpy as np

from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        Maths = request.form['Maths']
        Science = request.form['Science']
        English = request.form['English']
        Sinhalese = request.form['Sinhalese']
        History = request.form['History']
        Religion = request.form['Religion']
        groupI = request.form['groupI']
        groupII = request.form['groupII']
        groupIII = request.form['groupIII']
        Gender = request.form['Gender']
        data = [[Maths,Science,English,Sinhalese,History,Religion,groupI,groupII,groupIII,Gender]]
        # pred_data = np.array(data, dtype=int)
        # print(pred_data)

        with open('./model/decision_tree_Stream.pkl', 'rb') as file:
            model = pickle.load(file)

        prediction = model.predict(data)
        result = prediction[0]
        return render_template('index.html', result=result)


@app.route('/index')
def redirect_index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
