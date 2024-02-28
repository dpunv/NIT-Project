from interfaces.interfaceDefinition import InterfaceDefinition
import math
import os

class FileDiver:
    """
    Class that allows you to analyze a folder and get information about it.

    Attributes:
        path (str): The path of the folder to analyze.
    
    Methods:
        getTotalSize: Returns the total size of the folder.
        getPrettySize: Returns a pretty string of the size passed as a parameter.
        getTopTenFilesRankedBySize: Returns the top ten files ranked by size.
        getPercentileOfFilesBySize: Returns the size of a percentile of files.
        getFilesFormatDistribution: Returns a dictionary with the distribution of the formats.
        getFilesWithExtension: Returns a list of files with the extension passed as a parameter.
        getFilesExtensionSizeDistribution: Returns a dictionary with the distribution of the size by extension.
        maxFolederDepth: Returns the max folder depth.
        getRowSize: Returns the size of a row.
    """

    def __init__(self, path):
        """
        Initializes the FileDiver class.

        Args:
            path (str): The path of the folder to analyze.
        
        Raises:
            Exception: If the path is not valid.
        """

        try:
            self.path = path
            if not os.path.isdir(path):
                raise Exception
        except:
            raise Exception("Invalid path")

    def getTotalSize(self):
        """
        Returns the total size of the folder.

        Returns:
            int: The total size of the folder.
        """
        totalSize = 0
        for path, dirs, files in os.walk(self.path):
            for file in files:
                totalSize += os.path.getsize(os.path.join(path, file))
        return totalSize
    
    def getPrettySize(self, size):
        """
        Returns a pretty string of the size passed as a parameter.

        Args:
            size (int): The size to convert.

        Returns:
            str: The pretty string of the size passed as a parameter.
        """

        if size < 1024:
            return str(size) + " B"
        elif size < 1024**2:
            return str(round(size/1024, 2)) + " KiB"
        elif size < 1024**3:
            return str(round(size/1024**2, 2)) + " MiB"
        elif size < 1024**4:
            return str(round(size/1024**3, 2)) + " GiB"
        elif size < 1024**5:
            return str(round(size/1024**4, 2)) + " TiB"
        elif size < 1024**6:
            return str(round(size/1024**5, 2)) + " PiB"
        elif size < 1024**7:
            return str(round(size/1024**6, 2)) + " EiB"
        elif size < 1024**8:
            return str(round(size/1024**7, 2)) + " ZiB"
        else:
            return str(round(size/1024**8, 2)) + " YiB"

    def getTopTenFilesRankedBySize(self):
        """
        Returns the top ten files ranked by size.

        Returns:
            list: The top ten files ranked by size.
        """

        choosenFiles = []
        leastSize = 0
        for path, dirs, files in os.walk(self.path):
            for file in files:
                filePath = os.path.join(path, file)
                fileSize = os.path.getsize(filePath)
                if len(choosenFiles) < 10:
                    for index, choosen in enumerate(choosenFiles):
                        if fileSize > os.path.getsize(choosen):
                            choosenFiles.insert(index, filePath)
                            break
                    choosenFiles.append(filePath)
                    leastSize = min(fileSize, leastSize)
                elif fileSize > leastSize:
                    for index, choosen in enumerate(choosenFiles):
                        if fileSize > os.path.getsize(choosen):
                            choosenFiles.insert(index, filePath)
                            choosenFiles.pop()
                            leastSize = os.path.getsize(choosenFiles[-1])
                            break
        return [[self.getPrettySize(os.path.getsize(fp)), os.path.basename(fp)] for fp in choosenFiles]
    
    def getPercentileOfFilesBySize(self, percentile):
        """
        Returns the size of a percentile of files.

        Args:
            percentile (float): The percentile to calculate.

        Returns:
            str: The size of a percentile of files.
        """
        files = {os.path.join(path, file): os.path.getsize(os.path.join(path, file)) for path, dirs, files in os.walk(self.path) for file in files}
        fileNames = [i for i in files.keys()]
        fileNames.sort(key=lambda file: files[file])
        fileNames = fileNames[math.floor(len(fileNames)*percentile/100):]
        totalSize = 0
        for file in fileNames:
            totalSize += files[file]
        return self.getPrettySize(totalSize)

    def getFilesFormatDistribution(self):
        """
        Returns a dictionary with the distribution of the formats.
        
        Returns:
            dict: A dictionary with the distribution of the formats.
        """
        formats = {}
        for path, dirs, files in os.walk(self.path):
            for file in files:
                extension = file.split(".")[-1]
                if extension in [i for i in formats.keys()]:
                    formats[extension] += 1
                else:
                    formats[extension] = 1
        return formats
    
    def getFilesWithExtension(self, extension):
        """
        Returns a list of files with the extension passed as a parameter.

        Args:
            extension (str): The extension to search.
        
        Returns:
            list: A list of files with the extension passed as a parameter.
        """
        return [file for path, dir, files in os.walk(self.path) for file in files if file.split(".")[-1] == extension]

    def getFilesExtensionSizeDistribution(self):
        """
        Returns a dictionary with the distribution of the size by extension.

        Returns:
            dict: A dictionary with the distribution of the size by extension.
        """
        formats = {}
        for path, dirs, files in os.walk(self.path):
            for file in files:
                extension = file.split(".")[-1]
                if extension in formats.keys():
                    formats[extension] += os.path.getsize(os.path.join(path, file))
                else:
                    formats[extension] = os.path.getsize(os.path.join(path, file))
        return formats

    def maxFolederDepth(self):
        """
        Method that returns the max folder depth.

        Returns:
            int: The max folder depth.
        """
        return max([len(path.split(os.path.sep)) for path, dirs, files in os.walk(self.path) for file in files])
    
    def getRowSize(self, prettySize):
        """
        Method that returns the size in row format.

        Args:
            prettySize (str): The size in pretty format.

        Returns:
            int: The size in row format.
        """
        splitted = prettySize.split(" ")
        if splitted[1] == "B":
            return int(splitted[0])
        elif splitted[1] == "KiB":
            return float(splitted[0])*1024
        elif splitted[1] == "MiB":
            return float(splitted[0])*1024**2
        elif splitted[1] == "GiB":
            return float(splitted[0])*1024**3
        elif splitted[1] == "TiB":
            return float(splitted[0])*1024**4
        elif splitted[1] == "PiB":
            return float(splitted[0])*1024**5
        elif splitted[1] == "EiB":
            return float(splitted[0])*1024**6
        elif splitted[1] == "ZiB":
            return float(splitted[0])*1024**7
        else:
            return float(splitted[0])*1024**8
    

