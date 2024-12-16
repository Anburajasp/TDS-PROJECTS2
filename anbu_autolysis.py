# -*- coding: utf-8 -*-
"""Anbu_autolysis.py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RFuBlRjTUL6xzzwrRtu8sLvV0jXHZwCO
"""

# prompt: read 3 csv files namely goodreads.csv, happiness.csv and media.csv from a google drive folder and read it in difference data frame

import pandas as pd

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Define the folder path in Google Drive
folder_path = '/content/drive/My Drive/TDS/Project 2 data'  # Replace 'your_folder_name' with the actual folder name

# Read the CSV files into separate dataframes
try:
  goodreads_df = pd.read_csv(f'{folder_path}/goodreads.csv')
  happiness_df = pd.read_csv(f'{folder_path}/happiness.csv')
  media_df = pd.read_csv(f'{folder_path}/media.csv')

  print("goodreads.csv loaded successfully.")
  print("happiness.csv loaded successfully.")
  print("media.csv loaded successfully.")
except FileNotFoundError:
  print("Error: One or more CSV files not found in the specified folder.")
except pd.errors.EmptyDataError:
  print("Error: One or more CSV files are empty.")
except pd.errors.ParserError:
  print("Error: One or more CSV files could not be parsed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")