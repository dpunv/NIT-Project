

from interfaceDefinition import InterfaceDefinition
from autoOrganizer import AutoOrganizer, AutoOrganizerInterface
from morseTranslator import MorseTranslator, MorseTranslatorInterface
from randomGenerator import RandomGenerator, RandomGeneratorInterface
import os
import json
try:
    import readline
except ImportError:
    pass

class LauncherNIT(InterfaceDefinition):
    """
    Class that represent the launcher of the NIT programs

    Attributes:
        programs (dict): dictionary that contains all the installed programs

    Static Attributes:
        languages (dict): dictionary that contains all the languages supported by the program
    
    Methods:
        textInterface: show the launcher interface
    """

    languages = {
        "ita": {
            "choiceExit": ". Esci",
            "choiceNotValid": "Scelta non valida",
            "choice": "Scelta: ",
            "goodbye": "arrivederci",
            "pressEnterToContinue": "\nPremi invio per continuare...",
            "choiceLanguage": ". Cambia lingua",
            "languageChoice": "inserisci una lingua dalla seguente lista:"
        },
        "eng": {
            "choiceExit": ". Exit",
            "choiceNotValid": "Choice not valid",
            "choice": "Choice: ",
            "goodbye": "goodbye",
            "pressEnterToContinue": "\nPress enter to continue...",
            "choiceLanguage": ". Change language",
            "languageChoice": "insert a language from the following list:"
        }
    }

    def __init__(self):
        """
        Initialize the launcher. It will load all the programs installed

        Returns:
            None
        """
        super().__init__(["launcher NIT"], "0.1", "dp")
        self.programs = {
            "AutoOrganizer": AutoOrganizerInterface(AutoOrganizer()),
            "TraduttoreMorse": MorseTranslatorInterface(MorseTranslator()),
            "GeneratoreCasuali:": RandomGeneratorInterface(RandomGenerator())
        }

    def textInterface(self):
        """
        Show the launcher interface

        Returns:
            None
        """
        lang = "eng"
        if(os.path.exists("NITConfig.json")):
            with open("NITConfig.json", "r") as file:
                lang = json.load(file)["lang"]
        while True:
            super().drowPrologue()
            for index, key in enumerate(self.programs.keys()):
                print(f"{index+1}. {key}")
            print(str(len(self.programs.keys())+1) + LauncherNIT.languages[lang]["choiceLanguage"])
            print(str(len(self.programs.keys())+2) + LauncherNIT.languages[lang]["choiceExit"])
            rawChoice = input(LauncherNIT.languages[lang]["choice"])
            choice = int(rawChoice) if rawChoice.isnumeric() else -1
            if(choice == 0):
                print("NIT Is Text")
            elif choice > 0 and choice <= len(self.programs.keys()):
                self.programs[list(self.programs.keys())[choice-1]].textInterface(lang)
            elif choice == len(self.programs.keys()) + 1:
                print(LauncherNIT.languages[lang]["languageChoice"])
                for index, key in enumerate(LauncherNIT.languages.keys()):
                    print(f"{index+1}. {key}")
                rawChoice = input(LauncherNIT.languages[lang]["choice"])
                choice = int(rawChoice) if rawChoice.isnumeric() else -1
                if choice > 0 and choice <= len(LauncherNIT.languages.keys()):
                    lang = list(LauncherNIT.languages.keys())[choice-1]
                    with open("NITConfig.json", "w") as file:
                        json.dump({"lang": lang}, file)
                else:
                    print(LauncherNIT.languages[lang]["choiceNotValid"])
            elif choice == len(self.programs.keys()) + 2:
                print(LauncherNIT.languages[lang]["goodbye"])
                exit()
            else:
                print(LauncherNIT.languages[lang]["choiceNotValid"])
            input(LauncherNIT.languages[lang]["pressEnterToContinue"])

if __name__ == "__main__":
    LauncherNIT().textInterface()