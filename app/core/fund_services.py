from typing import List
from app.models.fund import Fund, FundCreate
from app.crud.fund import FundCRUD

fund_crud = FundCRUD()

def create_new_fund(fund_data: FundCreate) -> Fund:
    return fund_crud.create_fund(fund_data)

def get_all_funds() -> List[Fund]:
    return fund_crud.get_funds()

def get_fund_by_id(fund_id: str) -> Fund:
    return fund_crud.get_fund_by_id(fund_id)

def update_existing_fund(fund_id: str, fund_update: dict) -> Fund:
    return fund_crud.update_fund(fund_id, fund_update)

def delete_fund(fund_id: str):
    fund_crud.delete_fund(fund_id)