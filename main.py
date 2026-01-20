from fastapi import FastAPI
from app.routes.route1 import router as pachu_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware, # to allow cross origin resource sharing meaning that we can access this from any domain
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(pachu_router)