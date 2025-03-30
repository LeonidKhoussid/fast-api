from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Optional: enable CORS so frontend can access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/posts")
def get_posts():
    try:
        df = pd.read_csv("transformed_data.csv")
        df = df.fillna("")
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}