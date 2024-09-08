# data_preprocessing.py

import pandas as pd

def load_and_clean_data(file_path):
    """
    Loads the data from the specified CSV file and performs initial cleaning.
    """
    # Load data
    data = pd.read_csv(file_path)
    
    # Remove currency symbols and convert 'Income' to numeric
    data['Income'] = data[' Income '].replace({'$': '', ',': ''}, regex=True)
    data['Income'] = pd.to_numeric(data['Income'], errors='coerce')
    
    # Convert 'Dt_Customer' to datetime format
    data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'], format='%m/%d/%y')
    
    # Clean 'Education' column (e.g., remove leading/trailing spaces)
    data['Education'] = data['Education'].str.strip()
    
    # Clean 'Marital_Status' column
    data['Marital_Status'] = data['Marital_Status'].str.strip()
    
    # Handle missing values in 'Income'
    data['Income'] = data.groupby(['Education', 'Marital_Status'])['Income'].transform(lambda x: x.fillna(x.mean()))
    
    # If any 'Income' values are still missing, fill them with the overall mean
    data['Income'] = data['Income'].fillna(data['Income'].mean())
    
    # Return the cleaned DataFrame
    return data
