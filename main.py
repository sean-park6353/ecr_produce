from fastapi import FastAPI
from routes import diary_route
app = FastAPI()
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import os 
app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(diary_route.router)
print("*"*30)
print(os.getenv("MYSQL_URL"))
print("*"*30)

@app.get("/", description="나무 페이지", tags=["API"])
def root_page():
    return "it is root site"




