#! Import Libraries
import pickle
import streamlit as st

#! Load the saved models
diabetes = pickle.load(open('diabetes.sav', 'rb'))
heart = pickle.load(open('git heart_data.sav', 'rb'))
parkinsons = pickle.load(open('parkinsons_model.sav', 'rb'))

#! Initializze session state
if 'page' not in st.session_state:
    st.session_state.page = 'main_page'

#! Main Page: Disease Selection
if st.session_state.page == 'main_page':
    st.title('Disease Prediction System')
    st.subheader('Select the type of disease to predict:')
    disease = st.selectbox('Choose a prediction system:', 
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'])    
    if st.button('Next'):
        st.session_state.disease = disease
        st.session_state.page = 'Prediction_page'

#! Diabetes Prediction
elif st.session_state.page == 'prediction_page':
    disease = st.session_state.disease
    if disease == 'Diabetes Prediction':
        st.title('Diabetes Prediction')
        st.subheader("Check Gender.")

        #! Gender Selection
        def gender_selection():
            gender = st.selectbox('Gender', ['None', 'Male', 'Female'])
            if gender == 'None':
                st.write('Please select a gender.')
            elif gender == 'Male':
                st.write('You are a Male')
            elif gender == 'Female':
                st.write('You are a Female')
            return gender

        gender = gender_selection()
        if gender is not None and st.button('Next'):
            st.session_state.gender = gender
            st.session_state.page = 'input_page'

            #! Input Fields
            def inputs_fields(gender):
                col1, col2 = st.columns(2)
                if gender == 'Male':
                    with col1:
                        pregnancies = 0
                        glucose = st.number_input('Glucose Level',min = 0, max = 200, step = 1, disabled = gender == 'None')
                        bp = st.number_input('Blood Pressure value', min = 0, max = 122, step = 0.1, disabled = gender == 'None')
                        skinthickness = st.number_input('Skin Thickness value', min=0, max = 99, step = 0.1,disabled = gender == 'None')
                        insulin = st.number_input('Insulin Level', min = 0, max = 846,  step = 0.1, disabled = gender == 'None')
                    with col2:
                        bmi = st.number_input('BMI value', min = 0, max = 67.1,step = 0.1, disabled = gender == 'None')
                        dpf = st.number_input('Diabetes Pedigree Function', min = 0, max = 2.42,step = 0.1, disabled = gender == 'None')
                        age = st.number_input('Age', min = 21, max = 81,step = 1, disabled = gender == 'None')

                elif gender == 'Female':
                    with col1:
                        pregnancies = st.number_input('Number of Pregnancies', min = 0, max = 17, step = 1,disabled = gender == 'None')
                        glucose = st.number_input('Glucose Level',min = 0, max = 200, step = 1, disabled = gender == 'None')
                        bp = st.number_input('Blood Pressure value', min = 0, max = 122, step = 0.1, disabled = gender == 'None')
                        skinthickness = st.number_input('Skin Thickness value', min=0, max = 99, step = 0.1,disabled = gender == 'None')
                        insulin = st.number_input('Insulin Level', min = 0, max = 846,  step = 0.1, disabled = gender == 'None')
                    with col2:
                        bmi = st.number_input('BMI value', min = 0, max = 67.1,step = 0.1, disabled = gender == 'None')
                        dpf = st.number_input('Diabetes Pedigree Function', min = 0, max = 2.42,step = 0.1, disabled = gender == 'None')
                        age = st.number_input('Age', min = 21, max = 81,step = 1, disabled = gender == 'None')
                return pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age

                st.subheader("Provide the required details for diabetes prediction.")
                pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age = inputs_fields(gender)

            #! Prediction
            prediction_disabled = (gender is None)
            if st.button('Predict Diabetes',disabled=prediction_disabled):
                try:
                    prediction = diabetes.predict([[pregnancies, glucose, bp, skinthickness, insulin, bmi, dpf, age]])
                    result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'
                    st.success(f'Result: The person is {result}')
                except:
                    st.error("Please enter valid input")
        if st.button('Go Back'):
            st.session_state.page = 'Diabetes Prediction'

    #! Heart Disease Prediction
    elif disease == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction')
        st.write("Provide the required details for heart disease prediction.")
        
        #! Input fields
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age')
            sex = st.number_input('Sex')
        with col2:
            cp = st.number_input('Chest Pain types')
            trestbps = st.number_input('Resting Blood Pressure')
        with col3:
            chol = st.number_input('Serum Cholestoral in mg/dl')        
            fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        with col1:
            restecg = st.number_input('Resting Electrocardiographic results')
            thalach = st.number_input('Maximum Heart Rate achieved')
        with col2:
            exang = st.number_input('Exercise Induced Angina')
            oldpeak = st.number_input('ST depression induced by exercise')
        with col3:
            slope = st.number_input('Slope of the peak exercise ST segment')
            ca = st.number_input('Major vessels colored by flourosopy')
        with col1:
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        #! Prediction
        if st.button('Predict Heart Disease'):
            try:
                prediction = heart.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                result = 'Heart Disease' if prediction[0] == 1 else 'Healthy'
                st.success(f'Result: The person is {result}')
            except:
                st.error("Please enter valid input")
        if st.button('Go Back'):
            st.session_state.page = 'main_page'

    #! Parkinsons Prediction
    elif disease == 'Parkinsons Prediction':
        st.title('Parkinsons Prediction')
        st.write("Provide the required details for Parkinsons prediction.")
        
        #! Input fields
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            fo = st.number_input('MDVP:Fo(Hz)')
            fhi = st.number_input('MDVP:Fhi(Hz)')
        with col2:
            flo = st.number_input('MDVP:Flo(Hz)')
            Jitter_percent = st.number_input('MDVP:Jitter(%)')
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        with col3:
            RAP = st.number_input('MDVP:RAP')
            PPQ = st.number_input('MDVP:PPQ')
        with col4:
            DDP = st.number_input('Jitter:DDP')
            Shimmer = st.number_input('MDVP:Shimmer')
        with col1:
            Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
            APQ3 = st.number_input('Shimmer:APQ3')
            APQ5 = st.number_input('Shimmer:APQ5')
        with col2:
            APQ = st.number_input('MDVP:APQ')
            DDA = st.number_input('MDVP:DDA')
        with col3:
            NHR = st.number_input('NHR')
            HNR = st.number_input('HNR')
        with col4:
            RPDE = st.number_input('RPDE')
            DFA = st.number_input('DFA')
        with col1:
            spread1 = st.number_input('spread1')    
            spread2 = st.number_input('spread2')
        with col2:
            D2 = st.number_input('D2')
            PPE = st.number_input('PPE')

        #! Prediction
        if st.button('Predict Parkinsons'):
            try:
                prediction = parkinsons.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
                result = 'Parkinsons' if prediction[0] == 1 else 'Healthy'
                st.success(f'Result: The person is {result}')
            except:
                st.error("Please enter valid input")
        if st.button('Go Back'):
            st.session_state.page = 'main_page'