class FileDiverInterface(InterfaceDefinition):
    """
    Class that allows you to interact with the FileDiver class.

    Static Attributes:
        languages (dict): A dictionary with the languages.

    Methods:
        textInterface: The text interface of the class.
    """

    languages = {
        "ita": {
            "topTenFilesSizeChoice": "1. Top 10 file più grandi",
            "percentileFilesSizeChoice": "2. Spazio occupato da un percentile di file",
            "filesFormatDistributionChoice": "3. Distribuzione dei formati",
            "filesWithExtensionChoice": "4. File con estensione",
            "filesExtensionSizeDistributionChoice": "5. Distribuzione delle dimensioni per estensione",
            "maxFolderDepthChoice": "6. Profondità massima delle cartelle",
            "returnChoice": "7. Torna al menu principale",
            "exitChoice": "8. Esci",
            "chooseOption": "Scegli un'opzione: ",
            "chooseExtension": "Scegli un'estensione: ",
            "choosePath": "Scegli un percorso (vuoto per uscire): ",
            "invalidOption": "Opzione non valida",
            "invalidPath": "Percorso non valido",
            "invalidExtension": "Estensione non valida",
            "goodbye": "Arrivederci!",
            "pressEnter": "\nPremi invio per continuare...",
            "choosePercentile": "Scegli un percentile: ",
            "errorWhileGettingTopTenFiles": "Errore durante l'ottenimento dei top ten file",
            "errorWhileGettingPercentile": "Errore durante l'ottenimento del percentile",
            "errorWhileGettingFormatDistribution": "Errore durante l'ottenimento della distribuzione dei formati",
            "errorWhileGettingFilesWithExtension": "Errore durante l'ottenimento dei file con estensione",
            "errorWhileGettingFilesExtensionSizeDistribution": "Errore durante l'ottenimento della distribuzione delle dimensioni per estensione",
            "errorWhileGettingMaxFolderDepth": "Errore durante l'ottenimento della profondità massima delle cartelle"
        },
        "eng": {
            "topTenFilesSizeChoice": "1. Top 10 biggest files",
            "percentileFilesSizeChoice": "2. Space occupied by a percentile of files",
            "filesFormatDistributionChoice": "3. Format distribution",
            "filesWithExtensionChoice": "4. Files with extension",
            "filesExtensionSizeDistributionChoice": "5. Distribution of the size by extension",
            "maxFolderDepthChoice": "6. Max folder depth",
            "returnChoice": "7. Return to the main menu",
            "exitChoice": "8. Exit",
            "chooseOption": "Choose an option: ",
            "chooseExtension": "Choose an extension: ",
            "choosePath": "Choose a path (empty to leave): ",
            "invalidOption": "Invalid option",
            "invalidPath": "Invalid path",
            "invalidExtension": "Invalid extension",
            "goodbye": "Goodbye!",
            "pressEnter": "\nPress enter to continue...",
            "choosePercentile": "Choose a percentile: ",
            "errorWhileGettingTopTenFiles": "Error while getting top ten files",
            "errorWhileGettingPercentile": "Error while getting percentile",
            "errorWhileGettingFormatDistribution": "Error while getting format distribution",
            "errorWhileGettingFilesWithExtension": "Error while getting files with extension",
            "errorWhileGettingFilesExtensionSizeDistribution": "Error while getting distribution of the size by extension",
            "errorWhileGettingMaxFolderDepth": "Error while getting max folder depth"
        }
    }

    def __init__(self):
        """
        Initializes the FileDiverInterface class.
        
        Returns:
            None
        """
        super().__init__(["File Diver"], "0.1", "dp")
    
    def textInterface(self, lang="eng"):
        """
        The text interface of the class.

        Args:
            lang (str): The language of the interface.

        Returns:
            None
        """

        while True:
            super().drowPrologue()
            path = input(self.languages[lang]["choosePath"])
            alreadyPressed = False
            if path == "":
                print(self.languages[lang]["goodbye"])
                return
            if os.path.isdir(path):
                fd = FileDiver(path)
                continueLoop = True
                while continueLoop:
                    super().drowPrologue()
                    print(self.languages[lang]["topTenFilesSizeChoice"])
                    print(self.languages[lang]["percentileFilesSizeChoice"])
                    print(self.languages[lang]["filesFormatDistributionChoice"])
                    print(self.languages[lang]["filesWithExtensionChoice"])
                    print(self.languages[lang]["filesExtensionSizeDistributionChoice"])
                    print(self.languages[lang]["maxFolderDepthChoice"])
                    print(self.languages[lang]["returnChoice"])
                    print(self.languages[lang]["exitChoice"])
                    choice = input(self.languages[lang]["chooseOption"])
                    if choice == "1":
                        try:
                            files = fd.getTopTenFilesRankedBySize()
                            for file in files:
                                print(file[0] + " -- " + file[1])
                        except:
                            print(self.languages[lang]["errorWhileGettingTopTenFiles"])
                    elif choice == "2":
                        try:
                            percentile = float(input(self.languages[lang]["choosePercentile"]))
                            sizeFilesPercentile = fd.getPercentileOfFilesBySize(percentile)
                            totalSize = fd.getTotalSize()
                            print(sizeFilesPercentile + "   ---   " + str(round(100*fd.getRowSize(sizeFilesPercentile)/totalSize, 2)) + "%")
                        except:
                            print(self.languages[lang]["errorWhileGettingPercentile"])
                    elif choice == "3":
                        try:
                            formats = fd.getFilesFormatDistribution()
                            for format in formats.keys():
                                print(format + ": " + str(formats[format]))
                        except:
                            print(self.languages[lang]["errorWhileGettingFormatDistribution"])
                    elif choice == "4":
                        try:
                            extension = input(self.languages[lang]["chooseExtension"])
                            files = fd.getFilesWithExtension(extension)
                            for file in files:
                                print(file)
                        except:
                            print(self.languages[lang]["errorWhileGettingFilesWithExtension"])
                    elif choice == "5":
                        try:
                            formats = fd.getFilesExtensionSizeDistribution()
                            for format in formats.keys():
                                print(format + ": " + fd.getPrettySize(formats[format]))
                        except:
                            print(self.languages[lang]["errorWhileGettingFilesExtensionSizeDistribution"])
                    elif choice == "6":
                        try:
                            print(fd.maxFolederDepth())
                        except:
                            print(self.languages[lang]["errorWhileGettingMaxFolderDepth"])
                    elif choice == "7":
                        continueLoop = False
                        alreadyPressed = True
                    elif choice == "8":
                        print(self.languages[lang]["goodbye"])
                        return
                    else:
                        print(self.languages[lang]["invalidOption"])
                    input(self.languages[lang]["pressEnter"])
            else:
                print(self.languages[lang]["invalidPath"])
            if not alreadyPressed:
                input(self.languages[lang]["pressEnter"])


if __name__ == "__main__":
    FileDiverInterface().textInterface()