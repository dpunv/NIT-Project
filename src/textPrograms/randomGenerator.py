from random import randint
from interfaces.interfaceDefinition import InterfaceDefinition

class RandomGenerator:
    """
    Class that represent a random number generator
    
    Attributes:
        alreadyCalled (list): list of numbers already called
        minimum (int): minimum value
        maximum (int): maximum value
    
    Methods:
        generateRandom: generate a random number
        generateRandomWithoutRepetitions: generate a random number without repetitions
        reset: reset the generator
        textInterface: show the random number generator interface
    """

    def __init__(self, minimum=1, maximum=100):
        """
        Initialize the random number generator
        
        Args:
            minimum (int): minimum value
            maximum (int): maximum value
        
        Returns:
            None
        """
        self.alreadyCalled = []
        self.minimum = minimum
        self.maximum = maximum

    def generateRandom(self):
        """
        Method that generate a random number

        Returns:
            int: random number between minimum and maximum
        """
        return randint(self.minimum, self.maximum)

    def generateRandomWithoutRepetitions(self):
        """
        Method that generate a random number without repetitions
        
        Returns:
            int: random number between minimum and maximum
        """
        n = self.generateRandom()
        while n in self.alreadyCalled:
            n = self.generateRandom()
        self.alreadyCalled.append(n)
        return n

    def reset(self):
        """
        Method that reset the generator

        Returns:
            None
        """
        self.alreadyCalled.clear()


