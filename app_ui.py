import streamlit as st   # For creating web UI
import pickle            # To load saved model

# Load the trained model from file
model = pickle.load(open('model.pkl', 'rb'))

# Set title of the web app
st.title("Salary Prediction App")

# Create input field for user to enter experience
exp = st.number_input("Enter Experience", min_value=0, 
                      max_value=50, value=1)

# Create a button → when clicked, prediction will run
if st.button("Predict"):
    
    # Model expects input in 2D format → [[value]]
    result = model.predict([[exp]])
    
    # Display the predicted salary on screen
    st.write(f"Predicted Salary: {int(result[0])}")