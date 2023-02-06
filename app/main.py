from fastapi import FastAPI
from dotenv import load_dotenv
from app.ui.controllers.user_controller import user_controller

load_dotenv()

app = FastAPI()

user_controller(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}
