module_name = 'pickle_operations'
'''
Version: 1.0

Description:
    This module contains functions for visualization and searching of pickle files.

Authors:
    Drew Hutchinson, Rex Liner

Date Created     :  11-29-2024
Date Last Updated:  12-5-2024
'''

#imports
import pickle
import numpy as np
import itertools
import matplotlib.pyplot as plt
import os
import pandas as pd

#custom imports
import config

class DataAnalysis:
    CONFIG = {
        "pickle_file_path": config.pickle_name,
        "visualization": config.pickle_visualization,
    }

    def update_config(self, pickle_name=None, visualization=None):
        if pickle_name is not None:
            self.CONFIG['pickle_file_path'] = pickle_name
        #
        if visualization is not None:
            self.CONFIG['visualization'] = visualization
        #
    #
    
    def __init__(self, *arg):
        self.data = arg or []
    #
    
    def load_data(self):
        try:
            with open(self.CONFIG['pickle_file_path'], 'rb') as file:
                self.data = pickle.load(file)
                print("Data successfully loaded from pickle file.")
            #
        #
        except Exception as e:
            print(f"Error loading data: {e}")
        #
    #
    
    def calculate_statistics(self):
        if not self.data.empty: 
            print("No data to calculate statistics.")
            return None 
        #
        
        data_array = np.array(self.data)
        mean = np.mean(data_array)
        median = np.median(data_array)
        std = np.std(data_array)
        print(f"Mean: {mean}, Median: {median}, Std: {std}")
        return mean, median, std
    #
    
    def visualize_data(self):
        if self.CONFIG['visualization']:
            if not self.data.empty:
                print("No data to visualize.")
                return
            #
            plt.hist(self.data, bins=30, alpha=0.7, color='blue')
            plt.title("Data Visualization")
            plt.xlabel("Value")
            plt.ylabel("Frequency")
            plt.show()
        #
        else:
            print("Visualization is disabled in configuration.")
        #
    #
#

