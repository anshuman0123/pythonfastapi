from fastapi import FastAPI,Response,Cookie
from fastapi.responses import HTMLResponse,FileResponse
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. You might want to restrict this to specific origins.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods.
    allow_headers=["*"],
)
@app.get("/")
async def home(r:Response,name:Annotated[str | None , Cookie()]=None):
    if name:
        print(name)
        return HTMLResponse(content=f"<h1>hello {name}</h1>")
    r.set_cookie(key="name",value="anshu")
    return {"nothing":"here"} #HTMLResponse("<h1>Hello new User</h1> <form action='/{name}' method='post'>enter your name <input type='text' name='name' /></form>")
@app.get("/{name}")
def name(name:str):
    return [FileResponse("C:/Users/anshu/Desktop/pythonfastapi/disha_patani.jpeg"),FileResponse("C:/Users/anshu/Desktop/pythonfastapi/disha_2.jpeg")]
