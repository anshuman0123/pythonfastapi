from fastapi import FastAPI

from fastapi.responses import FileResponse
from fastapi.middlewares.cors import CORSMiddleware



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
    return [FileResponse("disha1.jpeg"), FileResponse("disha2.jpeg")]