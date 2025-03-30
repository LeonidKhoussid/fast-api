from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <- open access for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_csv():
    with open("transformed_data.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

@app.get("/posts")
def get_all_posts():
    return load_csv()

@app.get("/posts/{author_name}")
def get_posts_by_author(author_name: str):
    posts = load_csv()
    return [p for p in posts if p["autor_name"].lower() == author_name.lower()]