from fastapi import FastAPI
from routes import diary_route
app = FastAPI()


app.include_router(diary_route.router)

@app.get("/", description="나무 페이지", tags=["API"])
def root_page():
    return "it is root site"




