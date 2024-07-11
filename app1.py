from fastapi import FastAPI

from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def read_item():
    return [FileResponse(os.path.join(os.getcwd(),"disha1.jpeg")), FileResponse(os.path.join(os.getcwd(),"disha2.jpeg"))] #FileResponse("disha2.jpeg")]