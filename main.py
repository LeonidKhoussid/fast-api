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

@app.get("/posts")
def read_csv():
    try:
        df = pd.read_csv("transformed_data.csv")
        return df.fillna("").to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}