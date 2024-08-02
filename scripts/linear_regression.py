import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import io
import os

print("Linear Regression Analysis Script is Starting...")  # Initial debug statement

def load_data():
    # Load sample dataset from a multi-line string
    data = """
    Size,Bedrooms,Location,Price
    2000,3,Urban,500000
    1500,2,Suburban,350000
    2500,4,Urban,750000
    1800,3,Rural,200000
    2200,3,Suburban,450000
    1600,2,Urban,400000
    2400,4,Rural,300000
    1900,3,Urban,520000
    1700,2,Suburban,370000
    2300,4,Urban,680000
    2100,3,Suburban,490000
    1550,2,Rural,220000
    2600,5,Urban,800000
    1750,3,Suburban,410000
    2000,3,Rural,280000
    1650,2,Urban,390000
    2450,4,Suburban,610000
    1850,3,Rural,240000
    1700,2,Urban,370000
    2250,4,Suburban,640000
    """
    # Read the dataset into a pandas DataFrame
    df = pd.read_csv(io.StringIO(data))
    return df

def preprocess_data(df):
    # Convert categorical 'Location' column into dummy/indicator variables
    df = pd.get_dummies(df, columns=['Location'], drop_first=True)
    # Split the dataset into features (X) and target (y)
    X = df.drop('Price', axis=1)
    y = df['Price']
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    # Split the data into training and test sets
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    # Make predictions using the test set
    y_pred = model.predict(X_test)
    # Calculate mean squared error
    mse = mean_squared_error(y_test, y_pred)
    # Calculate R-squared score
    r2 = r2_score(y_test, y_pred)
    return mse, r2, y_pred

def visualize_results(y_test, y_pred, directory='graph_plots', file_name='actual_vs_predicted.png'):
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Ensure the directory exists
    save_dir = os.path.join(current_dir, directory)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Full path to save the file
    file_path = os.path.join(save_dir, file_name)
    
    # Plot actual vs predicted prices
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted Prices")
    plt.savefig(file_path)  # Save the plot as an image file
    print(f"Plot saved as {file_path}")
    plt.close()  # Close the plot to free memory

def main():
    # Main function to run the entire process
    df = load_data()
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    mse, r2, y_pred = evaluate_model(model, X_test, y_test)
    
    # Print evaluation metrics
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
    
    # Print model coefficients
    coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
    print(coefficients)

    # Visualize the results
    visualize_results(y_test, y_pred)

if __name__ == "__main__":
    main()  # Execute the main function
