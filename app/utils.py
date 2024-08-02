
from config import *
import pandas as pd
from services import EmployeeDataAnalyzer

def get_employee_data_analyzer():
    return EmployeeDataAnalyzer('app/data/employee_cleaned_data.csv')
