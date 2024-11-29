# config.py
class config:
    def __init__(self, file_name="titanic.csv", column="age", secondcol=None, search_value=None):
        """Initialize configuration with defaults."""
        self.file_name = file_name
        self.column = column
        self.secondcol = secondcol
        self.search_value = search_value

    def change_search_value(self, search_value):
        """Update search value."""
        self.search_value = search_value
