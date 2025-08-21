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

# Configure page
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main container styling */
    .main {
        padding: 2rem 1rem;
    }
    
    /* Custom background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Header styling */
    .main-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        color: #6b7280;
        font-weight: 400;
        margin-bottom: 0;
    }
    
    /* Input container */
    .input-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.4rem;
        font-weight: 600;
        color: #374151;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e5e7eb;
    }
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 1rem 3rem;
        font-size: 1.1rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Input styling */
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        transition: border-color 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Result styling */
    .result-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        .main-subtitle {
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="main-header">
    <h1 class="main-title">🩺 Diabetes Risk Predictor</h1>
    <p class="main-subtitle">Advanced AI-powered health assessment tool for diabetes risk evaluation</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
<div class="input-container">
    <div class="section-header">📊 Health Metrics Input</div>
    <p style="color: #6b7280; margin-bottom: 1.5rem;">
        Please enter your health metrics below. Our machine learning model will analyze these parameters 
        to provide a diabetes risk assessment. All values should be based on recent medical tests.
    </p>
</div>
""", unsafe_allow_html=True)

# Input section with better organization
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    # Create tabs for better organization
    tab1, tab2 = st.tabs(["🔬 Laboratory Values", "📏 Physical Measurements"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            Glucose = st.number_input(
                "🍯 Glucose Level (mg/dL)", 
                min_value=0, max_value=300, value=100,
                help="Normal fasting glucose: 70-100 mg/dL"
            )
            BloodPressure = st.number_input(
                "💓 Diastolic Blood Pressure (mmHg)", 
                min_value=0, max_value=200, value=70,
                help="Normal diastolic BP: 60-80 mmHg"
            )
        with col2:
            Insulin = st.number_input(
                "💉 Insulin Level (μU/mL)", 
                min_value=0, max_value=900, value=79,
                help="Normal fasting insulin: 5-25 μU/mL"
            )
            DiabetesPedigreeFunction = st.number_input(
                "🧬 Diabetes Pedigree Function", 
                min_value=0.0, max_value=3.0, value=0.5, format="%.2f",
                help="Genetic diabetes likelihood based on family history"
            )
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            SkinThickness = st.number_input(
                "📏 Triceps Skin Fold (mm)", 
                min_value=0, max_value=100, value=20,
                help="Normal range: 10-40 mm"
            )
            BMI = st.number_input(
                "⚖️ Body Mass Index (BMI)", 
                min_value=0.0, max_value=70.0, value=25.0, format="%.1f",
                help="Normal BMI: 18.5-24.9"
            )
        with col2:
            Age = st.number_input(
                "🎂 Age (years)", 
                min_value=1, max_value=120, value=30,
                help="Enter your current age"
            )
    
    st.markdown('</div>', unsafe_allow_html=True)

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

# BMI Category Display
bmi_category = ""
if BMI < 18.5:
    bmi_category = "Underweight"
    bmi_color = "#3b82f6"
elif BMI < 25:
    bmi_category = "Normal weight"
    bmi_color = "#10b981"
elif BMI < 30:
    bmi_category = "Overweight"
    bmi_color = "#f59e0b"
else:
    bmi_category = "Obese"
    bmi_color = "#ef4444"

st.markdown(f"""
<div class="input-container">
    <div style="text-align: center;">
        <p style="color: #6b7280; margin-bottom: 0.5rem;">Your BMI Category:</p>
        <p style="color: {bmi_color}; font-weight: 600; font-size: 1.1rem;">{bmi_category}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Prediction section
st.markdown("""
<div class="input-container">
    <div class="section-header">🔮 Risk Assessment</div>
</div>
""", unsafe_allow_html=True)

# Center the predict button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_clicked = st.button("🔍 Analyze Diabetes Risk", use_container_width=True)

# Results section
if predict_clicked:
    try:
        with st.spinner("🔄 Analyzing your health data..."):
            dbs = Diabetes(user_data)
            result = dbs.get_predicted_outcome()
        
        if result == 1:
            st.markdown("""
            <div class="result-container">
                <div style="font-size: 4rem; margin-bottom: 1rem;">⚠️</div>
                <h2 style="color: #dc2626; font-weight: 700; margin-bottom: 1rem;">High Diabetes Risk Detected</h2>
                <p style="color: #374151; font-size: 1.1rem; line-height: 1.6;">
                    Our AI model indicates an <strong>elevated risk</strong> of diabetes based on your current health metrics. 
                    We strongly recommend consulting with a healthcare professional for proper evaluation and guidance.
                </p>
                <div style="background: #fee2e2; border-radius: 10px; padding: 1rem; margin-top: 1.5rem;">
                    <p style="color: #dc2626; font-weight: 500; margin: 0;">
                        📋 <strong>Next Steps:</strong> Schedule an appointment with your doctor for comprehensive testing
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-container">
                <div style="font-size: 4rem; margin-bottom: 1rem;">✅</div>
                <h2 style="color: #059669; font-weight: 700; margin-bottom: 1rem;">Low Diabetes Risk</h2>
                <p style="color: #374151; font-size: 1.1rem; line-height: 1.6;">
                    Great news! Our AI model indicates a <strong>low risk</strong> of diabetes based on your current health metrics. 
                    Continue maintaining your healthy lifestyle and regular check-ups.
                </p>
                <div style="background: #d1fae5; border-radius: 10px; padding: 1rem; margin-top: 1.5rem;">
                    <p style="color: #059669; font-weight: 500; margin: 0;">
                        🌟 <strong>Keep it up:</strong> Maintain healthy diet, exercise regularly, and monitor your health
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.markdown(f"""
        <div class="result-container">
            <div style="font-size: 3rem; margin-bottom: 1rem;">❌</div>
            <h2 style="color: #dc2626; font-weight: 700; margin-bottom: 1rem;">Analysis Error</h2>
            <p style="color: #374151;">
                An error occurred during analysis: <code>{str(e)}</code>
            </p>
            <p style="color: #6b7280; font-size: 0.9rem; margin-top: 1rem;">
                Please check your input values and try again.
            </p>
        </div>
        """, unsafe_allow_html=True)

# Footer with disclaimer
st.markdown("""
<div class="input-container" style="margin-top: 3rem;">
    <div style="text-align: center; color: #6b7280;">
        <p style="font-size: 0.9rem; line-height: 1.5;">
            ⚠️ <strong>Medical Disclaimer:</strong> This tool is for informational purposes only and should not replace professional medical advice. 
            Always consult with qualified healthcare providers for medical decisions.
        </p>
        <p style="font-size: 0.8rem; margin-top: 1rem; opacity: 0.7;">
            Powered by Machine Learning • Built with Streamlit
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar with additional information
with st.sidebar:
    st.markdown("""
    ### 📖 Understanding the Parameters
    
    **Glucose**: Blood sugar level measured after fasting
    
    **Blood Pressure**: Diastolic pressure (bottom number)
    
    **Skin Thickness**: Triceps skin fold measurement
    
    **Insulin**: Serum insulin level after fasting
    
    **BMI**: Body Mass Index (weight/height²)
    
    **Diabetes Pedigree**: Genetic predisposition score
    
    **Age**: Current age in years
    
    ---
    
    ### 🎯 Healthy Ranges
    - **Glucose**: 70-100 mg/dL
    - **Blood Pressure**: 60-80 mmHg
    - **BMI**: 18.5-24.9
    - **Age**: Risk increases with age
    
    ---
    
    ### 💡 Tips for Better Health
    - Maintain regular exercise
    - Follow a balanced diet
    - Monitor blood sugar regularly
    - Stay hydrated
    - Get adequate sleep
    """)
