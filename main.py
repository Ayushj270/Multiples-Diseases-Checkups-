
#! Import Libraries
import pickle
import streamlit as st

#! Load the saved models
diabetes = pickle.load(open('diabetes.sav', 'rb'))
heart = pickle.load(open('heart_data.sav', 'rb'))
parkinsons = pickle.load(open('parkinsons_model.sav', 'rb'))

#! Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'main_page'

#! Main Page: Disease Selection
if st.session_state.page == 'main_page':
    st.title('Disease Prediction System')
    st.subheader('Select the type of disease to predict:')
    disease = st.selectbox('Choose a prediction system:', 
                           ['Select Your Prediction Mechanism','Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'])  

    if disease != 'Select Your Prediction Mechanism' and st.button('Next'):
        st.session_state.disease = disease
        st.session_state.page = 'prediction_page'

#! Diabetes Prediction
elif st.session_state.page == 'prediction_page':
    disease = st.session_state.disease

    #! Diabetes prediction
    if disease == 'Diabetes Prediction':
        st.title('Diabetes Prediction')
        st.subheader("Check Gender.")

        #! Gender Selection
        def gender_selection():
            gender = st.selectbox('Gender', ['None', 'Male', 'Female'])
            if gender != 'None':
                st.write(f'You are a {gender}.')
                return gender
            else:
                st.write('Please select a gender.')
                return None

        #! Input Fields
        def input_fields(gender):
            col1, col2 = st.columns(2)
            if gender == 'Male':
                with col1:
                    pregnancies = 0
                    glucose = st.number_input('Glucose Level', min_value=0.0, max_value=200.0, step=0.1)
                    bp = st.number_input('Blood Pressure value', min_value=0.0, max_value=122.0, step=0.1)
                    skinthickness = st.number_input('Skin Thickness value', min_value=0.0, max_value=99.0, step=0.1)
                    insulin = st.number_input('Insulin Level', min_value=0.0, max_value=846.0, step=0.1)
                with col2:
                    bmi = st.number_input('BMI value', min_value=0.0, max_value=67.1, step=0.1)
                    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.42, step=0.1)
                    age = st.number_input('Age', min_value=0, max_value=81, step=1)
           
            elif gender == 'Female':
                with col1:
                    pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=17, step=1)
                    glucose = st.number_input('Glucose Level', min_value=0.0, max_value=200.0, step=0.1)
                    bp = st.number_input('Blood Pressure value', min_value=0.0, max_value=122.0, step=0.1)
                    skinthickness = st.number_input('Skin Thickness value', min_value=0.0, max_value=99.0, step=0.1)
                with col2:
                    insulin = st.number_input('Insulin Level', min_value=0.0, max_value=846.0, step=0.1)
                    bmi = st.number_input('BMI value', min_value=0.0, max_value=67.1, step=0.1)
                    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.42, step=0.1)
                    age = st.number_input('Age', min_value=0, max_value=81, step=1)
            else:
                st.error("Invaild Gender Selection")
                return None, None, None, None, None, None, None, None

            return pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age

        #! Prediction
        def prediction(pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age):
            if st.button('Predict Diabetes'):
                if age == 0:
                    st.error("Please enter valid input")

                else:
                    try:
                        prediction = diabetes.predict([[pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age]])
                        result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'
                        st.success(f'Result: The person is {result}')
                    except:
                        st.error("Please enter valid input")

            if st.button('Go Back', key='back_to_main_from_diabetes'):
                st.session_state.page = 'main_page'

        gender = gender_selection()
        if gender:
            if st.button('Next', key='to_input_page'):
                st.session_state.page = 'input_page'

        st.subheader("Provide the required details for diabetes prediction.")
        pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age = input_fields(gender)

        if pregnancies is not None:
            prediction(pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age)

    #! Heart Disease Prediction
    elif disease == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction')
        st.subheader("Provide the required details for heart disease prediction.")
        
        #! Input fields
        def input_fields():
            col1, col2, col3 = st.columns(3)
            with col1:
                age = st.number_input('Age', min_value=0, max_value=100, step=1)
                sex = st.number_input('Sex', min_value=0, max_value=1, step=1)
                cp = st.number_input('Chest Pain types', min_value=0, max_value=3, step=1)
                trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=200, step=1)
                chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, max_value=600, step=1)
            with col2:
                fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0, max_value=1, step=1)
                restecg = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2, step=1)
                thalach = st.number_input('Maximum Heart Rate achieved', min_value=0, max_value=200, step=1)
                exang = st.number_input('Exercise Induced Angina', min_value=0, max_value=1, step=1)
            with col3:
                oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, max_value=6.2, step=0.1)
                slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1)
                ca = st.number_input('Major vessels colored by flourosopy', min_value=0, max_value=3, step=1)
                thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, step=1)

            return age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal

        #! Prediction
        def prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
            if st.button('Predict Heart Disease'):
                if age == 0:
                    st.error("Please enter valid input")

                else:
                    try:
                        prediction = diabetes.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                        result = 'Heart Disease' if prediction[0] == 1 else 'Healthy'
                        st.success(f'Result: The person is {result}')
                    except:
                        st.error("Please enter valid input")
            if st.button('Go Back'):
                st.session_state.page = 'main_page'
        
        age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal = input_fields()

        if age != 0:
            prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

    #! Parkinsons Prediction
    elif disease == 'Parkinsons Prediction':
        st.title('Parkinsons Prediction')
        st.subheader("Provide the required details for Parkinsons prediction.")
        
        #! Input fields
        def input_fields():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, max_value=200.0, step=0.1)
                fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, max_value=200.0, step=0.1)
                flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, max_value=200.0, step=0.1)
                Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, step=0.1)
                Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, max_value=1.0, step=0.1)
                RAP = st.number_input('MDVP:RAP', min_value=0.0, max_value=1.0, step=0.1)
                PPQ = st.number_input('MDVP:PPQ', min_value=0.0, max_value=1.0, step=0.1)
            with col2:
                DDP = st.number_input('Jitter:DDP', min_value=0.0, max_value=1.0, step=0.1)
                Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, max_value=1.0, step=0.1)
                Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, max_value=1.0, step=0.1)
                APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, max_value=1.0, step=0.1)
                APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, max_value=1.0, step=0.1)
                APQ = st.number_input('MDVP:APQ', min_value=0.0, max_value=1.0, step=0.1)
                DDA = st.number_input('MDVP:DDA', min_value=0.0, max_value=1.0, step=0.1)
            with col3:
                NHR = st.number_input('NHR', min_value=0.0, max_value=1.0, step=0.1)
                HNR = st.number_input('HNR', min_value=0.0, max_value=1.0, step=0.1)
                RPDE = st.number_input('RPDE', min_value=0.0, max_value=1.0, step=0.1)
                DFA = st.number_input('DFA', min_value=0.0, max_value=1.0, step=0.1)
                spread1 = st.number_input('spread1', min_value=0.0, max_value=1.0, step=0.1)
                spread2 = st.number_input('spread2', min_value=0.0, max_value=1.0, step=0.1)
                D2 = st.number_input('D2', min_value=0.0, max_value=1.0, step=0.1)
            PPE = st.number_input('PPE', min_value=0.0, max_value=1.0, step=0.1)

            return fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE

        #! Prediction
        def prediction(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE):
            if st.button('Result'):
                if fo == 0:
                    st.error("Please enter valid input")
                else:
                    try:
                        prediction = diabetes.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                        result = 'Heart Disease' if prediction[0] == 1 else 'Healthy'
                        st.success(f'Result: The person is {result}')
                    except:
                        st.error("Please enter valid input")
            if st.button('Go Back'):
                st.session_state.page = 'main_page'
        
        fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE = input_fields()

        if fo != 0:
            prediction(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE)
