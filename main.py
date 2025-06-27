from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

with open("data/questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "questions": questions
    })
