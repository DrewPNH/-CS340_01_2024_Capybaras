#%% MODULE BEGINS
module_name = 'csv_operations_secondary'

'''
Version: 1.2

Description:
    This module contains functions for visualization and querying of CSV files,
    following performance and safety coding standards.

Authors:
    Drew Hutchinson, Rex Liner

Date Created     :  11-11-2024
Date Last Updated:  11-27-2024

Doc:
    Adheres to efficient and safe coding practices with structured formatting.

Notes:
    Includes functionality for visualizations, dynamic queries, and generating data.
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    # os.chdir("./../..")  # Uncomment if necessary to change working directory #
#

# Custom imports
from csv_operations_primary import csv_operations_primary  

# Other imports
from matplotlib import pyplot as plt
from numpy import random as np_random
from pandas import DataFrame
from seaborn import violinplot, boxplot, scatterplot
from copy import deepcopy as dpcpy  # Import only required components #

#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# User Interface variable declarations start here #

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CONFIG_gl = {
    "file_name_gl": "./data/titanic.csv",  # Relative path to CSV file #
    "visualization_column_gl": "age",  # Column for visualizations #
    "scatter_x_gl": "age",  # X-axis column for scatter plot #
    "scatter_y_gl": "fare",  # Y-axis column for scatter plot #
    "search_column_gl": "sex",  # Column for searching #
    "search_values_gl": ["male", "female"],  # Values to search in the column #
    "output_dir_gl": "./output",  # Directory for saving outputs #
}  #

#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Configuration-related code starts here #

#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Initialization of variables and structures #

#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Global declarations start here #

# Class definitions start here #
class csv_operations_secondary(csv_operations_primary):
    def __init__(self, file_name=None):
        """Initialize with a CSV file name."""
        super().__init__(file_name)  # Initialize parent class #
        self._internal_data = None  # Private-like variable for internal processing #

    def Violin(self, column, **kwargs):
        """Plot a violin plot for the specified column."""
        violinplot(x=column, data=self.data[[column]], **kwargs)  # Create the plot #
        plt.title(f"Violin Plot for {column}")  # Add title #
        plt.xlabel(column)  # Add x-axis label #
        plt.show()  # Display plot #

    def Whisker_Box(self, column, *args, title="Whisker-Box Plot", **kwargs):
        """Plot a whisker-box plot for the specified column."""
        boxplot(x=column, data=self.data[[column]], *args, **kwargs)  # Create the plot #
        plt.title(title)  # Add title #
        plt.xlabel(column)  # Add x-axis label #
        plt.show()  # Display plot #

    def Scatter(self, x_col, y_col, marker="o", **kwargs):
        """Plot a scatter plot for two specified columns."""
        scatterplot(x=x_col, y=y_col, data=self.data, marker=marker, **kwargs)  # Create the plot #
        plt.title(f"Scatter Plot: {x_col} vs {y_col}")  # Add title #
        plt.xlabel(x_col)  # Add x-axis label #
        plt.ylabel(y_col)  # Add y-axis label #
        plt.legend(["Data Points"], loc="best")  # Add legend #
        plt.show()  # Display plot #

    def search(self, column, values):
        """Query data for rows where the column matches any of the specified values."""
        result = self.data[self.data[column].isin(values)]  # Boolean indexing #
        print(result)  # Display the result #
        return result  # Return the result #

    def generate_dataframe(self, rows, cols):
        """Generate an mxn Numpy array and write it into a DataFrame."""
        arr = np_random.randint(1, 100, size=(rows, cols))  # Generate random integers #
        df = DataFrame(arr, columns=[f"col_{i+1}" for i in range(cols)])  # Convert to DataFrame #
        print(df)  # Display the DataFrame #
        return df  # Return the DataFrame #

# Function definitions start here #
def main():
    """Main function to execute module operations."""
    csv_ops = csv_operations_secondary(CONFIG_gl["file_name_gl"])  # Initialize object #

    # Visualizations #
    csv_ops.Violin(CONFIG_gl["visualization_column_gl"])  #
    csv_ops.Whisker_Box(CONFIG_gl["visualization_column_gl"])  #
    csv_ops.Scatter(CONFIG_gl["scatter_x_gl"], CONFIG_gl["scatter_y_gl"])  #

    # Query operations #
    csv_ops.search(CONFIG_gl["search_column_gl"], CONFIG_gl["search_values_gl"])  #

    # Generate DataFrame from random Numpy array #
    csv_ops.generate_dataframe(5, 3)  #
#

#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code execution #
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")  # Display module initialization #
    main()  # Run the main function #


