from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load CSV once at startup
try:
    df = pd.read_csv("transformed_data.csv")
    df = df.fillna("")
    data = df.to_dict(orient="records")
except Exception as e:
    data = []
    print(f"Error loading CSV: {e}")

@app.get("/")
def root():
    return {"status": "OK"}

@app.get("/posts")
def get_posts():
    return data