import pandas as pd  # Import the pandas library for data manipulation
import numpy as np  # Import the numpy library for numerical operations

# Function to load data from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to fill missing IDs by incrementing the previous ID
def fill_missing_ids(df):
    for i in range(1, len(df)):
        if pd.isna(df.loc[i, 'ID']):
            df.loc[i, 'ID'] = df.loc[i-1, 'ID'] + 1
    return df

# Function to handle missing values in specific columns
def handle_missing_values(df):
    df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], errors='coerce')  # Convert 'Date_of_Birth' to datetime
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')  # Convert 'Salary' to numeric
    
    # Fill missing 'Salary' with median value
    median_salary = df['Salary'].median()
    df['Salary'] = df['Salary'].fillna(median_salary)
    
    # Fill missing 'Department' and 'Name' with 'not_available'
    df = df.fillna({'Department': 'not_available', 'Name': 'not_available'})
    return df

# Function to remove outliers in the 'Salary' column
def remove_outliers(df):
    salary_mean = df['Salary'].mean()  # Calculate mean of 'Salary'
    salary_std = df['Salary'].std()  # Calculate standard deviation of 'Salary'
    
    # Calculate Z-scores for 'Salary'
    df['Z_Score_Salary'] = (df['Salary'] - salary_mean) / salary_std
    
    # Filter out rows where Z-score is within -3 and 3, and 'Salary' is non-negative
    df = df[(np.abs(df['Z_Score_Salary']) <= 3) & (df['Salary'] >= 0)]
    
    # Drop the 'Z_Score_Salary' column as it is no longer needed
    df = df.drop(columns=['Z_Score_Salary'])
    return df

# Function to recalibrate 'ID' values sequentially
def recalibrate_ids(df):
    df['ID'] = range(1, len(df) + 1)
    return df

# Function to standardize data formats in the dataframe
def standardize_data_formats(df):
    # Standardize 'Date_of_Birth' format to 'YYYY-MM-DD'
    df['Date_of_Birth'] = df['Date_of_Birth'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d') if not pd.isna(x) else x)
    
    # Convert 'Department' values to lowercase
    df['Department'] = df['Department'].str.lower()
    return df

# Main function to clean data from input file and save to output file
def clean_data(input_file: str, output_file: str):
    df = load_data(input_file)  # Load data from input file
    df = fill_missing_ids(df)  # Fill missing IDs
    df = handle_missing_values(df)  # Handle missing values
    df = remove_outliers(df)  # Remove outliers
    df = recalibrate_ids(df)  # Recalibrate IDs
    df = standardize_data_formats(df)  # Standardize data formats
    df.to_csv(output_file, index=False)  # Save cleaned data to output file

# Entry point for script execution
if __name__ == "__main__":
    clean_data('app/data/employee_raw_data.csv', 'app/data/employee_cleaned_data.csv')
