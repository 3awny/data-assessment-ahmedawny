from fastapi import APIRouter, HTTPException
from typing import List
import pandas as pd
from .schemas import Employee
from .utils import get_employee_data_analyzer

router = APIRouter()  # Create a new FastAPI router

employee_data_analyzer = get_employee_data_analyzer()  # Get an instance of the DataAnalyzer

# Endpoint to get the top N highest paid employees
@router.get("/top-n-highest-paid-employees", response_model=List[Employee])
async def get_top_n_highest_paid_employees(n: int):
    if n <= 0:
        raise HTTPException(status_code=400, detail="The number of employees must be greater than zero.")
    # Use the data analyzer to find the top N highest paid employees
    top_n_employees = employee_data_analyzer.find_top_n_highest_paid_employees(n)
    return top_n_employees

# Endpoint to get the number of employees in a specific department
@router.get("/number-of-employees-in-department")
async def get_number_of_employees_in_department(department: str):
    # Use the data analyzer to determine the number of employees in the specified department
    num_employees = employee_data_analyzer.determine_x_department_number_of_employees(department)
    return {"department": department, "number_of_employees": num_employees}
