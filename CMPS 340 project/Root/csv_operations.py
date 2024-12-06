#module begins
module_name = 'csv_operations'
'''
Version: 1.0

Description:
    This module contains functions for visualization and searching of CSV files.

Authors:
    Drew Hutchinson, Rex Liner

Date Created     :  11-11-2024
Date Last Updated:  12-5-2024

Doc:
    Uses pandas, seaborn, and matplotlib

Notes:
    
'''

#imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#custom imports
import config

class csv_operations_primary:
    #store config into a dictionary, make a histogram for distributions and a line plot for numerical data, and query data for searching
    config = {
        'file_name': config.file_name,
        'secondcol': config.secondcol,
        'column': config.column,
        'search_vallue': config.column,
    }
    def update_config(self, file_name=None, column=None, secondcol=None, search_value=None):
        if file_name is not None:
            self.config['file_name'] = file_name
        if secondcol is not None:
            self.config['secondcol'] = secondcol
        if column is not None:
            self.config['column'] = column
        if search_value is not None:
            self.config['search_value'] = search_value
        return config
    #
    def __init__(self):
        self.file_name = self.config['file_name']
        self.data = pd.read_csv(f'./Input/{self.file_name}')
    #
    def histogram(self):
        sns.histplot(x=self.config['column'], data=self.data[[self.config['column']]])
        plt.show()
    #
    def line_plot(self):
        sns.lineplot(x=self.config['column'], y=self.config['secondcol'], data=self.data)
        plt.show()
    #
    def search(self):
            result = self.data[self.data[self.config['column']] == int(self.config['search_value'])]
            print(result)
    #
#

class csv_operations_secondary(csv_operations_primary):
    def __init__(self):
        super().__init__()
        self.data = pd.read_csv(f'./Input/{self.config['file_name']}')
    #
    def Violin(self):
        sns.violinplot(x=self.config['column'], data=self.data[[self.config['column']]])
        plt.show()
    #
    def Whisker_Box(self):
        sns.boxplot(x=self.config['column'], data=self.data[[self.config['column']]])
        plt.show()
    #
    def Scatter(self):
        sns.scatterplot(x=self.config['column'], y=self.config['secondcol'], data=self.data)
        plt.show()
    #
#    

def main(file_name=None, column=None, secondcol=None, search_value=None):
    primary = csv_operations_primary()
    secondary = csv_operations_secondary()
    primary.update_config(file_name, column, secondcol, search_value)
    primary.histogram()
    secondary.Violin()
    secondary.Whisker_Box()
    if secondcol != None:
        secondary.Scatter()
        primary.line_plot()
    #
    if search_value != None:
        primary.search()
    #
#


if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
#