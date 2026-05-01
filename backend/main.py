from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sabko allow karega
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data load
df = pd.read_csv("data/student_satisfaction.csv")

@app.get("/")
def home():
    return {"message": "Campus Pulse API Running"}

# Full data
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

# Metrics
@app.get("/metrics")
def get_metrics():
    return {
        "overall_avg": df['satisfaction_score'].mean(),
        "best_facility": df.groupby('facility_rated')['satisfaction_score'].mean().idxmax(),
        "worst_facility": df.groupby('facility_rated')['satisfaction_score'].mean().idxmin()
    }

# Filter
@app.get("/filter")
def filter_data(facility: str):
    filtered = df[df['facility_rated'] == facility]
    return filtered.to_dict(orient="records")