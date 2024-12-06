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
'''
#imports
import logging

#custom imports
import csv_operations
import pickle_operations



print("Would you like to change the config? (Y/N)")
choice = input()
if choice.upper() == 'Y':
    __file_name=None
    column=None
    secondcol = None
    search_value=None
    #change the config through a series of prompts
    print("What is the csv file that you would like to read data from?")
    __file_name = input()
    print("What column would you like to visualize?")
    column = input()
    print("Would you like to compare this column in a scatter plot and line graph? (Y/N)")
    compare = input()
    if compare.upper() == 'Y':
        print("What is the second column that you'd like to include in the graph?")
        secondcol = input()
    #
    print("Would you like to search this data? (Y/N)")
    searchchoice = input()
    if searchchoice.upper() == 'Y':
        print("What is the value that you'd like to search for?")
        search_value = input()
    #
    print("Would you like to change the pickle file being read? (Y/N)")
    change_pickle = input()
    if change_pickle.upper() == 'Y':
        print("What is the new pickle file that you'd like to read from?")
        pickle_name = input()
    #
    csv_operations.main(__file_name, column, secondcol, search_value)
    pickle_operations.main(pickle_name)

#

if choice.upper() == 'N':
    #run the modules with default config
    csv_operations.main()
    pickle_operations.main()
#

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler('./Output/log.txt')])