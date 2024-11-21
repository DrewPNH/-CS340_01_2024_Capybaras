class config:
    def __init__(self, file_name='titanic.csv', column='Age', secondcol=None, search_value=None):
        self.file_name = file_name
        self.secondcol = secondcol
        self.column = column
        self.search_value = search_value
    #
    def change_search_value(self, search_value):
        self.search_value = search_value
    #
#