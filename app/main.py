from fastapi import FastAPI
import uvicorn
from config.routes import setup_routes

app = FastAPI()
setup_routes(app)

@app.get("/")
def roo() -> str:
    return"Welcome"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)