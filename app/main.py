from fastapi import FastAPI
import uvicorn
from commons.base_repository import BaseRepository
from config.database import get_db

app = FastAPI()

@app.get('/api/v1/users')
def get_usuarios():
    return {"info": "todos os usuarios"}

@app.get('/api/v1/users{id}')
def get_usuario(id:int):
    base_repository = BaseRepository()
    base_repository.filter_by_id()
    return 'usuario'

@app.post('/api/v1/users')
def post_usruario(usuario):
    return usuario


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)