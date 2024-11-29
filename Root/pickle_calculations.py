#Version: v1.3
#Date Last Updated: 11-29-2024

#%% MODULE BEGINS
module_name = 'pickle_calculations'

'''
Version: 1.0

Description:
    A module to handle calculations and operations on data loaded from a pickle file.
    Includes methods for reading pickle files, calculating statistics, and exporting data.

Authors:
    Rex Liner, Drew Hutchinson

Date Created     :  11-27-2024
Date Last Updated:  11-29-2024

Doc:
    Uses pandas, pickle, and os.

Notes:
    This module ensures flexible configuration and efficient data processing.
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    #os.chdir("./../..")
#

# Other imports
import pandas as pd
import pickle
#

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CONFIG_gl = {
    "pickle_file": "./Input/data.pkl",  # Path to the pickle file
    "output_dir_gl": "./Output",  # Directory for saving outputs
}  #

#%% CLASS DEFINITIONS           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class pickle_calculations:
    def __init__(self, config):
        """Initialize with configuration constants."""
        self.config = config  #
        self.data = self.read_pickle(self.config["pickle_file"])  #

    def read_pickle(self, file_path):
        """Read data from a pickle file."""
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                data = pickle.load(f)  #
            print(f"Data loaded from {file_path}.")  #
            return pd.DataFrame(data)  #
        else:
            raise FileNotFoundError(f"Pickle file {file_path} not found.")  #

    def calculate_statistics(self, column):
        """Calculate mean, median, and standard deviation for a numeric column."""
        stats = {
            "mean": self.data[column].mean(),
            "median": self.data[column].median(),
            "std": self.data[column].std(),
        }  #
        print(f"Statistics for {column}: {stats}")  #
        return stats  #

    def export_csv(self, filename, data):
        """Export data to a CSV file."""
        if not os.path.exists(self.config["output_dir"]):
            os.makedirs(self.config["output_dir"])  #
        path = os.path.join(self.config["output_dir"], filename)  #
        data.to_csv(path, index=False)  #
        print(f"Data exported to {path}.")  #

#%% FUNCTION DEFINITIONS        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """Main function to demonstrate module functionality."""
    print("Running pickle_calculations as a standalone script.")  #

    # Example usage of pickle_calculations
    config = CONFIG_gl  #
    parent = pickle_calculations(config)  #

    # Example: calculate statistics for a sample column
    try:
        parent.calculate_statistics("sample_column")  #
    except KeyError:
        print("The column 'sample_column' does not exist in the dataset.")  #

    # Example: export a CSV (adjust 'data' as needed)
    # parent.export_csv("exported_data.csv", parent.data)  #

#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")  #
    main()  #