class AdvancedAnalysis(DataAnalysis):
    def __init__(self, data=None):
        super().__init__(data)
    #
    
    def calculate_joint_counts(self, data1, data2):
        joint_counts = {}
        for val1, val2 in zip(data1, data2):
            if (val1, val2) not in joint_counts:
                joint_counts[(val1, val2)] = 0
            #
            joint_counts[(val1, val2)] += 1
        #
        print(f"Joint Counts: {joint_counts}")
        return joint_counts
    #
    
    def calculate_joint_probabilities(self, joint_counts, total):
        joint_probs = {key: count / total for key, count in joint_counts.items()}
        print(f"Joint Probabilities: {joint_probs}")
        return joint_probs
    #
    
    def calculate_conditional_probability(self, joint_counts, marginal_counts, event):
        joint_count = joint_counts.get(event, 0)
        marginal_count = marginal_counts.get(event[1], 0)
        if marginal_count == 0:
            print("Error: Marginal count is zero.")
            return 0
        #
        conditional_prob = joint_count / marginal_count
        print(f"Conditional Probability P({event[0]}|{event[1]}): {conditional_prob}")
        return conditional_prob
    #
    
    def calculate_dot_product(self, vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        print(f"Dot Product: {dot_product}")
        return dot_product
    #
    
    def calculate_angle(self, vec1, vec2):
        dot_product = self.calculate_dot_product(vec1, vec2)
        magnitude_v1 = np.linalg.norm(vec1)
        magnitude_v2 = np.linalg.norm(vec2)
        cosine_angle = dot_product / (magnitude_v1 * magnitude_v2)
        angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
        print(f"Angle between vectors: {np.degrees(angle)} degrees")
        return angle
    #
    
    def check_orthogonality(self, vec1, vec2):
        dot_product = self.calculate_dot_product(vec1, vec2)
        if dot_product == 0:
            print("Vectors are orthogonal.")
            return True
        #
        else:
            print("Vectors are not orthogonal.")
            return False
        #
    #
    
    def handle_categorical_data(self, data):
        unique_values = np.unique(data)
        print(f"Unique Values: {unique_values}")
        
        permutations = list(itertools.permutations(unique_values, 2))
        combinations = list(itertools.combinations(unique_values, 2))
        
        print(f"Permutations: {permutations}")
        print(f"Combinations: {combinations}")
        
        return unique_values, permutations, combinations
    #

    def obtain_position_vector(self, coords):
        position_vector = np.array(coords)
        print(f"Position Vector: {position_vector}")
        return position_vector
    #
    
    def obtain_unit_vector(self, vector):
        unit_vector = vector / np.linalg.norm(vector)
        print(f"Unit Vector: {unit_vector}")
        return unit_vector
    #
    
    def obtain_projection_vector(self, vector, onto_vector):
        projection = np.dot(vector, onto_vector) / np.dot(onto_vector, onto_vector) * onto_vector
        print(f"Projection Vector: {projection}")
        return projection
    #
    
    def export_results(self, filename, results):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            for result in results:
                f.write(str(result) + "\n")
            #
        #
        print(f"Results exported to {filename}.")
    #
#

def main(pickle_name=None):
    data_analysis = DataAnalysis()
    data_analysis.update_config(pickle_name)
    data_analysis.load_data()

    stats = data_analysis.calculate_statistics()

    if stats is not None:
        mean, median, std = stats
    #
    else:
        mean, median, std = None, None, None 
    #

    data_analysis.visualize_data()
    
    advanced_analysis = AdvancedAnalysis(data_analysis.data)
    advanced_analysis.load_data()
    

    results = []

    if mean is not None:  
        results.extend([
            f"Mean: {mean}",
            f"Median: {median}",
            f"Std: {std}"
        ])
    #

    if isinstance(data_analysis.data, (list, np.ndarray)):
        if len(data_analysis.data) > 1:
            vector1 = np.array(data_analysis.data[0], dtype=float) 
            vector2 = np.array(data_analysis.data[1], dtype=float) 
            
            dot_product = advanced_analysis.calculate_dot_product(vector1, vector2)
            results.append(f"Dot Product: {dot_product}")
            
            angle = advanced_analysis.calculate_angle(vector1, vector2)
            results.append(f"Angle between vectors: {np.degrees(angle)} degrees")
            
            orthogonality = advanced_analysis.check_orthogonality(vector1, vector2)
            results.append(f"Orthogonality: {orthogonality}")
        #
    #
    
    elif isinstance(data_analysis.data, pd.DataFrame):
        if len(data_analysis.data) > 1:
            numeric_data = data_analysis.data.select_dtypes(include=[np.number])
            
            if numeric_data.shape[0] > 1: 
                vector1 = np.array(numeric_data.iloc[0].values, dtype=float) 
                vector2 = np.array(numeric_data.iloc[1].values, dtype=float) 
                
                dot_product = advanced_analysis.calculate_dot_product(vector1, vector2)
                results.append(f"Dot Product: {dot_product}")
                
                angle = advanced_analysis.calculate_angle(vector1, vector2)
                results.append(f"Angle between vectors: {np.degrees(angle)} degrees")
                
                orthogonality = advanced_analysis.check_orthogonality(vector1, vector2)
                results.append(f"Orthogonality: {orthogonality}")
            #
        #
    #

    if isinstance(data_analysis.data, list):
        categorical_data = [str(item) for item in data_analysis.data if isinstance(item, str)]
        unique_values, permutations, combinations = advanced_analysis.handle_categorical_data(categorical_data)
        
        results.append(f"Unique Values: {unique_values}")
        results.append(f"Permutations: {permutations}")
        results.append(f"Combinations: {combinations}")
    #

    advanced_analysis.export_results("./Output/analysis_results.txt", results)
#


if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
#
