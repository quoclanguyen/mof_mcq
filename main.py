from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
import random

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

@app.get("/exam")
def exam(request: Request):
    sample = random.sample(questions, 40)
    return templates.TemplateResponse("exam.html", {
        "request": request,
        "questions": sample
    })
