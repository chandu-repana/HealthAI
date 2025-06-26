import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sample_health_data():
    dates = pd.date_range(datetime.now() - timedelta(days=30), periods=30)
    heart_rate = [random.randint(60, 100) for _ in range(30)]
    bp_sys = [random.randint(110, 130) for _ in range(30)]
    bp_dia = [random.randint(70, 85) for _ in range(30)]
    glucose = [random.randint(90, 140) for _ in range(30)]
    return pd.DataFrame({
        'Date': dates,
        'Heart Rate': heart_rate,
        'BP Sys': bp_sys,
        'BP Dia': bp_dia,
        'Glucose': glucose
    })

def get_default_profile():
    return {'Name': 'John Doe', 'Age': 30, 'Gender': 'Male', 'Condition': 'None'}
