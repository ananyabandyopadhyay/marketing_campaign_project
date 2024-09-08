# main.py

import pandas as pd
from scripts import data_preprocessing, feature_engineering, visualization

def main():
    # Load and clean data
    data = data_preprocessing.load_and_clean_data("data/marketing_data.csv")
    
    # Perform feature engineering
    data = feature_engineering.create_features(data)
    
    # Generate visualizations
    visualization.plot_histograms(data)

if __name__ == "__main__":
    main()
