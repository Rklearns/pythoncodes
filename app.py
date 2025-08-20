import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("wine_model.joblib")

# Set page config
st.set_page_config(page_title="🍷 Wine Quality Predictor", page_icon="🍷", layout="wide")

# --- Sidebar ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1525/1525050.png", width=120)
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Enter values manually to predict the wine quality.")

# --- Main Title ---
st.markdown(
    "<h1 style='text-align: center; color: #B22222;'>🍷 Wine Quality Prediction 🍷</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center; color: #555;'>Enter the wine properties below to predict its quality.</h4>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Feature placeholders with default values
feature_defaults = {
    "fixed acidity": "7.8",
    "volatile acidity": "0.3",
    "citric acid": "0.4",
    "residual sugar": "6.4",
    "chlorides": "0.029",
    "free sulfur dioxide": "45",
    "total sulfur dioxide": "170",
    "density": "0.9959",
    "pH": "3.24",
    "sulphates": "0.72",
    "alcohol": "11.8"
}


# Columns layout for input fields
col1, col2 = st.columns(2)
user_input = {}

# Input Fields using Search Bars (Text Inputs)
for i, (feature, default_val) in enumerate(feature_defaults.items()):
    col = col1 if i % 2 == 0 else col2  # Alternate columns
    user_input[feature] = col.text_input(f"🔹 {feature}", value=default_val)

# --- Prediction Button ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🍷 Predict Wine Quality", use_container_width=True):
    try:
        # Convert input values to float
        input_data = {feature: float(value) for feature, value in user_input.items()}
        input_df = pd.DataFrame([input_data])  # Convert to DataFrame
        prediction = model.predict(input_df)[0]  # Get prediction

        # --- Display Result ---
        if prediction == 1:
            st.success("✅ **Good Quality Wine!** 🍾 Enjoy! 🎉")
            st.balloons()
        else:
            st.error("❌ **Poor Quality Wine!** 😞 Better luck next time!")
    
    except ValueError:
        st.error("⚠️ Please enter valid numerical values.")

# Footer
st.markdown(
    "<hr><p style='text-align: center; color: #888;'>Made with ❤️ using Streamlit | 🍇 Cheers!</p>",
    unsafe_allow_html=True,
)
