from fastapi import FastAPI
from api.v1 import matrice
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=settings.ORIGINS,
    allow_headers=["*"],
    allow_methods=["*"],
)




app.include_router(matrice.route)
