from fastapi import APIRouter, HTTPException
from typing import List
from app.models.fund import Fund, FundCreate
from app.core.fund_services import (
    create_new_fund,
    get_all_funds,
    get_fund_by_id,
    update_existing_fund,
    delete_fund
)

router = APIRouter()

@router.post("/funds/", response_model=Fund)
def create_fund(fund: FundCreate):
    return create_new_fund(fund)

@router.get("/funds/", response_model=List[Fund])
def read_funds():
    return get_all_funds()

@router.get("/funds/{fund_id}", response_model=Fund)
def read_fund(fund_id: str):
    fund = get_fund_by_id(fund_id)
    if fund is None:
        raise HTTPException(status_code=404, detail="Fondo no encontrado")
    return fund

@router.put("/funds/{fund_id}", response_model=Fund)
def update_fund(fund_id: str, fund_update: dict):
    fund = update_existing_fund(fund_id, fund_update)
    if fund is None:
        raise HTTPException(status_code=404, detail="Fondo no encontrado")
    return fund

@router.delete("/funds/{fund_id}")
def remove_fund(fund_id: str):
    delete_fund(fund_id)
    return {"detail": "Fondo eliminado"}