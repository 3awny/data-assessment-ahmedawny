from pydantic import BaseModel

# Define the Employee schema
class Employee(BaseModel):
    Name: str  # Employee's name
    Salary: float  # Employee's salary
    Department: str  # Employee's department
