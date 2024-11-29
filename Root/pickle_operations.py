#Version: v1.3
#Date Last Updated: 11-29-2024

#%% MODULE BEGINS
module_name = 'pickle_operations'

'''
Version: 1.0

Description:
    A module for performing operations on data loaded from a pickle file.
    Includes calculations for joint counts, probabilities, vector operations,
    and categorical analysis.

Authors:
    Rex Liner, Drew Hutchinson

Date Created     :  11-27-2024
Date Last Updated:  11-29-2024

Doc:
    Uses pandas, numpy, itertools, math, and matplotlib.

Notes:
    Ensures compatibility with configuration constants for flexible use.
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    #os.chdir("./../..")
#

# Custom imports
from pickle_calculations import pickle_calculations

# Other imports
import itertools
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CONFIG_gl = {
    "pickle_file": "./Input/data.pkl",  # Path to the pickle file
    "categorical_column": "category_col",  # Categorical column name
    "numeric_columns": ["x", "y"],  # Numeric column names
    "output_dir": "./Output",  # Directory for saving outputs
}  #

#%% CLASS DEFINITIONS           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class pickle_operations(pickle_calculations):
    def __init__(self, config):
        """Initialize the class with configuration constants."""
        super().__init__(config)  #

    def calculate_joint_counts(self, column1, column2):
        """Calculate joint counts of two columns."""
        counts = pd.crosstab(self.data[column1], self.data[column2])  #
        print(f"Joint Counts:\n{counts}")  #
        return counts  #

    def calculate_joint_probabilities(self, column1, column2):
        """Calculate joint probabilities of two columns."""
        counts = self.calculate_joint_counts(column1, column2)  #
        probabilities = counts / counts.sum().sum()  #
        print(f"Joint Probabilities:\n{probabilities}")  #
        return probabilities  #

    def calculate_conditional_probabilities(self, column1, column2):
        """Calculate conditional probabilities P(column1|column2)."""
        counts = self.calculate_joint_counts(column1, column2)  #
        probabilities = counts.div(counts.sum(axis=0), axis=1)  #
        print(f"Conditional Probabilities:\n{probabilities}")  #
        return probabilities  #

    def vector_operations(self, column1, column2):
        """Perform vector operations between two numeric columns."""
        vector1 = self.data[column1].to_numpy()  #
        vector2 = self.data[column2].to_numpy()  #
        dot_product = np.dot(vector1, vector2)  #
        magnitude1 = np.linalg.norm(vector1)  #
        magnitude2 = np.linalg.norm(vector2)  #
        unit_vector1 = vector1 / magnitude1  #
        unit_vector2 = vector2 / magnitude2  #
        projection_vector = (dot_product / np.dot(vector2, vector2)) * vector2  #
        angle = math.acos(dot_product / (magnitude1 * magnitude2)) * (180 / np.pi)  #
        orthogonal = np.isclose(dot_product, 0)  #

        print(f"Vector Operations:\n"
              f"Dot Product: {dot_product}\n"
              f"Projection Vector: {projection_vector}\n"
              f"Angle: {angle:.2f} degrees\n"
              f"Orthogonal: {orthogonal}")  #

        return {
            "dot_product": dot_product,
            "projection_vector": projection_vector,
            "angle": angle,
            "orthogonal": orthogonal,
            "unit_vector1": unit_vector1,
            "unit_vector2": unit_vector2,
        }  #

    def analyze_categorical(self, column):
        """Analyze a categorical column for unique values, permutations, and combinations."""
        unique_values = self.data[column].unique()  #
        permutations = list(itertools.permutations(unique_values, 2))  #
        combinations = list(itertools.combinations(unique_values, 2))  #

        print(f"Unique Values: {unique_values}")  #
        print(f"Permutations (2): {len(permutations)} total")  #
        print(f"Combinations (2): {len(combinations)} total")  #

        return {
            "unique_values": unique_values,
            "permutations": permutations,
            "combinations": combinations,
        }  #

    def export_vector_operations(self, filename, results):
        """Export vector operations to a text file."""
        if not os.path.exists(self.config["output_dir"]):
            os.makedirs(self.config["output_dir"])  #
        path = os.path.join(self.config["output_dir"], filename)  #
        with open(path, 'w') as f:
            for key, value in results.items():
                f.write(f"{key}: {value}\n")  #
        print(f"Vector operations exported to {path}.")  #

    def export_probabilities(self, filename, probabilities):
        """Export probabilities to a CSV file."""
        if not os.path.exists(self.config["output_dir"]):
            os.makedirs(self.config["output_dir"])  #
        path = os.path.join(self.config["output_dir"], filename)  #
        probabilities.to_csv(path)  #
        print(f"Probabilities exported to {path}.")  #

    def visualize_column(self, column):
        """Visualize the data distribution for a numeric column."""
        if column not in self.data.columns:
            raise KeyError(f"Column '{column}' not found in the dataset.")  #
        plt.hist(self.data[column].dropna(), bins=20, color='blue', alpha=0.7)  #
        plt.title(f"Histogram for {column}")  #
        plt.xlabel(column)  #
        plt.ylabel("Frequency")  #
        plt.grid(True)  #
        plt.show()  #
        print(f"Visualization for column '{column}' displayed.")  #

#%% MAIN FUNCTION DEFINITIONS   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """Main function to demonstrate module functionality."""
    print(f"\"{CONFIG_gl['pickle_file']}\" analysis begins.")  #

    # Initialize operations
    child = pickle_operations(CONFIG_gl)  #

    # Statistics
    child.calculate_statistics(CONFIG_gl["numeric_columns"][0])  #

    # Probability calculations
    joint_counts = child.calculate_joint_counts(CONFIG_gl["numeric_columns"][0], CONFIG_gl["numeric_columns"][1])  #
    child.export_probabilities("joint_counts.csv", joint_counts)  #

    joint_probabilities = child.calculate_joint_probabilities(CONFIG_gl["numeric_columns"][0], CONFIG_gl["numeric_columns"][1])  #
    child.export_probabilities("joint_probabilities.csv", joint_probabilities)  #

    conditional_probabilities = child.calculate_conditional_probabilities(CONFIG_gl["numeric_columns"][0], CONFIG_gl["numeric_columns"][1])  #
    child.export_probabilities("conditional_probabilities.csv", conditional_probabilities)  #

    # Vector operations
    vector_results = child.vector_operations(CONFIG_gl["numeric_columns"][0], CONFIG_gl["numeric_columns"][1])  #
    child.export_vector_operations("vector_operations.txt", vector_results)  #

    # Categorical analysis
    child.analyze_categorical(CONFIG_gl["categorical_column"])  #

    # Visualization
    child.visualize_column(CONFIG_gl["numeric_columns"][0])  #

#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")  #
    main()  #


