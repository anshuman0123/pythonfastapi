from fastapi import FastAPI

from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import List
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class imges(BaseModel):
    path : str
@app.get("/")
def home():
    return [imges(path="/files/disha1.jpeg"),imges(path="/files/disha2.jpeg")]

@app.get("/files/{filename}")
def get_file(filename: str):
    return FileResponse(filename)     