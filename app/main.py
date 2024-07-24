from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.client import router as client_router
from app.api.transactions import router as transaction_router
from app.api.fund import router as fund_router

app = FastAPI()

app.include_router(client_router, prefix="/api")
app.include_router(transaction_router, prefix="/api")
app.include_router(fund_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Reemplaza con la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)