#Version: v1.0
#Date Last Updated: 12-20-2023

#%% MODULE BEGINS
module_name = 'csv_operations_primary'

'''
Version: 1.0

Description:
    This module contains functions for visualization and searching of CSV files.
    Includes functionality for histograms, line plots, and search operations.

Authors:
    Drew Hutchinson, Rex Liner

Date Created     :  11-11-2024
Date Last Updated:  11-20-2024

Doc:
    Uses pandas, seaborn, and matplotlib.

Notes:
    Handles data visualization and search operations with user-configured options.
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    #os.chdir("./../..")  # Uncomment if necessary to change the working directory #
#

# Other imports
from matplotlib import pyplot as plt
from pandas import read_csv
from seaborn import histplot
#

#%% CLASS DEFINITIONS           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class csv_operations_primary:
    def __init__(self, file_name):
        """Initialize the class with a CSV file."""
        self.file_name = file_name  #
        print(f"Debug: Looking for file at {self.file_name}")  # Debug print #
        if not os.path.exists(self.file_name):
            raise FileNotFoundError(f"File not found: {self.file_name}")  #
        self.data = read_csv(self.file_name)  # Load the CSV file #

    def histogram(self, column):
        """Plot a histogram for the specified column."""
        if column not in self.data.columns:
            raise KeyError(f"Column '{column}' not found in the dataset.")  #
        histplot(x=column, data=self.data[[column]])  #
        plt.title(f"Histogram for {column}")  #
        plt.xlabel(column)  #
        plt.ylabel("Frequency")  #
        plt.show()  #

    def line_plot(self, column):
        """Plot a line plot for the specified numeric column."""
        if column not in self.data.columns:
            raise KeyError(f"Column '{column}' not found in the dataset.")  #
        if self.data[column].dtype in ["int64", "float64"]:  #
            self.data[column].plot(kind='line', title=f"Line Plot for {column}")  #
            plt.xlabel("Index")  #
            plt.ylabel(column)  #
            plt.show()  #
        else:
            print(f"Column '{column}' is not numeric and cannot be visualized with a line plot.")  #

    def search(self, column, search_value):
        """Query data for rows where the column matches the search value."""
        if column not in self.data.columns:
            raise KeyError(f"Column '{column}' not found in the dataset.")  #
        result = self.data[self.data[column] == search_value]  #
        print(result)  #
        return result  #

    @staticmethod
    def main(config):
        """Static method to execute operations based on a config."""
        try:
            # Initialize object
            csv_ops = csv_operations_primary(config.file_name)  #

            # Visualizations
            csv_ops.histogram(config.column)  #
            csv_ops.line_plot(config.column)  #

            # Search operations
            if config.search_value:
                csv_ops.search(config.column, config.search_value)  #

        except FileNotFoundError as e:
            print(f"Error: {e}")  #
        except KeyError as e:
            print(f"Error: {e}")  #

#%% MAIN FUNCTION DEFINITIONS   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """Main function to test module functionality."""
    print(f"Testing '{module_name}' module.")  #
    # Test with a sample configuration
    from config import config  #
    test_config = config(file_name="./Input/titanic.csv", column="age", search_value=30)  #
    csv_operations_primary.main(test_config)  #

#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")  #
    main()  #



