from fastapi import FastAPI
 
from domain.user import user_routes
 
def setup_routes(app: FastAPI):
    app.include_router(user_routes.router,
                        tags=['User'],
                        prefix="/user")