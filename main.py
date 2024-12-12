
#! import libraries
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#! load the saved models
diabetes = pickle.load(open('diabetes.sav', 'rb'))
heart = pickle.load(open('heart_data.sav', 'rb'))
parkinsons = pickle.load(open('parkinsons_model.sav', 'rb'))

#! Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                            ['Diabetes Prediction',
                            'Heart Disesease Prediction',
                            'Parkinsons Prediction'],
                            icons = ['activity','heart','person'],
                            default_index=0)

#! Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    #! page title
    st.title('Diabetes Prediction Using ML')

    #! getting the input data from the user
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
    with col2:
        Glucose = st.number_input('Glucose Level')
    with col1:
        BloodPressure = st.number_input('Blood Pressure value')
    with col2:
        SkinThickness = st.number_input('Skin Thickness value')
    with col1:
        Insulin = st.number_input('Insulin Level')
    with col2:
        BMI = st.number_input('BMI value')
    with col1:
        dpf = st.text_input('Diabetes Pedigree Function')
    with col2:
        age = st.text_input('Age')

    #! code for prediction
    diagnosis = ''

    #! creating a button for prediction
    if st.button('Diabetes Test Result'):
        prediction = diabetes.predict([[pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age]])
        if (prediction[0] == 1):
            diagnosis = 'The person is diabetic'
        else:
            diagnosis = 'The person is not diabetic'
    st.success(diagnosis)

if (selected == 'Heart Disesease Prediction'):
    #! page title
    st.title('Heart Disesease Prediction Using ML')

    #! getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    #! code for prediction
    diagnosis = ''

    #! creating a button for prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        prediction = heart.predict([user_input])
        if prediction[0] == 1:
            diagnosis = 'The person is having heart disease'
        else:
            diagnosis = 'The person does not have any heart disease'
    st.success(diagnosis)


if (selected == 'Parkinsons Prediction'):
    #! page title
    st.title('Parkinsons Prediction Using ML')

    #! getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    #! code for prediction
    diagnosis = ''

    #! creating a button for prediction
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        prediction = parkinsons.predict([user_input])
        if prediction[0] == 1:
            diagnosis = "The person has Parkinson's disease"
        else:
            diagnosis = "The person does not have Parkinson's disease"
    st.success(diagnosis)