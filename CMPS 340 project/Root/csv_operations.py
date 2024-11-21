#module begins
module_name = 'csv_operations'
'''
Version: 1.0

Description:
    This module contains functions for visualization and searching of CSV files.

Authors:
    Drew Hutchinson, Rex Liner

Date Created     :  11-11-2024
Date Last Updated:  11-20-2024

Doc:
    Uses pandas, seaborn, and matplotlib

Notes:
    
'''

#imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#custom imports


class csv_operations:
    #store config into a dictionary, make a histogram for distributions and a line plot for numerical data, and query data for searching
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = pd.read_csv(f'./Input/{self.file_name}')
    #
    def histogram(self, column):
        sns.histplot(x=column, data=self.data[[column]])
        plt.show()
    #
    def search(self, column, search_value):
        print(self.data[self.data[column] == int(search_value)])
    #
#
class csv_operations_child(csv_operations):
    def __init__(self, file_name=None):
        super().__init__(file_name)
        self.data = pd.read_csv(f'./Input/{self.file_name}')
    #
    def Violin(self, column):
        sns.violinplot(x=column, data=self.data[[column]])
        plt.show()
    #
    def Whisker_Box(self, column):
        sns.boxplot(x=column, data=self.data[[column]])
        plt.show()
    #
    def Scatter(self, column, column2=None):
        sns.scatterplot(x=column, y=column2, data=self.data)
        plt.show()
    #
#    

def main(config):
    parent = csv_operations(config.file_name)
    child = csv_operations_child(config.file_name)
    parent.histogram(config.column)
    child.Violin(config.column)
    child.Whisker_Box(config.column)
    if config.secondcol != None:
        child.Scatter(config.column, config.secondcol)
    #
    if config.search_value != None:
        parent.search(config.column, config.search_value)
    #
#


if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
#