class RandomGeneratorInterface(InterfaceDefinition):
    """
    Class that represent the random number generator interface

    Attributes:
        rg (RandomGenerator): random number generator to use

    Methods:
        textInterface: show the random number generator interface
    """

    languages = {
        "ita": {
            "choiceRandomNumber": "1. Genera un numero casuale",
            "choiceRandomNumberWithoutRepetitions": "2. Genera un numero casuale senza ripetizioni",
            "choiceReset": "3. Reset",
            "choiceSetMaximum": "4. Imposta il valore massimo (attuale: ",
            "choiceSetMinimum": "5. Imposta il valore minimo (attuale: ",
            "choiceShowCalledNumbers": "6. Mostra numeri già chiamati",
            "choiceShowStatistics": "7. mostra statistiche",
            "choiceExit": "8. Esci",
            "choiceNotValid": "Scelta non valida",
            "choice": "Scelta (default 2): ",
            "allNumbersCalled": "Tutti i numeri sono stati chiamati",
            "howManyCalled": "Numeri chiamati: ",
            "howManyToBeCalled": "Numeri da chiamare: ",
            "goodbye": "arrivederci",
            "pressEnterToContinue": "\nPremi invio per continuare...",
            "insertMaximumValue": "Inserisci il valore massimo: ",
            "insertMinimumValue": "Inserisci il valore minimo: ",
            "errorGeneratingRandomNumber": "Errore generando un numero casuale",
            "errorResetting": "Errore resettando",
            "errorSettingMaximum": "Errore impostando il valore massimo",
            "errorSettingMinimum": "Errore impostando il valore minimo",
            "errorShowingCalledNumbers": "Errore mostrando i numeri già chiamati",
            "errorShowingStatistics": "Errore mostrando le statistiche"
        },
        "eng": {
            "choiceRandomNumber": "1. Generate a random number",
            "choiceRandomNumberWithoutRepetitions": "2. Generate a random number without repetitions",
            "choiceReset": "3. Reset",
            "choiceSetMaximum": "4. Set maximum value (current: ",
            "choiceSetMinimum": "5. Set minimum value (current: ",
            "choiceShowCalledNumbers": "6. Show called numbers",
            "choiceShowStatistics": "7. Show statistics",
            "choiceExit": "8. Exit",
            "choiceNotValid": "Choice not valid",
            "choice": "Choice (default 2): ",
            "allNumbersCalled": "All numbers have been called",
            "howManyCalled": "Numbers called: ",
            "howManyToBeCalled": "Numbers to be called: ",
            "goodbye": "goodbye",
            "pressEnterToContinue": "\nPress enter to continue...",
            "insertMaximumValue": "Insert maximum value: ",
            "insertMinimumValue": "Insert minimum value: ",
            "errorGeneratingRandomNumber": "Error generating a random number",
            "errorResetting": "Error resetting",
            "errorSettingMaximum": "Error setting maximum value",
            "errorSettingMinimum": "Error setting minimum value",
            "errorShowingCalledNumbers": "Error showing called numbers",
            "errorShowingStatistics": "Error showing statistics"
        }
    }

    def __init__(self, rg=None):
        """
        Initialize the random number generator interface

        Args:
            rg (RandomGenerator): random number generator to use

        Returns:
            None
        """

        super().__init__(["Random Generator With Memory"], "0.1", "dp")
        self.rg = rg if rg != None else RandomGenerator()

    def textInterface(self, lang="eng"):
        """
        Method that show the random number generator interface

        Args:
            lang (str): language to use for the error message (default: "eng")

        Returns:
            None
        """
        
        while True:
            super().drowPrologue()
            print(RandomGeneratorInterface.languages[lang]["choiceRandomNumber"])
            print(RandomGeneratorInterface.languages[lang]["choiceRandomNumberWithoutRepetitions"])
            print(RandomGeneratorInterface.languages[lang]["choiceReset"])
            print(RandomGeneratorInterface.languages[lang]["choiceSetMaximum"] + str(self.rg.maximum) + ")")
            print(RandomGeneratorInterface.languages[lang]["choiceSetMinimum"] + str(self.rg.minimum) + ")")
            print(RandomGeneratorInterface.languages[lang]["choiceShowCalledNumbers"])
            print(RandomGeneratorInterface.languages[lang]["choiceShowStatistics"])
            print(RandomGeneratorInterface.languages[lang]["choiceExit"])
            choiceStr = input(RandomGeneratorInterface.languages[lang]["choice"])
            choice = int(choiceStr if choiceStr.isnumeric() else "2")
            if choice == 1:
                try:
                    print(self.rg.generateRandom())
                except:
                    print(RandomGeneratorInterface.languages[lang]["errorGeneratingRandomNumber"])
            elif choice == 2:
                try:
                    if(len(self.rg.alreadyCalled) == self.rg.maximum - self.rg.minimum + 1):
                        print(RandomGeneratorInterface.languages[lang]["allNumbersCalled"])
                    else:
                        print(self.rg.generateRandomWithoutRepetitions())
                except:
                    print(RandomGeneratorInterface.languages[lang]["errorGeneratingRandomNumber"])
            elif choice == 3:
                try:
                    self.rg.reset()
                except:
                    print(RandomGeneratorInterface.languages[lang]["errorResetting"])
            elif choice == 4:
                try:
                    self.rg.maximum = int(input(RandomGeneratorInterface.languages[lang]["insertMaximumValue"]))
                except:
                    print(RandomGeneratorInterface.languages[lang]["errorSettingMaximum"])
            elif choice == 5:
                try:
                    self.rg.minimum = int(input(RandomGeneratorInterface.languages[lang]["insertMinimumValue"]))
                except:
                    print(RandomGeneratorInterface.languages[lang]["errorSettingMinimum"])
            elif choice == 6:
                try:
                    for i in range(len(self.rg.alreadyCalled)):
                        print(self.rg.alreadyCalled[i], end=" ")
                        if(i+1 % 10 == 0):
                            print()
                except:
                    print(RandomGeneratorInterface.languages[lang]["errorShowingCalledNumbers"])
            elif choice == 7:
                try:
                    howManyCalled = len(self.rg.alreadyCalled)
                    howManyToBeCalled = self.rg.maximum - self.rg.minimum + 1 - howManyCalled
                    print(RandomGeneratorInterface.languages[lang]["howManyCalled"] + str(howManyCalled))
                    print(RandomGeneratorInterface.languages[lang]["howManyToBeCalled"] + str(howManyToBeCalled))
                except:
                    print(RandomGeneratorInterface.languages[lang]["errorShowingStatistics"])
            elif choice == 8:
                print(RandomGeneratorInterface.languages[lang]["goodbye"])
                return
            else:
                print(RandomGeneratorInterface.languages[lang]["choiceNotValid"])
            input(RandomGeneratorInterface.languages[lang]["pressEnterToContinue"])

def construct():
    """
    Method that construct a random number generator interface

    Returns:
        RandomGeneratorInterface: a random number generator interface
    """
    return RandomGeneratorInterface(RandomGenerator())

if __name__ == "__main__":
    RandomGeneratorInterface().textInterface()