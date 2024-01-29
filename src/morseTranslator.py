from interfaceDefinition import InterfaceDefinition

class MorseTranslator:
    """
    Class that represent a morse translator

    Attributes:
        abc (str): alphabet
        morseChar (list): morse alphabet
    
    Methods:
        toMorse: translate a text to morse
        fromMorse: translate a morse code to text
        textInterface: show the morse translator interface
    """

    def __init__(self):
        """
        Initialize the morse translator

        Returns:
            None
        """
        self.abc = "abcdefghijklmnopqrstuvwxyz 1234567890"
        self.morseChar = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", " ", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]

    def toMorse(self, toTranslate, lang="eng"):
        """
        Translate a text to morse

        Args:
            toTranslate (str): text to translate
            lang (str): language to use for the error message (default: "eng")

        
        Returns:
            str: translated text if no errors, error message otherwise
        """
        translated = ""
        for index in toTranslate:
            if(index not in self.abc):
                return MorseTranslator.languages[lang]["errorMessageTextPart1"] + index + MorseTranslator.languages[lang]["errorMessageTextPart2"] + str(toTranslate.index(index)) + ")"
            translated += self.morseChar[self.abc.index(index)] + " "
        return translated

    def fromMorse(self, toTranslate, lang="eng"):
        """
        Translate a morse code to text
        
        Args:
            toTranslate (str): morse code to translate
            lang (str): language to use for the error message (default: "eng")

        Returns:
            str: translated morse code if no errors, error message otherwise
        """
        sequence = ""
        translated = ""
        for index in range(len(toTranslate)):
            if toTranslate[index] == " ":
                if index < len(toTranslate)-1 and toTranslate[index+1] == " " and toTranslate[index-1] != " ":
                        if sequence not in self.morseChar:
                            return MorseTranslatorInterface.languages[lang]["errorMessageMorsePart1"] + sequence + MorseTranslatorInterface.languages[lang]["errorMessageMorsePart2"] + str(toTranslate.index(sequence)) + ")"
                        translated += self.abc[self.morseChar.index(sequence)] + " "
                        sequence = ""
                else:
                    if toTranslate[index-1] != " ":
                        translated += self.abc[self.morseChar.index(sequence)]
                        sequence = ""
            else:
                sequence += toTranslate[index]
        if sequence != "":
            if sequence not in self.morseChar:
                return MorseTranslator.languages[lang]["errorMessageMorsePart1"] + sequence + MorseTranslator.languages[lang]["errorMessageMorsePart2"] + str(toTranslate.index(sequence)) + ")"
            translated += self.abc[self.morseChar.index(sequence)]
        return translated


class MorseTranslatorInterface(InterfaceDefinition):
    """
    Class that represent a morse translator interface

    Attributes:
        mt (MorseTranslator): morse translator to use
    
    Static Attributes:
        languages (dict): dictionary that contains all the languages supported by the program

    Methods:
        textInterface: show the morse translator interface
    """

    languages = {
        "ita": {
            "choiceToMorse": "scrivi un testo da tradurre in morse",
            "choiceFromMorse": "oppure scrivi un codice morse da tradurre in testo",
            "choiceExit": "per uscire premi invio",
            "choice": " --> ",
            "goodbye": "arrivederci",
            "pressEnterToContinue": "\nPremi invio per continuare...",
            "errorMessageMorsePart1": "codice morse non valido: ",
            "errorMessageMorsePart2": " (posizione ",
            "errorMessageTextPart1": "carattere non valido: ",
            "errorMessageTextPart2": " (posizione "
        },
        "eng": {
            "choiceToMorse": "write a text to translate in morse",
            "choiceFromMorse": "or write a morse code to translate in text",
            "choiceExit": "press enter to exit",
            "choice": " --> ",
            "goodbye": "goodbye",
            "pressEnterToContinue": "\nPress enter to continue...",
            "errorMessageMorsePart1": "invalid morse code: ",
            "errorMessageMorsePart2": " (position ",
            "errorMessageTextPart1": "invalid character: ",
            "errorMessageTextPart2": " (position "
        }
    }

    def __init__(self, mt=None):
        """
        Initialize the morse translator interface

        Args:
            mi (MorseTranslator): morse translator to use
        
        Returns:
            None
        """
        super().__init__(["-- --- .-. ... .", "morse to alphabet and back again"], "0.2", "dp")
        self.mt = mt if mt != None else MorseTranslator()

    def textInterface(self, lang="eng"):
        """
        Show the morse translator interface

        Args:
            lang (str): language to use for the interface (default: "eng")
        
        Returns:
            None
        """
        while True:
            super().drowPrologue()
            print(MorseTranslatorInterface.languages[lang]["choiceToMorse"])
            print(MorseTranslatorInterface.languages[lang]["choiceFromMorse"])
            print(MorseTranslatorInterface.languages[lang]["choiceExit"])
            choice = input(MorseTranslatorInterface.languages[lang]["choice"])
            if len(choice) == 0:
                print(MorseTranslatorInterface.languages[lang]["goodbye"])
                return
            else:
                if choice.lower()[0] in self.mt.abc:
                    print(self.mt.toMorse(choice.lower()))
                else:
                    print(self.mt.fromMorse(choice))
            input(MorseTranslatorInterface.languages[lang]["pressEnterToContinue"])

if __name__ == "__main__":
    MorseTranslatorInterface().textInterface()