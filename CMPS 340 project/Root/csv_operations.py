#module begins
module_name = 'csv_operations'

#imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#custom imports
import config

class csv_operations:
    def __init__(self, file_name=None):
        self.file_name = file_name

class csv_operations_child(csv_operations):
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
    child = csv_operations_child(config.file_name)
    print(child.data)

    print("How would you like to graph this data.")
    print("1. Violin Plot")
    print("2. Whisker box plot")
    print("3. Scatter plot")
    choice = input()
    
    if (choice == '1'):
        print("Now input the name of the column that you would like to graph.")
        column = input()
        child.Violin(column)

if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()