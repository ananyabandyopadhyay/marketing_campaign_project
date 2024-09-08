# feature_engineering.py

import pandas as pd

def create_features(data):
    """
    Create new features such as total children, total spending, and age.
    """
    # Create a feature for total number of children
    data['Total_Children'] = data['Kidhome'] + data['Teenhome']
    
    # Create a feature for customer's age (assuming 'Year_Birth' is available)
    current_year = pd.to_datetime('today').year
    data['Age'] = current_year - data['Year_Birth']
    
    # Create a feature for total spending (sum of various spending categories)
    spending_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    data['Total_Spending'] = data[spending_columns].sum(axis=1)
    
    # Create a feature for total purchases across three channels
    purchase_columns = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
    data['Total_Purchases'] = data[purchase_columns].sum(axis=1)
    
    return data
