
# Data Analysis and API Project Description

This project is designed to clean and analyze employee and house price data, and expose the analysis via a FastAPI application. The project includes scripts for data cleaning, analysis, statistical regression, and tests to ensure the API endpoints function correctly.

## Project Structure

```
fastapi_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py               # Main FastAPI application
│   ├── schemas.py            # Pydantic schemas
│   ├── routes.py             # API routes
│   ├── utils.py              # Utility functions for data processing
│   ├── data/
│   │   ├── raw_data.csv      # Raw CSV data
│   │   └── cleaned_data.csv  # Cleaned CSV data
│   └── tests/
│       ├── __init__.py
│       └── test_api.py       # Unit tests
│
├── services/
│   ├── __init__.py
│   ├── data_analyzer.py      # Data analysis class
│
├── scripts/
│   ├── clean_data.py         # Script for cleaning data
│   ├── analyze_data.py       # Script for data analysis and aggregation
│   └── linear_regression.py  # Script for regression analysis
│
├── run_all.sh                # Shell script to run all scripts and tests
├── .gitignore
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Setup

### Install Dependencies

Ensure you have Python installed, then install the required packages:

```bash
pip install -r requirements.txt
```

### Data Cleaning and Preparation

To clean the data, run the data cleaning script:

```bash
python scripts/clean_data.py
```

This script handles missing values, outliers, and standardizes data formats.

### Data Analysis and Aggregation

To analyze the cleaned data, run the data analysis script:

```bash
python scripts/analyze_data.py
```

This script calculates the average salary per department, finds the top 3 highest-paid employees, and determines the number of employees in each department.

### Regression Analysis

To perform a linear regression analysis on house prices, run the regression analysis script:

```bash
python scripts/linear_regression.py
```

This script loads the dataset, preprocesses it, splits it into training and testing sets, trains the model, evaluates the model, and visualizes the results.

### Running the FastAPI Application

To start the FastAPI application, run:

```bash
uvicorn app.main:app --reload
```

This will start the server, and you can access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Running Tests

To run the tests for the API endpoints, execute the following command:

```bash
pytest
```

### Run Everything

To run all scripts and tests in one go, you can use the provided python script `env_setup_run.py`. Ensure the script has execute permissions:

```bash
python env_setup_run.py
```

## API Endpoints

### Get Top N Highest-Paid Employees

- **URL**: `/top-n-highest-paid-employees`
- **Method**: `GET`
- **Query Parameters**: 
  - `n` (integer): Number of top highest-paid employees to retrieve.
- **Response**: JSON list of top N highest-paid employees.

### Get Number of Employees in Department

- **URL**: `/number-of-employees-in-department`
- **Method**: `GET`
- **Query Parameters**: 
  - `department` (string): Department name to retrieve the number of employees.
- **Response**: JSON object with department name and number of employees.