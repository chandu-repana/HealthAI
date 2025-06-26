import streamlit as st
from huggingface_api import query_huggingface
from utils import generate_sample_health_data, get_default_profile
import plotly.express as px

st.set_page_config(page_title="HealthAI", layout="wide")

if 'profile' not in st.session_state:
    st.session_state['profile'] = get_default_profile()

menu = st.sidebar.selectbox("Select Feature", ["Patient Chat", "Disease Prediction", "Treatment Plan", "Health Analytics"])

if menu == "Patient Chat":
    st.title("🩺 Patient Chat Assistant")
    user_input = st.text_input("Ask a health question:")
    if user_input:
        prompt = f"Act as a healthcare assistant. Answer clearly: {user_input}"
        response = query_huggingface(prompt)
        st.success(response)

elif menu == "Disease Prediction":
    st.title("🤒 Disease Prediction")
    symptoms = st.text_area("Describe your symptoms:")
    if symptoms:
        prompt = f"List possible diseases based on: {symptoms}"
        response = query_huggingface(prompt)
        st.info(response)

elif menu == "Treatment Plan":
    st.title("💊 Treatment Plan Generator")
    condition = st.text_input("Enter diagnosed condition:")
    if condition:
        prompt = f"Provide a treatment plan for: {condition}"
        response = query_huggingface(prompt)
        st.warning(response)

elif menu == "Health Analytics":
    st.title("📊 Health Analytics Dashboard")
    df = generate_sample_health_data()
    st.dataframe(df)

    fig1 = px.line(df, x='Date', y='Heart Rate', title='Heart Rate Trend')
    fig2 = px.line(df, x='Date', y=['BP Sys', 'BP Dia'], title='Blood Pressure Trend')
    fig3 = px.line(df, x='Date', y='Glucose', title='Glucose Level Trend')

    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
