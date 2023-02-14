from fastapi import FastAPI
 
from domain.user import user_routes
from domain.events import events_routes
from domain.registration import registration_routes
 
def setup_routes(app: FastAPI):
    app.include_router(user_routes.router,
                        tags=['User'],
                        prefix="/api/v1")
    
    app.include_router(events_routes.router,
                       tags=['Event'],
                       prefix="/api/v1")
    
    app.include_router(registration_routes.router,
                       tags=["Registration"],
                       prefix="/api/v1")