from fastapi import APIRouter, HTTPException
from typing import List
import pandas as pd
from .schemas import Employee
from .utils import get_data_analyzer

router = APIRouter()

data_analyzer = get_data_analyzer()

@router.get("/top-n-highest-paid-employees", response_model=List[Employee])
async def get_top_n_highest_paid_employees(n: int):
    if n <= 0:
        raise HTTPException(status_code=400, detail="The number of employees must be greater than zero.")
    top_n_employees = data_analyzer.find_top_n_highest_paid_employees(n)
    return top_n_employees

@router.get("/number-of-employees-in-department")
async def get_number_of_employees_in_department(department: str):
    num_employees = data_analyzer.determine_x_department_number_of_employees(department)
    return {"department": department, "number_of_employees": num_employees}
