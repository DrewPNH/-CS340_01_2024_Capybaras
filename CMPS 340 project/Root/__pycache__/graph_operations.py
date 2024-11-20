#module begins
module_name = 'graph_passenger'

'''
Version: 1.0

Description:
    This is the child class for csv_operations, where the user chooses how to plot their data
    and have the graoh displayed

Authors:
    Drew Hutchinson, Rex Liner

Date Created     :  11-11-2024
Date Last Updated:  11-13-2024

Doc:
    Uses pandas, seaborn, and matplotlib

Notes:
    The uses will enter 1, 2, or 3 for the type of graph they want their data displayed on
    The user will then input the name they want for their column
'''

#imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from csv_operations import csv_operations

class child_age:
    def __init__(self, file_name=None):
        self.file_name = file_name

class child_age(passenger):
    def __init__(self, file_name=None):
        super().__init__(file_name)
        self.data = pd.read_csv(f'./Input/{self.file_name}')

    def Violin(self, column):
        sns.violinplot(x=column, data=self.data[[column]])
        plt.show()
    def Whisker_Box(self, column):
        sns.boxplot(x=column, data=self.data[column])
        plt.show()
    def Scatter(self, column):
        sns.scatterplot(x=column, data=self.data[column])
        plt.show()
        

def main():
    child = child_age(config.file_name)
    print(child.data)

    print("How would you like to graph this data.")
    print("1. Violin Plot")
    print("2. Whisker box plot")
    print("3. Scatter plot")
    choice = input()
    
    if choice == '1':
        print("Now input the name of the column that you would like to graph.")
        column = input()
        child.Violin(column)

    elif choice == '2':
        print("Now input the name of the column that you would like to graph.")
        column = input()
        child.Whisker_Box(column)

    elif choice == '3':
        print("Now input the name of the column that you would like to graph.")
        column = input()
        child.Scatter(column)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()