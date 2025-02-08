import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Prediction of Disease Outbreaks", layout="wide", page_icon="&")

working_dir = os.path.dirname(os.path.abspath(__file__))

# Load saved models with relative paths
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/heart_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System',
                            ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                            menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Function to check if any input is empty
def is_empty(values):
    return any(v is None or v == '' for v in values)

# Add custom CSS styling for the page
st.markdown("""
    <style>
        /* Page Styling */
        body {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }

        /* Sidebar Styling */
        .sidebar .sidebar-content {
            background-color: #34495e;
            color: white;
            padding: 20px;
        }

        /* Title Styling */
        .title {
            text-align: center;
            font-size: 36px;
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Card Styling */
        .stCard {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Input Fields */
        .stNumberInput {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        /* Button Styling */
        .stButton {
            background-color: #3498db;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            border: none;
        }

        .stButton:hover {
            background-color: #2980b9;
        }

        /* Result Styling */
        .result-positive {
            font-size: 22px;
            font-weight: bold;
            color: red;
            text-align: center;
        }

        .result-negative {
            font-size: 22px;
            font-weight: bold;
            color: green;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Function to check if inputs are empty
def is_empty(values):
    return any(v is None or v == '' for v in values)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.markdown('<h1 class="title">Diabetes Prediction using ML</h1>', unsafe_allow_html=True)

    # Initialize variables to None (empty fields)
    Pregnancies = Glucose = BloodPressure = SkinThickness = Insulin = BMI = DiabetesPedigreeFunction = Age = None

    # Getting input data from the user in 3 columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0.0, step=0.001, format="%.3f", value=None)
        Glucose = st.number_input('Glucose Level', min_value=0.0, step=0.001, format="%.3f", key="Glucose", value=None)
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0, step=0.001, format="%.3f", key="BloodPressure", value=None)

    with col2:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0, step=0.001, format="%.3f", key="SkinThickness", value=None)
        Insulin = st.number_input('Insulin Level', min_value=0.0, step=0.001, format="%.3f", key="Insulin", value=None)
        BMI = st.number_input('BMI value', min_value=0.0, step=0.001, format="%.3f", key="BMI", value=None)

    with col3:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, step=0.001, format="%.3f", key="DiabetesPedigreeFunction", value=None)
        Age = st.number_input('Age of the Person', min_value=0.0, step=0.001, format="%.3f", key="Age", value=None)

    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result', key="diabetes_btn"):
        # Check if any input is empty (no value given or left unfilled)
        if is_empty([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.error("Please fill in all fields before proceeding!")
        else:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.markdown(f'<p class="result-text">{diab_diagnosis}</p>', unsafe_allow_html=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.markdown('<h1 class="title">Heart Disease Prediction using ML</h1>', unsafe_allow_html=True)

    # Initialize variables to None (empty fields)
    age = sex = cp = trestbps = chol = fbs = restecg = thalach = exang = oldpeak = slope = ca = thal = None

    # Getting input data from the user in 3 columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', value=None, step=0.000, format="%.3f")
        sex = st.number_input('Sex', value=None, step=0.000, format="%.3f")
        cp = st.number_input('Chest Pain types', value=None, step=0.000, format="%.3f")

    with col2:
        trestbps = st.number_input('Resting Blood Pressure', value=None, step=0.000, format="%.3f")
        chol = st.number_input('Serum Cholestoral in mg/dl', value=None, step=0.000, format="%.3f")
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', value=None, step=0.000, format="%.3f")

    with col3:
        restecg = st.number_input('Resting Electrocardiographic results', value=None, step=0.000, format="%.3f")
        thalach = st.number_input('Maximum Heart Rate achieved', value=None, step=0.000, format="%.3f")
        exang = st.number_input('Exercise Induced Angina', value=None, step=0.000, format="%.3f")

    # Second row of input fields
    col4, col5, col6 = st.columns(3)

    with col4:
        oldpeak = st.number_input('ST depression induced by exercise', value=None, step=0.000, format="%.3f")
        slope = st.number_input('Slope of the peak exercise ST segment', value=None, step=0.000, format="%.3f")

    with col5:
        ca = st.number_input('Major vessels colored by fluoroscopy', value=None, step=0.000, format="%.3f")
    with col6:
        thal = st.number_input('Thal: normal; 1 fixed defect; 2 reversible defect', value=None, step=0.000, format="%.3f")
        

    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result', key="heart_btn"):
        # Check if any input is empty (no value given or left unfilled)
        if is_empty([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            st.error("Please fill in all fields before proceeding!")
        else:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

            st.markdown(f'<p class="result-text">{heart_diagnosis}</p>', unsafe_allow_html=True)


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.markdown('<h1 class="title">Parkinson\'s Disease Prediction using ML</h1>', unsafe_allow_html=True)

    # Initialize variables to None (empty fields)
    fo = fhi = flo = Jitter_percent = Jitter_Abs = RAP = PPQ = DDP = Shimmer = Shimmer_dB = APQ3 = APQ5 = APQ = DDA = NHR = HNR = RPDE = DFA = spread1 = spread2 = D2 = PPE = None

    # Getting input data from the user in 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.number_input('Fo', value=None, step=0.001, format="%.3f")
        fhi = st.number_input('Fhi', value=None, step=0.001, format="%.3f")
        flo = st.number_input('Flo', value=None, step=0.001, format="%.3f")

    with col2:
        Jitter_percent = st.number_input('Jitter Percent', value=None, step=0.00001, format="%.5f")
        Jitter_Abs = st.number_input('Jitter Abs', value=None, step=0.00001, format="%.5f")
        RAP = st.number_input('RAP', value=None, step=0.00001, format="%.5f")

    with col3:
        PPQ = st.number_input('PPQ', value=None, step=0.00001, format="%.5f")
        DDP = st.number_input('DDP', value=None, step=0.00001, format="%.5f")
        Shimmer = st.number_input('Shimmer', value=None, step=0.00001, format="%.5f")

    # Second row of input fields
    col4, col5, col6 = st.columns(3)

    with col4:
        Shimmer_dB = st.number_input('Shimmer_dB', value=None, step=0.001, format="%.3f")
        APQ3 = st.number_input('APQ3', value=None, step=0.00001, format="%.5f")
        APQ5 = st.number_input('APQ5', value=None, step=0.00001, format="%.5f")

    with col5:
        APQ = st.number_input('APQ', value=None, step=0.00001, format="%.5f")
        DDA = st.number_input('DDA', value=None, step=0.00001, format="%.5f")
        NHR = st.number_input('NHR', value=None, step=0.000001, format="%.5f")

    with col6:
        HNR = st.number_input('HNR', value=None, step=0.001, format="%.3f")
        RPDE = st.number_input('RPDE', value=None, step=0.000001, format="%.6f")
        DFA = st.number_input('DFA', value=None, step=0.000001, format="%.6f")

    col7, col8, col9 = st.columns(3)

    with col7:
        spread1 = st.number_input('Spread1', value=None, step=0.000001, format="%.6f")
        spread2 = st.number_input('Spread2', value=None, step=0.000001, format="%.6f")

    with col8:
        D2 = st.number_input('D2', value=None, step=0.000001, format="%.6f")

    with col9:
        PPE = st.number_input('PPE', value=None, step=0.000001, format="%.6f")

    park_diagnosis = ''

    if st.button('Parkinson\'s Test Result', key="parkinsons_btn"):
        # Check if any input is empty (no value given or left unfilled)
        if is_empty([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer,Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            st.error("Please fill in all fields before proceeding!")
        else:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer,Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            park_prediction = parkinsons_model.predict([user_input])

            if park_prediction[0] == 1:
                park_diagnosis = 'The person has Parkinson\'s disease'
            else:
                park_diagnosis = 'The person does not have Parkinson\'s disease'

            st.markdown(f'<p class="result-text">{park_diagnosis}</p>', unsafe_allow_html=True)
