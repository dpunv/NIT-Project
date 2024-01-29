import math
from interfaceDefinition import InterfaceDefinition

class Add:
    """
    Class that represent the addition operator

    Methods:
        __call__: sum between two numbers
    """

    def __call__(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid expression")
        return operands[0] + operands[1]

class Sub:
    """
    Class that represent the subtraction operator

    Methods:
        __call__: difference between two numbers
    """

    def __call__(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid expression")
        return operands[0] - operands[1]

class Mul:
    """
    Class that represent the multiplication operator
    
    Methods:
        __call__: product between two numbers
    """

    def __call__(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid expression")
        return operands[0] * operands[1]

class Div:
    """
    Class that represent the division operator

    Methods:
        __call__: division between two numbers
    """
    
    def __call__(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid expression")
        return operands[0] / operands[1]

class Pow:
    """
    Class that represent the exponentiation operator

    Methods:
        __call__: exponentiation
    """

    def __call__(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid expression")
        return operands[0] ** operands[1]

class Sin:
    """
    Class that represent the sine operator

    Methods:
        __call__: sine of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.sin(operands[0])

class Cos:
    """
    Class that represent the cosine operator

    Methods:
        __call__: cosine of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.cos(operands[0])

class Tan:
    """
    Class that represent the tangent operator

    Methods:
        __call__: tangent of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.tan(operands[0])

class Cot:
    """
    Class that represent the cotangent operator

    Methods:
        __call__: cotangent of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return 1 / math.tan(operands[0])

class Sec:
    """
    Class that represent the secant operator

    Methods:
        __call__: secant of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return 1 / math.cos(operands[0])

class Csc:
    """
    Class that represent the cosecant operator

    Methods:
        __call__: cosecant of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return 1 / math.sin(operands[0])

class Arcsin:
    """
    Class that represent the arc sine operator

    Methods:
        __call__: arc sine of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.asin(operands[0])

class Arccos:
    """
    Class that represent the arc cosine operator

    Methods:
        __call__: arc cosine of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.acos(operands[0])

class Arctan:
    """
    Class that represent the arc tangent operator

    Methods:
        __call__: arc tangent of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.atan(operands[0])

class Arccot:
    """
    Class that represent the arc cotangent operator

    Methods:
        __call__: arc cotangent of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.atan(1 / operands[0])

class Arcsec:
    """
    Class that represent the arc secant operator
    
    Methods:
        __call__: arc secant of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.acos(1 / operands[0])

class Arccsc:
    """
    Class that represent the arc cosecant operator

    Methods:
        __call__: arc cosecant of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.asin(1 / operands[0])

class Sinh:
    """
    Class that represent the hyperbolic sine operator

    Methods:
        __call__: hyperbolic sine of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.sinh(operands[0])

class Cosh:
    """
    Class that represent the hyperbolic cosine operator

    Methods:
        __call__: hyperbolic cosine of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.cosh(operands[0])

class Tanh:
    """
    Class that represent the hyperbolic tangent operator

    Methods:
        __call__: hyperbolic tangent of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.tanh(operands[0])

class Coth:
    """
    Class that represent the hyperbolic cotangent operator

    Methods:
        __call__: hyperbolic cotangent of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return 1 / math.tanh(operands[0])

class Sech:
    """
    Class that represent the hyperbolic secant operator

    Methods:
        __call__: hyperbolic secant of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return 1 / math.cosh(operands[0])

class Csch:
    """
    Class that represent the hyperbolic cosecant operator

    Methods:
        __call__: hyperbolic cosecant of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return 1 / math.sinh(operands[0])

class Arsinh:
    """
    Class that represent the hyperbolic arc sine operator

    Methods:
        __call__: hyperbolic arc sine of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.asinh(operands[0])

class Arcosh:
    """
    Class that represent the hyperbolic arc cosine operator

    Methods:
        __call__: hyperbolic arc cosine of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.acosh(operands[0])

class Artanh:
    """
    Class that represent the hyperbolic arc tangent operator

    Methods:
        __call__: hyperbolic arc tangent of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.atanh(operands[0])

class Arcoth:
    """
    Class that represent the hyperbolic arc cotangent operator

    Methods:
        __call__: hyperbolic arc cotangent of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.atanh(1 / operands[0])

class Arsech:
    """
    Class that represent the hyperbolic arc secant operator

    Methods:
        __call__: hyperbolic arc secant of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.acosh(1 / operands[0])

class Arcsch:
    """
    Class that represent the hyperbolic arc cosecant operator

    Methods:
        __call__: hyperbolic arc cosecant of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return math.asinh(1 / operands[0])
class Log:
    """
    Class that represent the logarithm operator

    Methods:
        __call__: logarithm in base b of a
    """
    def __call__(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid expression")
        return math.log(operands[0], operands[1])

class Rad:
    """
    Class that represent the n-th root operator

    Methods:
        __call__: n-th root of a number
    """

    def __call__(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid expression")
        return operands[0] ** (1 / operands[1])

class Tet:
    """
    Class that represent the tetration operator

    Methods:
        __call__: tetration of a number
    """

    def __call__(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid expression")
        z = operands[0]
        for i in range(operands[1] - 1):
            z = operands[0] ** z
        return z

class Abs:
    """
    Class that represent the absolute value operator

    Methods:
        __call__: absolute value of a number
    """

    def __call__(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid expression")
        return abs(operands[0])

class Expression:
    """
    Class that represent a mathematical expression

    Attributes:
        stringExpression (str): string that represent the expression
        operator (str): operator of the expression
        operands (list): operands of the expression
        result (float): result of the expression
    
    Static Attributes:
        operators (dict): dictionary that contains all the operators

    Methods:
        addOperand: add an operand to the expression
        parseExpression: parse the expression
        evaluate: evaluate the expression
        __str__: return the string representation of the expression
        removeInvisibleChars: remove all the white spaces from the string expression
    """

    operators = {
        'add': Add(),
        'sub': Sub(),
        'mul': Mul(),
        'div': Div(),
        'pow': Pow(),
        'sin': Sin(),
        'cos': Cos(),
        'tan': Tan(),
        'cot': Cot(),
        'sec': Sec(),
        'csc': Csc(),
        'arcsin': Arcsin(),
        'arccos': Arccos(),
        'arctan': Arctan(),
        'arccot': Arccot(),
        'arcsec': Arcsec(),
        'arccsc': Arccsc(),
        'sinh': Sinh(),
        'cosh': Cosh(),
        'tanh': Tanh(),
        'coth': Coth(),
        'sech': Sech(),
        'csch': Csch(),
        'arsinh': Arsinh(),
        'arcosh': Arcosh(),
        'artanh': Artanh(),
        'arcoth': Arcoth(),
        'arsech': Arsech(),
        'arcsch': Arcsch(),
        'log': Log(),
        'rad': Rad(),
        'tet': Tet(),
        'abs': Abs()
    }
    
    def __init__(self, stringExpression):
        """
        Initialize the expression

        Args:
            stringExpression (str): string that represent the expression

        Returns:
            None
        """

        self.stringExpression = stringExpression
        self.operator = None
        self.operands = []
        self.result = None
    
    def addOperand(self, operand):
        """
        Add an operand to the expression
        
        Args:
            operand (str): operand to add
        
        Returns:
            None
        """

        if operand == "":
            raise Exception("Invalid expression")
        elif "." in operand and (operand.count(".") > 1 or operand[-1] == "."):
            raise Exception("Invalid expression")
        elif "." in operand and operand.count(".") == 1:
            self.operands.append(float(operand))
        elif operand.isnumeric():
            self.operands.append(int(operand))
        else:
            subExpr = Expression(operand)
            subExpr.parseExpression()
            self.operands.append(subExpr)

    def parseExpression(self):
        """
        Parse the expression

        Returns:
            None
        """

        self.removeInvisibleChars()
        currentString = ""
        state = 0
        parenthesis = 0
        for char in self.stringExpression:
            if char.isalpha() and state == 0:
                currentString += char
            elif char == "(" and state == 0:
                state = 1
                if currentString in self.operators.keys():
                    self.operator = currentString
                else:
                    raise Exception("Invalid expression")
                currentString = ""
            elif state == 1 and char == ',' and parenthesis == 0:
                self.addOperand(currentString)
                currentString = ""
            elif state == 1 and char == '(':
                currentString += char
                parenthesis += 1
            elif state == 1 and char == ')':
                if parenthesis == 0:
                    self.addOperand(currentString)
                    break
                else:
                    currentString += char
                    parenthesis -= 1
            elif state == 1:
                currentString += char

    def evaluate(self):
        """
        Evaluate the expression

        Returns:
            float: result of the expression
        """

        if(self.result == None):
            operands = []
            for i in self.operands:
                if type(i) == Expression:
                    operands.append(i.evaluate())
                else:
                    operands.append(i)
            self.result = self.operators[self.operator](operands)
        return self.result

    def __str__(self):
        """
        Return the string representation of the expression

        Returns:
            str: string representation of the expression
        """
        return self.stringExpression

    def removeInvisibleChars(self):
        """
        Remove all the white spaces from the string expression

        Returns:
            None
        """
        newString = ""
        ignore = False
        for char in self.stringExpression:
            if char == "#" and not ignore:
                ignore = True
            if char != " " and char != "\n" and char != "\t" and char != "\r" and not ignore:
                newString += char
            elif char == "\n" and ignore:
                ignore = False
        self.stringExpression = newString

class BaseConverter:
    """
    Class that represent a base converter

    Static Attributes:
        dictionary (str): dictionary that contains all the characters used for the conversion

    Methods:
        baseConverter: convert a number from a base to another
        baseToDecimal: convert a number from a base to decimal
        decimalToBase: convert a number from decimal to a base
    """

    dictionary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    
    def baseConverter(inputNumber, inputBase, outputBase):
        """
        Convert a number from a base to another

        Args:
            inputNumber (str): number to convert
            inputBase (int): base of the input number
            outputBase (int): base of the output number
        
        Returns:
            str: converted number
        """
        try:
            if inputBase == outputBase:
                return inputNumber
            if inputBase == 10:
                return BaseConverter.decimalToBase(inputNumber, outputBase)
            if outputBase == 10:
                return BaseConverter.baseToDecimal(inputNumber, inputBase)
            return BaseConverter.decimalToBase(BaseConverter.baseToDecimal(inputNumber, inputBase), outputBase)
        except Exception as e:
            print(e)
    
    def baseToDecimal(inputNumber, inputBase):
        """
        Convert a number from a base to decimal

        Args:
            inputNumber (str): number to convert
            inputBase (int): base of the input number

        Returns:
            int: converted number
        """
        outputNumber = 0
        for i in range(len(inputNumber)):
            outputNumber += BaseConverter.dictionary.index(inputNumber[i]) * (inputBase ** (len(inputNumber) - i - 1))
        return outputNumber
    
    def decimalToBase(inputNumber, outputBase):
        """
        Convert a number from decimal to a base

        Args:
            inputNumber (int): number to convert
            outputBase (int): base of the output number

        Returns:
            str: converted number
        """

        if(type(inputNumber) == str):
            inputNumber = int(inputNumber)
        outputNumber = ""
        while inputNumber > 0:
            outputNumber = BaseConverter.dictionary[inputNumber % outputBase] + outputNumber
            inputNumber = inputNumber // outputBase
        return outputNumber

class DigitalAbaco(InterfaceDefinition):
    """
    Class that represent a digital abaco

    Static Attributes:
        languages (dict): dictionary that contains all the languages supported by the program

    Methods:
        textInterface: show the digital abaco interface
    """

    languages = {
        "ita": {
            "choiceFile": "1. scegli un file che contiene un'espressione",
            "choiceExpression": "2. inserisci un'espressione da tastiera",
            "choiceDictionary": "3. mostra il dizionario delle funzioni disponibili",
            "choiceBaseConverter": "4. convertitore di base",
            "choiceExit": "5. esci",
            "choice": "scelta: ",
            "insertFile": "inserisci il nome del file: ",
            "insertExpression": "inserisci l'espressione: ",
            "invalidChoice": "scelta non valida",
            "invalidExpression": "espressione non valida",
            "invalidFile": "file non valido",
            "goodbye": "arrivederci",
            "pressEnter": "\npremi invio per continuare...",
            "addDescription": "somma tra due numeri",
            "subDescription": "differenza tra due numeri",
            "mulDescription": "prodotto tra due numeri",
            "divDescription": "divisione tra due numeri",
            "powDescription": "elevamento a potenza",
            "sinDescription": "seno di un numero",
            "cosDescription": "coseno di un numero",
            "tanDescription": "tangente di un numero",
            "cotDescription": "cotangente di un numero",
            "secDescription": "secante di un numero",
            "cscDescription": "cosecante di un numero",
            "arcsinDescription": "arco seno di un numero",
            "arccosDescription": "arco coseno di un numero",
            "arctanDescription": "arco tangente di un numero",
            "arccotDescription": "arco cotangente di un numero",
            "arcsecDescription": "arco secante di un numero",
            "arccscDescription": "arco cosecante di un numero",
            "sinhDescription": "seno iperbolico di un numero",
            "coshDescription": "coseno iperbolico di un numero",
            "tanhDescription": "tangente iperbolica di un numero",
            "cothDescription": "cotangente iperbolica di un numero",
            "sechDescription": "secante iperbolica di un numero",
            "cschDescription": "cosecante iperbolica di un numero",
            "arsinhDescription": "arco seno iperbolico di un numero",
            "arcoshDescription": "arco coseno iperbolico di un numero",
            "artanhDescription": "arco tangente iperbolica di un numero",
            "arcothDescription": "arco cotangente iperbolica di un numero",
            "arsechDescription": "arco secante iperbolica di un numero",
            "arcschDescription": "arco cosecante iperbolica di un numero",
            "logDescription": "logaritmo in base b di a",
            "radDescription": "radice n-esima di un numero",
            "tetDescription": "tetrazione di un numero",
            "absDescription": "valore assoluto di un numero",
            "insertNumber": "inserisci il numero: ",
            "insertInputBase": "inserisci la base di input: ",
            "insertOutputBase": "inserisci la base di output: ",
            "invalidNumber": "numero non valido",
            "resultNumberInBase": "il numero in base "
        },
        "eng": {
            "choiceFile": "1. choose a file containing an expression",
            "choiceExpression": "2. insert an expression from the keyboard",
            "choiceDictionary": "3. show the dictionary of available functions",
            "choiceBaseConverter": "4. base converter",
            "choiceExit": "5. exit",
            "choice": "choice: ",
            "insertFile": "insert the name of the file: ",
            "insertExpression": "insert the expression: ",
            "invalidChoice": "invalid choice",
            "invalidExpression": "invalid expression",
            "invalidFile": "invalid file",
            "goodbye": "goodbye",
            "pressEnter": "\npress enter to continue...",
            "addDescription": "sum between two numbers",
            "subDescription": "difference between two numbers",
            "mulDescription": "product between two numbers",
            "divDescription": "division between two numbers",
            "powDescription": "exponentiation",
            "sinDescription": "sine of a number",
            "cosDescription": "cosine of a number",
            "tanDescription": "tangent of a number",
            "cotDescription": "cotangent of a number",
            "secDescription": "secant of a number",
            "cscDescription": "cosecant of a number",
            "arcsinDescription": "arc sine of a number",
            "arccosDescription": "arc cosine of a number",
            "arctanDescription": "arc tangent of a number",
            "arccotDescription": "arc cotangent of a number",
            "arcsecDescription": "arc secant of a number",
            "arccscDescription": "arc cosecant of a number",
            "sinhDescription": "hyperbolic sine of a number",
            "coshDescription": "hyperbolic cosine of a number",
            "tanhDescription": "hyperbolic tangent of a number",
            "cothDescription": "hyperbolic cotangent of a number",
            "sechDescription": "hyperbolic secant of a number",
            "cschDescription": "hyperbolic cosecant of a number",
            "arsinhDescription": "hyperbolic arc sine of a number",
            "arcoshDescription": "hyperbolic arc cosine of a number",
            "artanhDescription": "hyperbolic arc tangent of a number",
            "arcothDescription": "hyperbolic arc cotangent of a number",
            "arsechDescription": "hyperbolic arc secant of a number",
            "arcschDescription": "hyperbolic arc cosecant of a number",
            "logDescription": "logarithm in base b of a",
            "radDescription": "n-th root of a number",
            "tetDescription": "tetration of a number",
            "absDescription": "absolute value of a number",
            "insertNumber": "insert the number: ",
            "insertInputBase": "insert the input base: ",
            "insertOutputBase": "insert the output base: ",
            "invalidNumber": "invalid number",
            "resultNumberInBase": "the number in base "
        }
    }

    def __init__(self):
        """
        Initialize the digital abaco interface

        Returns:
            None
        """

        super().__init__(["Digital Abaco"], "0.1", "dp")
    
    def textInterface(self, lang="eng"):
        """
        Show the digital abaco interface

        Args:
            lang (str): language to use for the interface (default: "eng")

        Returns:
            None
        """

        while True:
            super().drowPrologue()
            print(self.languages[lang]["choiceFile"])
            print(self.languages[lang]["choiceExpression"])
            print(self.languages[lang]["choiceDictionary"])
            print(self.languages[lang]["choiceBaseConverter"])
            print(self.languages[lang]["choiceExit"])
            choice = input(self.languages[lang]["choice"])
            if choice == "1":
                fileName = input(self.languages[lang]["insertFile"])
                try:
                    with open(fileName, "r") as file:
                        expr = Expression(file.read())
                        expr.parseExpression()
                        print(expr.evaluate())
                except:
                    print(self.languages[lang]["invalidFile"])
            elif choice == "2":
                exprString = input(self.languages[lang]["insertExpression"])
                try:
                    expr = Expression(exprString)
                    expr.parseExpression()
                    print(expr.evaluate())
                except:
                    print(self.languages[lang]["invalidExpression"])
            elif choice == "3":
                for key in Expression.operators.keys():
                    print(key + ": " + self.languages[lang][key+"Description"])
            elif choice == "4":
                inputNumber = input(self.languages[lang]["insertNumber"])
                inputBase = input(self.languages[lang]["insertInputBase"])
                outputBase = input(self.languages[lang]["insertOutputBase"])
                try:
                    print(self.languages[lang]["resultNumberInBase"] + outputBase + ": " + str(BaseConverter.baseConverter(inputNumber, int(inputBase), int(outputBase))))
                except:
                    print(self.languages[lang]["invalidNumber"])
            elif choice == "5":
                print(self.languages[lang]["goodbye"])
                return
            else:
                print(self.languages[lang]["invalidChoice"])
            input(self.languages[lang]["pressEnter"])


if __name__ == "__main__":
    DigitalAbaco().textInterface()