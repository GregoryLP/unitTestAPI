from server.routes.classeDestiny import router as destinyRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(destinyRouter, tags=["DestinyClasse"], prefix="/DestinyClasse")