import pandas as pd
import numpy as np
from io import StringIO

def load_data(file_path):
    return pd.read_csv(file_path)

def fill_missing_ids(df):
    for i in range(1, len(df)):
        if pd.isna(df.loc[i, 'ID']):
            df.loc[i, 'ID'] = df.loc[i-1, 'ID'] + 1
    return df

def handle_missing_values(df):
    df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], errors='coerce')
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    median_salary = df['Salary'].median()
    df['Salary'] = df['Salary'].fillna(median_salary)
    df = df.fillna({'Department': 'not_available', 'Name': 'not_available'})
    return df

def remove_outliers(df):
    salary_mean = df['Salary'].mean()
    salary_std = df['Salary'].std()
    df['Z_Score_Salary'] = (df['Salary'] - salary_mean) / salary_std
    
    df = df[(np.abs(df['Z_Score_Salary']) <= 3) & (df['Salary'] >= 0)]
    df = df.drop(columns=['Z_Score_Salary'])
    return df

def recalibrate_ids(df):
    df['ID'] = range(1, len(df) + 1)
    return df

def standardize_data_formats(df):
    df['Date_of_Birth'] = df['Date_of_Birth'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d') if not pd.isna(x) else x)
    df['Department'] = df['Department'].str.lower()
    return df

def clean_data(input_file: str, output_file: str):
    df = load_data(input_file)
    df = fill_missing_ids(df)
    df = handle_missing_values(df)
    df = remove_outliers(df)
    df = recalibrate_ids(df)
    df = standardize_data_formats(df)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    clean_data('app/data/raw_data.csv', 'app/data/cleaned_data.csv')
