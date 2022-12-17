from flask import Flask, jsonify, render_template, request, redirect
import config
from utils import Diabetes

app = Flask(__name__)
@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict',methods = ['GET', "POST"])

def home():
    if request.method == 'POST':
        data = request.form
        
        print('data :',data)

        med_dbs = Diabetes(data)
        pred_class = med_dbs.get_predicted_outcome()
        print("::::::::::",pred_class)
        print(int(pred_class))
        return render_template('after.html', data=pred_class)
        # if pred_class == 1:
        #     return jsonify({"Outcome": "Person has Diabetes"})

        # else:
        #     return jsonify({"Outcome": "Person has no Diabetes"})
       # return f"{pred_class}"
        #return jsonify({"class" :0 })



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)