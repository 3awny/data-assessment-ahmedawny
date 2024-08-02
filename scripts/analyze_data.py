from config import *
import pandas as pd
from services import EmployeeDataAnalyzer

def main():
    analyzer = EmployeeDataAnalyzer('app/data/employee_cleaned_data.csv')

    # Calculate the average salary per department
    avg_salary_per_department = analyzer.calculate_average_salary_per_department()
    print("A) Average Salary per Department:")
    for item in avg_salary_per_department:
        print(f"  Department: {item['Department']}, Average Salary: ${item['Average_Salary']:,.2f}")
    print("\n\n")
    # Find the top 3 highest paid employees
    top_3_highest_paid_employees = analyzer.find_top_n_highest_paid_employees(3)
    print("\nB) Top 3 Highest Paid Employees:")
    for idx, item in enumerate(top_3_highest_paid_employees, start=1):
        print(f"  {idx}. Name: {item['Name']}, Salary: ${item['Salary']:,.2f}, Department: {item['Department']}")
    print("\n\n")
    # Determine the number of employees in each department
    num_employees_per_department = analyzer.determine_number_of_employees_per_department()
    print("\nC) Number of Employees per Department:")
    for item in num_employees_per_department:
        print(f"  Department: {item['Department']}, Number of Employees: {item['Number_of_Employees']}")
    print("\n\n")

if __name__ == "__main__":
    main()
