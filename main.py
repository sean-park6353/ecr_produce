from fastapi import FastAPI
from routes import diary_route
import os
app = FastAPI()

print("*"*40)
print(os.getenv("MYSQL_URL"))
print("*"*40)
app.include_router(diary_route.router)

@app.get("/", description="나무 페이지", tags=["API"])
def root_page():
    return "it is root site"




