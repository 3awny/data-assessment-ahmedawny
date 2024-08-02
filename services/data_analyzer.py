
import pandas as pd

class DataAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        
    def calculate_average_salary_per_department(self):
        result = self.df.groupby('Department', as_index=False).agg(Average_Salary=('Salary', 'mean'))
        return result.astype({'Average_Salary': 'float'}).to_dict(orient='records')
    
    def find_top_n_highest_paid_employees(self, n):
        result = self.df.nlargest(n, 'Salary')[['Name', 'Salary', 'Department']]
        return result.astype({'Salary': 'float'}).to_dict(orient='records')
    
    def determine_number_of_employees_per_department(self):
        # Use value_counts to get the count of employees per department
        result = self.df['Department'].value_counts().reset_index()
        result.columns = ['Department', 'Number_of_Employees']  # Rename columns for clarity
        result['Number_of_Employees'] = pd.to_numeric(result['Number_of_Employees'], errors='coerce').fillna(0).astype(int)
        return result.to_dict(orient='records')
    
    def determine_x_department_number_of_employees(self, department):
        num_employees = self.df['Department'].value_counts().get(department.lower(), 0)
        return int(num_employees)
