from fastapi import FastAPI
from api.v1 import matrice
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["http://127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["*"],
)




app.include_router(matrice.route)
