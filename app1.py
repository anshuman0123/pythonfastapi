from fastapi import FastAPI

from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware



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
    return [FileResponse("C:/Users/anshu/Desktop/pythonfastapi/disha1.jpeg"), FileResponse("C:/Users/anshu/Desktop/pythonfastapi/disha2.jpeg")]