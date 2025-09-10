import numpy as np
import pickle
import streamlit as st


# # loading the saved model
loaded_model = pickle.load(open("loan_prediction_model_v2.pkl", "rb"))

def loan_prediction(input_data):
    input_data =(0, 0, 0, 1, 1.34, 0.5, 5.5, 180, 0, 0, 1, 0, 0, 1)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    

    # reshape the array so the model will understand i am making prediction foe one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    

    # making prediction on the loaded model
    prediction = loaded_model.predict(input_data_reshaped)
 
    if prediction[0] == 0:
        return("This customer is not eligible for a loan")
    else:
        return("This customer is eligible for a loan")
    

def main():
    # giving the app a title
    st.title("Loan Prediction web App")
    
    
    # getting the input data from user

    gender = st.text_input("gender")
    married = st.text_input("married")
    education = st.text_input("education")
    self_employed = st.text_input("self_employed")
    applicant_income = st.text_input("applicant_income")
    coapplicant_income = st.text_input("coapplicant_income")
    loan_amount = st.text_input("loan_amount")
    loan_amount_term = st.text_input("loan_amount_term")
    dependent_1 = st.text_input("dependent_1")
    dependents_2 = st.text_input("dependents_2")
    dependents_3 = st.text_input("dependents_3+")
    credit_history = st.text_input("credit_history")
    property_area_Semiurban = st.text_input("property_area_Semiurban")
    property_area_Urban = st.text_input("property_area_Urban")

    # code for prediction
    performance = ""

    # creating a button for prediction

    if st.button("Loan status"):
        performance = loan_prediction(
            [int(gender), int(married), int(education), int(self_employed), int(applicant_income), int(coapplicant_income),
            int(loan_amount), int(loan_amount_term), int(dependent_1), int(dependents_2),
            int(dependents_3), int(credit_history), int(property_area_Semiurban), int(property_area_Urban])
        st.success(performance)


if __name__ == "__main__":
    main()
    




