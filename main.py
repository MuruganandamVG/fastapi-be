from fastapi import FastAPI
from routes import resume

app = FastAPI()


app.include_router(resume.router)