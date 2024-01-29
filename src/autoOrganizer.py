import os
import json
import shutil
from interfaceDefinition import InterfaceDefinition

class AutoOrganizer:
    """
    Class to organize files by tags

    Attributes:
        configPath (str): The path of the configuration file
        config (dict): The configuration of the AutoOrganizer
        configured (bool): True if the AutoOrganizer is configured, False otherwise

    Methods:
        loadConfig(path = None): Method to load the configuration file
        saveConfig(): Method to save the configuration file
        configure(basePath): Method to configure the AutoOrganizer
        addFile(path, tags): Method to add a file to the AutoOrganizer
        removeFile(id): Method to remove a file from the AutoOrganizer
        search(tags): Method to search files by tags
        showTags(id): Method to show the tags of a file
        calculatePath(tags): Method to calculate the path where the file will be copied
        getMaxId(): Method to get the max id of the files
    """

    def __init__(self):
        """
        Initialize the AutoOrganizer.
        It will load the configuration file (config.json) if it exists in the working directory
        """
        self.configPath = "config.json"
        self.config = {}
        self.configured = False
        self.loadConfig()

    def loadConfig(self, path = None):
        """
        Method to load the configuration file. If the path is not specified it will load the default one (config.json)
        
        Args:
            path (str, optional): The path of the configuration file. Defaults to None.
        
        Returns:
            bool: True if the configuration file is loaded successfully, False otherwise
        """
        if path is not None:
            self.configPath = path
        if os.path.exists(self.configPath):
            with open(self.configPath, "r") as f:
                self.config = json.load(f)
                if all(i in ["basePath", "files"] for i in self.config.keys()):
                    self.configured = True
                else:
                    self.config = {}
    
    def saveConfig(self):
        """
        Method to save the configuration file
        If the configuration file is not loaded it will do nothing

        Returns:
            bool: True if the configuration file is saved successfully, False otherwise
        """
        if self.configured:
            with open(self.configPath, "w") as f:
                json.dump(self.config, f)
    
    def configure(self, basePath):
        """
        Method to configure the AutoOrganizer.
        It will set the base path and initialize the files list

        Args:
            basePath (str): The base path of the files
        
        Returns:
            bool: True if the configuration is successful, False otherwise
        """
        self.config["basePath"] = basePath
        self.config["files"] = []
        self.configured = True
        self.saveConfig()
    
    def addFile(self, path, tags):
        """
        Method to add a file to the AutoOrganizer

        Args:
            path (str): The path of the file
            tags (list): The additional tags of the file
        
        Returns:
            bool: True if the file is added successfully, False otherwise
        """
        if(not self.configured):
            return False
        elif not os.path.exists(path):
            return False
        else:
            newPath = self.calculatePath(tags)
            fileName = os.path.basename(path)
            [tags.append(i) for i in " ".join(fileName.split(".")[:-1]).split(" ") if i not in tags]
            shutil.copy(path, newPath+fileName)
            self.config["files"].append({"id":self.getMaxId()+1, "path": newPath, "tags": tags, "name":fileName})
            self.saveConfig()
            return True

    def removeFile(self, id):
        """
        Method to remove a file from the AutoOrganizer
        
        Args:
            id (int): The id of the file to remove
        
        Returns:
            bool: True if the file is removed successfully, False otherwise
        """
        if(not self.configured):
            return False
        else:
            for (index,file) in enumerate(self.config["files"]):
                if file["id"] == id:
                    os.remove(file["path"]+file["name"])
                    self.config["files"].pop(index)
                    self.saveConfig()
                    return True
            return False

    def search(self, tags):
        """
        Method to search files by tags

        Args:
            tags (list): The tags to search
        
        Returns:
            list: The list of files that match the tags (empty list if no file is found or the AutoOrganizer is not configured)
        """
        if(not self.configured):
            return []
        else:
            result = []
            for file in self.config["files"]:
                if all(tag in file["tags"] for tag in tags):
                    result.append(file)
            return result

    def showTags(self, id):
        """
        Method to show the tags of a file

        Args:
            id (int): The id of the file to show the tags
        
        Returns:
            list: The list of tags of the file (empty list if no tag is found or the AutoOrganizer is not configured)
        """
        if(not self.configured):
            return []
        else:
            for file in self.config["files"]:
                if file["id"] == id:
                    return file["tags"]
            return []

    def calculatePath(self, tags):
        """
        Method to calculate the path where the file will be copied
        
        Args:
            tags (list): The tags of the file
        
        Returns:
            str: The path where the file will be copied (empty string if the AutoOrganizer is not configured)
        """
        if(not self.configured):
            return ""
        possiblePaths = [i[0][len(self.config["basePath"]):] for i in os.walk(self.config["basePath"])]
        chosenPath = ""
        chosenPathCounter = 0
        for path in possiblePaths:
            counter = 0
            for tag in tags:
                if tag in path.split(os.path.sep):
                    counter += 1
            if counter > chosenPathCounter:
                chosenPath = path
                chosenPathCounter = counter
            elif counter == chosenPathCounter and len(chosenPath.split(os.path.sep)) > len(path.split(os.path.sep)):
                chosenPath = path
        return self.config["basePath"]+chosenPath+os.path.sep

    def getMaxId(self):
        """
        Method to get the max id of the files

        Returns:
            int: The max id of the files (0 if no file is found, -1 if the AutoOrganizer is not configured)
        """
        if(not self.configured):
            return -1
        else:
            if(len(self.config["files"]) == 0):
                return 0
            else:
                return max([i["id"] for i in self.config["files"]])


