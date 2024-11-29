#%% MODULE BEGINS
module_name = 'main'

'''
Version: 1.0

Description:
    This script serves as the main entry point for performing operations using 
    csv_operations_primary, csv_operations_secondary, pickle_calculations, and pickle_operations modules.

Authors:
    Drew Hutchinson, Rex Liner

Date Created     :  11-6-2024
Date Last Updated:  11-29-2024

Doc:
    Handles configuration management, user interaction, and invokes appropriate operations.

Notes:
    Modularized to allow flexible user configuration or default execution.
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    #os.chdir("./../..")  # Uncomment if necessary to change the working directory #
#

# Custom imports
from csv_operations_primary import csv_operations_primary
from csv_operations_secondary import csv_operations_secondary
from pickle_calculations import pickle_calculations
from pickle_operations import pickle_operations

# Other imports
import logging
#

#%% CLASS DEFINITIONS           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class config:
    def __init__(self, file_name="titanic.csv", column="age", secondcol=None, search_value=None):
        """Initialize configuration constants."""
        self.file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "Input", file_name))  #
        self.column = column  #
        self.secondcol = secondcol  #
        self.search_value = search_value  #

        # Debugging the resolved path
        print(f"Resolved file path: {self.file_name}")  #

        # Check if the file exists
        if not os.path.exists(self.file_name):
            raise FileNotFoundError(f"File not found: {self.file_name}")  #

#%% FUNCTION DEFINITIONS        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """Main function to execute operations."""
    # Ensure the Output directory exists
    output_dir = './Output'  #
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  #

    # Logging setup
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(os.path.join(output_dir, 'log.txt'))])  #

    print("Would you like to change the config? (Y/N)")  #
    choice = input().strip()  #

    if choice.upper() == 'Y':
        # User-configured operations
        print("What is the file that you would like to read data from?")  #
        file_name = input().strip()  #
        print("What column would you like to visualize?")  #
        column = input().strip()  #
        print("Would you like to compare this column in a scatter plot? (Y/N)")  #
        compare = input().strip()  #
        column2 = None  #
        if compare.upper() == 'Y':
            print("What is the second column that you'd like to include in the graph?")  #
            column2 = input().strip()  #

        updatedConfig = config(file_name=file_name, column=column, secondcol=column2)  #

        print("Would you like to search this data? (Y/N)")  #
        searchchoice = input().strip()  #
        if searchchoice.upper() == 'Y':
            print("What is the value that you'd like to search for?")  #
            search_value = input().strip()  #
            updatedConfig.search_value = search_value  #

        # Run csv_operations_primary
        csv_operations_primary.main(updatedConfig)  #

        # Run csv_operations_secondary
        print("Running secondary operations.")  #
        secondary_ops = csv_operations_secondary(updatedConfig.file_name)  #
        secondary_ops.Violin(updatedConfig.column)  #
        secondary_ops.Whisker_Box(updatedConfig.column)  #
        if updatedConfig.secondcol:
            secondary_ops.Scatter(updatedConfig.column, updatedConfig.secondcol)  #

        # Run pickle_operations
        print("Would you like to process a pickle file? (Y/N)")  #
        pickle_choice = input().strip()  #
        if pickle_choice.upper() == 'Y':
            print("What is the pickle file that you would like to read data from?")  #
            pickle_file = input().strip()  #
            pickle_config = {
                "pickle_file": os.path.abspath(os.path.join(os.path.dirname(__file__), "Input", pickle_file)),
                "output_dir": output_dir,
            }  #
            print("Initializing pickle_operations...")  #
            child = pickle_operations(pickle_config)  #

            # Vector operations
            numeric_columns = input("Enter two numeric columns for vector operations, separated by a comma: ").split(",")  #
            if len(numeric_columns) == 2:
                child.vector_operations(numeric_columns[0].strip(), numeric_columns[1].strip())  #

            # Probability calculations
            prob_choice = input("Would you like to calculate joint/conditional probabilities? (Y/N): ").strip()  #
            if prob_choice.upper() == 'Y':
                child.calculate_joint_counts(numeric_columns[0].strip(), numeric_columns[1].strip())  #
                child.calculate_joint_probabilities(numeric_columns[0].strip(), numeric_columns[1].strip())  #
                child.calculate_conditional_probabilities(numeric_columns[0].strip(), numeric_columns[1].strip())  #

            # Categorical analysis
            cat_column = input("Enter the name of the categorical column to analyze: ").strip()  #
            child.analyze_categorical(cat_column)  #

            # Export vector operations
            export_choice = input("Would you like to export vector operations to a file? (Y/N): ").strip()  #
            if export_choice.upper() == 'Y':
                export_file = input("Enter the filename for export (e.g., vector_operations.txt): ").strip()  #
                child.export_vector_operations(export_file, {})  #

    elif choice.upper() == 'N':
        # Default operations
        defaultConfig = config(file_name="titanic.csv", column="age", search_value=2)  #
        csv_operations_primary.main(defaultConfig)  #

        print("Running default secondary operations.")  #
        secondary_ops = csv_operations_secondary(defaultConfig.file_name)  #
        secondary_ops.Violin(defaultConfig.column)  #
        secondary_ops.Whisker_Box(defaultConfig.column)  #
        if defaultConfig.secondcol:
            secondary_ops.Scatter(defaultConfig.column, defaultConfig.secondcol)  #

        # Default pickle operations
        default_pickle_config = {
            "pickle_file": os.path.abspath(os.path.join(os.path.dirname(__file__), "Input", "data.pkl")),
            "output_dir": output_dir,
        }  #
        print("Running default operations for pickle file.")  #
        try:
            child = pickle_operations(default_pickle_config)  #
            child.calculate_statistics("sample_column")  #
        except FileNotFoundError as e:
            print(f"Error: {e}")  #
        except KeyError as e:
            print(f"Error: {e}")  #
    else:
        print("Invalid choice. Please restart and select Y or N.")  #

#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")  #
    main()  #






