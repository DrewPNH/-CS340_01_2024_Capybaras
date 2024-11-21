import csv_operations
import config
import logging


print("Would you like to change the config? (Y/N)")
choice = input()
if choice.upper() == 'Y':
    #change the config through a series of prompts
    print("What is the file that you would like to read data from?")
    file_name = input()
    print("What column would you like to visualize?")
    column = input()
    print("Would you like to compare this column in a scatter plot? (Y/N)")
    compare = input()
    if compare.upper() == 'Y':
        print("What is the second column that you'd like to include in the graph?")
        column2 = input()
        updatedConfig = config.config(file_name=file_name, column=column, secondcol=column2)
    #
    else:
        updatedConfig = config.config(file_name=file_name, column=column)
    #
    print("Would you like to search this data? (Y/N)")
    searchchoice = input()
    if searchchoice.upper() == 'Y':
        print("What is the value that you'd like to search for?")
        search_value = input()
        updatedConfig.change_search_value(search_value=search_value)
    #

    csv_operations.main(updatedConfig)
#

if choice.upper() == 'N':
    #run the default module with default config
    defaultConfig = config.config()
    csv_operations.main(defaultConfig)
#

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler('./Output/log.txt')])