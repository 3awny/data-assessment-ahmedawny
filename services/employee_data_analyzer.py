import pandas as pd

# Class for employee data analysis
class EmployeeDataAnalyzer:
    # Initialize the class with the data from a CSV file
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        
    # Method to calculate the average salary per department
    def calculate_average_salary_per_department(self):
        # Group data by 'Department' and calculate the mean of 'Salary'
        result = self.df.groupby('Department', as_index=False).agg(Average_Salary=('Salary', 'mean'))
        # Sort the result by 'Average_Salary' in descending order for better interpretation
        result = result.sort_values(by='Average_Salary', ascending=False)
        # Convert result to a dictionary with 'float' type for 'Average_Salary'
        return result.astype({'Average_Salary': 'float'}).to_dict(orient='records')
    
    # Method to find the top N highest paid employees
    def find_top_n_highest_paid_employees(self, n):
        # Get the top N largest values in 'Salary' and select relevant columns
        result = self.df.nlargest(n, 'Salary')[['Name', 'Salary', 'Department']]
        # Convert result to a dictionary with 'float' type for 'Salary'
        return result.astype({'Salary': 'float'}).to_dict(orient='records')
    
    # Method to determine the number of employees per department
    def determine_number_of_employees_per_department(self):
        # Use value_counts to get the count of employees per department
        result = self.df['Department'].value_counts().reset_index()
        # Rename columns for clarity
        result.columns = ['Department', 'Number_of_Employees']
        # Ensure 'Number_of_Employees' is numeric, fill missing values with 0, and convert to integer
        result['Number_of_Employees'] = pd.to_numeric(result['Number_of_Employees'], errors='coerce').fillna(0).astype(int)
        return result.to_dict(orient='records')
    
    # Method to determine the number of employees in a specific department
    def determine_x_department_number_of_employees(self, department):
        # Get the count of employees in the specified department
        num_employees = self.df['Department'].value_counts().get(department.lower(), 0)
        return int(num_employees)
