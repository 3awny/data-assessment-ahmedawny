#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo -e "\nSetting up virtual environment"

# Check if virtual environment directory exists
if [ ! -d "venv" ]; then
  echo -e "\nCreating virtual environment..."
  python3.10 -m venv venv
else
  echo -e "\nVirtual environment already exists. Skipping creation."
fi

# Activate the virtual environment
source venv/bin/activate
echo -e "\nVirtual environment activated."

# Get the site-packages directory of the virtual environment
SITE_PACKAGES_DIR=$(python -c "import site; print(site.getsitepackages()[0])")

# Define the path to the .pth file
PTH_FILE_PATH="$SITE_PACKAGES_DIR/myproject.pth"

# Automatically determine the project root directory
PROJECT_ROOT_DIR=$(pwd)

# Create the .pth file and add the project root directory to it
echo $PROJECT_ROOT_DIR > $PTH_FILE_PATH

# Print a confirmation message
echo "Added $PROJECT_ROOT_DIR to $PTH_FILE_PATH"
echo -e "\nProject root directory added to site-packages."

# Step 1: Install dependencies
echo -e "\nStep 1: Installing dependencies..."
pip install -r requirements.txt
echo -e "\nDependencies installed."

# Step 2: Clean the data
echo -e "\nStep 2: Cleaning data..."
python scripts/clean_data.py
echo -e "\nData cleaned."

# Step 3: Analyze the data
echo -e "\nStep 3: Analyzing data..."
python scripts/analyze_data.py
echo -e "\nData analysis completed."

# Step 4: Perform regression analysis
echo -e "\nStep 4: Performing regression analysis..."
python scripts/linear_regression.py
echo -e "\nRegression analysis completed."

# Uncomment the following lines to run the FastAPI application in the background
# Step 5: Run FastAPI application (in the background)
# echo -e "\nStep 5: Starting FastAPI application..."
# uvicorn app.main:app --reload &

# Step 6: Run tests
echo -e "\nStep 6: Running tests..."
pytest
echo -e "\nTests completed."

# Deactivate the virtual environment
deactivate
echo -e "\nVirtual environment deactivated."

echo -e "\nAll tasks completed!"
