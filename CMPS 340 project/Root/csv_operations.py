#module begins
module_name = 'passenger'

'''
Version: 1.0

Description:
    This is the parent class for passenger, where the data is imported

Authors:
    Drew Hutchinson, Rex Liner

Date Created     :  11-11-2024
Date Last Updated:  11-13-2024

Doc:
    Uses pandas, seaborn, and matplotlib

Notes:
    This is only for inputting/importing data
'''

#imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class passenger:
    def __init__(self, file_name=None):
        self.file_name = file_name  
        self.data_df = None  
        #Initialize with file name.

    def load_data(self):
        
        if self.file_name:
            try:
               
                self.data_df = pd.read_csv(f'./Input/{self.file_name}')
                print(f"Data loaded successfully from {self.file_name}")
            except FileNotFoundError:
                print("File not found. Please verify the file path.")
        else:
            print("No file name provided.")
            #Load data from CSV to DataFrame.

if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()