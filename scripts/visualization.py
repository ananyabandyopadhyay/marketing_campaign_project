# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Make sure to save visualizations in the 'results/charts/' folder
CHARTS_DIR = 'results/charts/'

# Create directory if it doesn't exist
if not os.path.exists(CHARTS_DIR):
    os.makedirs(CHARTS_DIR)

def plot_histograms(data):
    """
    Plot histograms of selected numerical features.
    """
    numerical_columns = ['Income', 'Age', 'Total_Spending', 'Total_Purchases', 'Total_Children']
    
    for col in numerical_columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(data[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.savefig(f'{CHARTS_DIR}histogram_{col}.png')
        plt.close()

def plot_boxplots(data):
    """
    Plot boxplots of selected numerical features.
    """
    numerical_columns = ['Income', 'Total_Spending', 'Age', 'Total_Purchases']
    
    for col in numerical_columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=data, y=col)
        plt.title(f'Boxplot of {col}')
        plt.ylabel(col)
        plt.savefig(f'{CHARTS_DIR}boxplot_{col}.png')
        plt.close()

def plot_heatmap(data):
    """
    Plot a heatmap of correlations between features.
    """
    plt.figure(figsize=(12, 8))
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.savefig(f'{CHARTS_DIR}correlation_heatmap.png')
    plt.close()
