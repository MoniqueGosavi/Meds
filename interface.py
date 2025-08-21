#from flask import Flask, jsonify, render_template, request, redirect
#import config
#from utils import Diabetes

#app = Flask(__name__)
#@app.route('/')
#def man():
    #return render_template('home.html')


#@app.route('/predict',methods = ['GET', "POST"])

#def home():
   # if request.method == 'POST':
     #   data = request.form
        
     #   print('data :',data)

     #   med_dbs = Diabetes(data)
      #  pred_class = med_dbs.get_predicted_outcome()
      #  print("::::::::::",pred_class)
      #  print(int(pred_class))
       # return render_template('after.html', data=pred_class)
        # if pred_class == 1:
        #     return jsonify({"Outcome": "Person has Diabetes"})

        # else:
        #     return jsonify({"Outcome": "Person has no Diabetes"})
       # return f"{pred_class}"
        #return jsonify({"class" :0 })



#if __name__ == "__main__":
   # app.run(host='0.0.0.0', port=5004)

# code for streamlit
import streamlit as st
from utils import Diabetes
import numpy as np

st.set_page_config(page_title="Diabetes Risk Predictor", layout="wide")

st.title("🩺 Diabetes Risk Prediction App")
st.write("Enter your health metrics below to predict diabetes risk:")

# Create columns for a cleaner layout
col1, col2, col3 = st.columns(3)

with col1:
    Glucose = st.number_input("Glucose", min_value=0, max_value=300, value=100)
    BloodPressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
    SkinThickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)

with col2:
    Insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)
    BMI = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, format="%.2f")

with col3:
    Age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Pack all inputs into a dictionary
user_data = {
    "Glucose": Glucose,
    "BloodPressure": BloodPressure,
    "SkinThickness": SkinThickness,
    "Insulin": Insulin,
    "BMI": BMI,
    "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
    "Age": Age
}

# Predict button
if st.button("Predict Risk"):
    try:
        dbs = Diabetes(user_data)
        result = dbs.get_predicted_outcome()
        if result == 1:
            st.error("⚠️ The model predicts a HIGH risk of diabetes.")
        else:
            st.success("✅ The model predicts a LOW risk of diabetes.")
    except Exception as e:
        st.error(f"Error: {e}")