class AutoOrganizerInterface(InterfaceDefinition):
    """
    Class to show the AutoOrganizer interface

    Attributes:
        ao (AutoOrganizer): The AutoOrganizer to use

    Static Attributes:
        languages (dict): dictionary that contains all the languages supported by the program

    Methods:
        textInterface(lang): Show the AutoOrganizer interface
    """

    
    languages = {
        "ita": {
            "choiceLoadConfig": "1. Carica configurazione",
            "choiceConfigure": "2. Inizializza configurazione",
            "choiceExit1": "3. Esci",
            "choice": "Scelta: ",
            "goodbye": "arrivederci",
            "pressEnterToContinue": "\nPremi invio per continuare...",
            "choiceNotValid": "Scelta non valida",
            "insertConfigPath": "Inserisci il path del file di configurazione: ",
            "insertBasePath": "Inserisci il path base per la configurazione: ",
            "configLoaded": "Configurazione caricata con successo",
            "configError": "Errore nel caricamento della configurazione",
            "configInitialized": "Configurazione inizializzata con successo",
            "configInitError": "Errore nell'inizializzazione della configurazione",
            "choiceAddFile": "1. Aggiungi file",
            "choiceRemoveFile": "2. Rimuovi file",
            "choiceSearch": "3. cerca",
            "choiceShowTags": "4. mostra i tag di un file",
            "insertPath": "Inserisci il path del file: ",
            "insertTags": "Inserisci i tag separati da virgola: ",
            "fileAdded": "File aggiunto con successo",
            "fileAddError": "Errore nell'aggiunta del file",
            "insertIdFileToRemove": "Inserisci l'id del file da eliminare: ",
            "fileRemoved": "File eliminato con successo",
            "fileRemoveError": "Errore nell'eliminazione del file",
            "insertIdFileToSearchTags": "Inserisci l'id del file di cui vuoi i tags: ",
            "choiceExit2": "5. Esci",
        },
        "eng": {
            "choiceLoadConfig": "1. Load configuration",
            "choiceConfigure": "2. Initialize configuration",
            "choiceExit1": "3. Exit",
            "choice": "Choice: ",
            "goodbye": "goodbye",
            "pressEnterToContinue": "\nPress enter to continue...",
            "choiceNotValid": "Choice not valid",
            "insertConfigPath": "Insert the path of the configuration file: ",
            "insertBasePath": "Insert the base path for the configuration: ",
            "configLoaded": "Configuration loaded successfully",
            "configError": "Error loading configuration",
            "configInitialized": "Configuration initialized successfully",
            "configInitError": "Error initializing configuration",
            "choiceAddFile": "1. Add file",
            "choiceRemoveFile": "2. Remove file",
            "choiceSearch": "3. Search",
            "choiceShowTags": "4. Show tags of a file",
            "insertPath": "Insert the path of the file: ",
            "insertTags": "Insert the tags separated by comma: ",
            "fileAdded": "File added successfully",
            "fileAddError": "Error adding file",
            "insertIdFileToRemove": "Insert the id of the file to remove: ",
            "fileRemoved": "File removed successfully",
            "fileRemoveError": "Error removing file",
            "insertIdFileToSearchTags": "Insert the id of the file to show the tags: ",
            "choiceExit2": "5. Exit",
        }
    }

    def __init__(self, ao = None):
        """
        Initialize the AutoOrganizerInterface

        Args:
            ao (AutoOrganizer, optional): The AutoOrganizer to use (default: None)
        
        Returns:
            None
        """
        super().__init__(["AutoOrganizer"], "0.1", "dp")
        self.ao = ao if ao is not None else AutoOrganizer()

    def textInterface(self, lang="eng"):
        """
        Show the AutoOrganizer interface

        Args:
            lang (str, optional): The language of the interface (default: "eng")

        Returns:
            None
        """
        while True:
            super().drowPrologue()
            if(not self.ao.configured):
                print(AutoOrganizerInterface.languages[lang]["choiceLoadConfig"])
                print(AutoOrganizerInterface.languages[lang]["choiceConfigure"])
                print(AutoOrganizerInterface.languages[lang]["choiceExit1"])
                choice = input(AutoOrganizerInterface.languages[lang]["choice"])
                if choice == "1":
                    path = input(AutoOrganizerInterface.languages[lang]["insertConfigPath"])
                    self.ao.loadConfig(path)
                    if(self.ao.configured):
                        print(AutoOrganizerInterface.languages[lang]["configLoaded"])
                    else:
                        print(AutoOrganizerInterface.languages[lang]["configError"])
                elif choice == "2":
                    path = input(AutoOrganizerInterface.languages[lang]["insertBasePath"])
                    self.ao.configure(path)
                    if(self.ao.configured):
                        print(AutoOrganizerInterface.languages[lang]["configInitialized"])
                    else:
                        print(AutoOrganizerInterface.languages[lang]["configInitError"])
                elif choice == "3":
                    print(AutoOrganizerInterface.languages[lang]["goodbye"])
                    return
                else:
                    print(AutoOrganizerInterface.languages[lang]["choiceNotValid"])
            else:
                print(AutoOrganizerInterface.languages[lang]["choiceAddFile"])
                print(AutoOrganizerInterface.languages[lang]["choiceRemoveFile"])
                print(AutoOrganizerInterface.languages[lang]["choiceSearch"])
                print(AutoOrganizerInterface.languages[lang]["choiceShowTags"])
                print(AutoOrganizerInterface.languages[lang]["choiceExit2"])
                choice = input(AutoOrganizerInterface.languages[lang]["choice"])
                if choice == "1":
                    path = input(AutoOrganizerInterface.languages[lang]["insertPath"])
                    tags = [i.strip() for i in input(AutoOrganizerInterface.languages[lang]["insertTags"]).split(",") if i.strip() != ""]
                    if self.ao.addFile(path, tags):
                        print(AutoOrganizerInterface.languages[lang]["fileAdded"])
                    else:
                        print(AutoOrganizerInterface.languages[lang]["fileAddError"])
                elif choice == "2":
                    id = int(input(AutoOrganizerInterface.languages[lang]["insertIdFileToRemove"]))
                    if self.ao.removeFile(id):
                        print(AutoOrganizerInterface.languages[lang]["fileRemoved"])
                    else:
                        print(AutoOrganizerInterface.languages[lang]["fileRemoveError"])
                elif choice == "3":
                    tags = [i.strip() for i in input(AutoOrganizerInterface.languages[lang]["insertTags"]).split(",") if i.strip() != ""]
                    for file in self.ao.search(tags):
                        print(file["id"], file["name"])
                elif choice == "4":
                    id = int(input(AutoOrganizerInterface.languages[lang]["insertIdFileToSearchTags"]))
                    for tag in self.ao.showTags(id):
                        print(tag)
                elif choice == "5":
                    print(AutoOrganizerInterface.languages[lang]["goodbye"])
                    return
                else:
                    print(AutoOrganizerInterface.languages[lang]["choiceNotValid"])
            input(AutoOrganizerInterface.languages[lang]["pressEnterToContinue"])


if __name__ == "__main__":
    AutoOrganizerInterface().textInterface()