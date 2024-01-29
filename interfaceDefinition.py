import math
import os

class InterfaceDefinition:
    """
    Class that represent the interface definition

    Attributes:
        lines (list): lines to show
        version (str): version of the program
        author (str): author of the program
    
    Methods:
        drowPrologue: show the prologue
        textInterface: show the interface
    """
    def __init__(self, lines, version, author):
        """
        Initialize the interface definition

        Args:
            lines (list): lines to show
            version (str): version of the program
            author (str): author of the program
        
        Returns:
            None
        """
        self.lines = lines
        self.version = version
        self.author = author
    
    def drowPrologue(self):
        """
        Show the prologue

        Returns:
            None
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        lenght = max([len(i) for i in self.lines])
        tryLine = f"by {self.author} v:{self.version}"
        if len(tryLine) > lenght:
            lenght = len(tryLine)
        else:
            tryLine = "by " + self.author + " " *(lenght-len(tryLine)+1) + "v:" + self.version
        print("----" + "-"*lenght + "----")
        for i in self.lines:
            print("    " + " "*(math.floor((lenght-len(i))/2)) + i + " "*(math.ceil((lenght-len(i))/2)) + "    ")
        print("    " + tryLine + "    ")
        print("----" + "-"*lenght + "----")
    
    def textInterface(self):
        """
        Show the interface (to be implemented in the child classes)
        """
        pass