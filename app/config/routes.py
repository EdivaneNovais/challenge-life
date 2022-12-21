from fastapi import FastAPI
 
from domain.user import user_routes
from domain.events import events_routes
from domain.registration import registration_routes
 
def setup_routes(app: FastAPI):
    app.include_router(user_routes.router,
                        tags=['User'],
                        prefix="/user")
    
    app.include_router(events_routes.router,
                       tags=['Event'],
                       prefix="/event")
    
    app.include_router(registration_routes.router,
                       tags=["Registration"],
                       prefix="/registration")