from interfaces.interfaceDefinition import InterfaceDefinition
import re
from fractions import Fraction

class Complex_number:
    """
    class Complex_number represents a complex number

    Attributes:
        real (Fraction): real part of the complex number
        imaginary (Fraction): imaginary part of the complex number

    Methods:
        getReal: get the real part of the complex number
        getImaginary: get the imaginary part of the complex number
        add: add two complex numbers
        subtract: subtract two complex numbers
        multiply: multiply two complex numbers
        divide: divide two complex numbers
        __str__: represent the complex number as a string
    """

    def __init__(self, real, imaginary):
        """
        Initialize the complex number

        Args:
            r (int): real part of the complex number
            i (int): imaginary part of the complex number
        """
        self.real = Fraction(real).limit_denominator()
        self.imaginary = Fraction(imaginary).limit_denominator()

    def getReal(self):
        """
        Get the real part of the complex number

        Returns:
            int: the real part of the complex number
        """
        return self.real

    def getImaginary(self):
        """
        Get the imaginary part of the complex number

        Returns:
            int: the imaginary part of the complex number
        """
        return self.imaginary

    def add(self, other):
        """
        Add two complex numbers

        Args:
            other (Complex_number): the other complex number

        Returns:
            Complex_number: the sum of the two complex numbers
        """
        return Complex_number(self.real + other.real, self.imaginary + other.imaginary)

    def subtract(self, other):
        """
        Subtract two complex numbers

        Args:
            other (Complex_number): the other complex number

        Returns:
            Complex_number: the difference of the two complex numbers
        """
        return Complex_number(self.real - other.real, self.imaginary - other.imaginary)

    def multiply(self, other):
        """
        Multiply two complex numbers

        Args:
            other (Complex_number): the other complex number

        Returns:
            Complex_number: the product of the two complex numbers
        """
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex_number(real_part, imag_part)

    def divide(self, other):
        """
        Divide two complex numbers

        Args:
            other (Complex_number): the other complex number

        Returns:
            Complex_number: the division of the two complex numbers
        """
        denominator = other.real**2 + other.imaginary**2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex_number(real_part, imag_part)

    def __str__(self):
        """
        Represent the complex number as a string

        Returns:
            str: the complex number as a string
        """
        return f"{self.real}{' + ' if self.imaginary > 0 else ' - '}{abs(self.imaginary)}i"


class Node:
    """
    class Node represents a node in the expression tree

    Attributes:
        value (str): the value of the node
        left (Node): the left child of the node
        right (Node): the right child of the node
    """

    def __init__(self, value):
        """
        Initialize the node

        Args:
            value (str): the value of the node
        """
        self.value = value
        self.left = None
        self.right = None


class Calculator:
    """
    class Calculator represents a complex calculator

    Attributes:
        numbers (dict): the dictionary of variables
        expr (str): the expression to evaluate
        expression_tree (Node): the expression tree
    
    Static Attributes:
        pattern (str): the pattern to match a complex number
        operators (dict): the dictionary of operators

    Methods:
        getNumbers: get the list of variables
        setNumber: set a variable
        insertExpression: insert an expression
        buildExpressionTree: build the expression tree
        evaluateExpressionTree: evaluate the expression tree
        calculateResult: calculate the result of the expression
        setupVariables: set up the variables
        tryToConvert: try to convert a string to a complex number
        removeSpaces: remove spaces from a string
        reset: reset the calculator
        build_tree: build the expression tree
    """

    pattern = r'^([+\-]?)(\d*(\.\d*)?)\s*([+\-]?)(\d*(\.\d*)?)(i?)$'
    operators = {
        '+': Complex_number.add, 
        '-': Complex_number.subtract, 
        '*': Complex_number.multiply, 
        '/': Complex_number.divide
    }

    def __init__(self):
        """
        Initialize the calculator

        Returns:
            None
        """
        self.numbers = {}
        self.expr = ''
        self.expression_tree = None
    
    def getNumbers(self):
        """
        Get the list of variables

        Returns:
            list: the list of variables
        """
        return [var for var in self.numbers.keys()]

    def setNumber(self, key, value):
        """
        Set a variable

        Args:
            key (str): the name of the variable
            value (Complex_number): the value of the variable

        Returns:
            None
        """
        self.numbers[key] = value

    def insertExpression(self, e):
        """
        Insert an expression

        Args:
            e (str): the expression to evaluate

        Returns:
            None
        """
        if True not in [op in e for op in self.operators.keys()]:
            raise Exception("ERROR -> no operator found.")
        exprInput = e
        expr = self.removeSpaces(exprInput)
        if not expr:
            raise Exception("ERROR -> empty expression.")
        self.expr = expr
        self.buildExpressionTree()

    def buildExpressionTree(self):
        """
        Build the expression tree

        Returns:
            None
        """
        self.expression_tree = self.build_tree(self.expr)

    def evaluateExpressionTree(self, node):
        """
        Evaluate the expression tree

        Args:
            node (Node): the node of the expression tree

        Returns:
            Complex_number: the result of the expression
        """
        if node.value.isalnum():
            return self.numbers[node.value]
        else:
            left_result = self.evaluateExpressionTree(node.left)
            right_result = self.evaluateExpressionTree(node.right)
            operation = self.operators[node.value]
            return operation(left_result, right_result)

    def calculateResult(self):
        """
        Calculate the result of the expression

        Returns:
            Complex_number: the result of the expression
        """
        return self.evaluateExpressionTree(self.expression_tree)

    def setupVariables(self):
        """
        Set up the variables

        Returns:
            None
        """
        variables = set([self.expr[i] for i in range(len(self.expr)) if self.expr[i].isalpha()])
        self.numbers = {name: None for name in variables}

    def tryToConvert(self, expr: str) -> Complex_number:
        """
        Try to convert a string to a complex number

        Args:
            expr (str): the string to convert

        Returns:
            Complex_number: the complex number
        """
        match = re.match(self.pattern, expr)
        if match:
            real_positive = True if match.group(1) == '+' or match.group(1) == '' else False
            real_part = float(match.group(2))
            if not real_positive:
                real_part = real_part * -1
            if match.group(4) == '' and match.group(7) == 'i':
                imaginary_part = real_part
                real_part = 0
                imaginary_positive = True
            else:
                imaginary_positive = True if match.group(4) == '+' or match.group(4) == '' else False
                imaginary_part = float(match.group(5)) if match.group(5) != '' else 1
            if match.group(7) != 'i':
                if (match.group(4) != '' or match.group(5) != ''):
                    raise Exception("ERROR -> imaginary part not found.")
                imaginary_part = 0
                
            if not imaginary_positive:
                imaginary_part = imaginary_part * -1
            return Complex_number(real_part, imaginary_part)
        else:
            return None

    def removeSpaces(self, string):
        """
        Remove spaces from a string

        Args:
            string (str): the string to modify

        Returns:
            str: the string without spaces
        """
        return string.replace(" ", "")    

    def reset(self):
        """
        Reset the calculator

        Returns:
            None
        """
        self.numbers = {}
        self.expr = ''
        self.expression_tree = None

    def build_tree(self, expression):
        """
        Build the expression tree

        Args:
            expression (str): the expression to evaluate

        Returns:
            Node: the root of the expression tree
        """
        def priority(op):
            if op == '+' or op == '-':
                return 1
            elif op == '*' or op == '/':
                return 2
            else:
                return 0  

        def infix_to_postfix(infix):
            output = []
            operators = []
            for token in infix:
                if token.isalnum():
                    output.append(token)
                elif token == '(':
                    operators.append(token)
                elif token == ')':
                    while operators and operators[-1] != '(':
                        output.append(operators.pop())
                    operators.pop() 
                else:
                    while operators and priority(operators[-1]) >= priority(token):
                        output.append(operators.pop())
                    operators.append(token)
            while operators:
                output.append(operators.pop())
            return output

        def build_tree_from_postfix(postfix):
            stack = []
            for token in postfix:
                if token.isalnum():
                    stack.append(Node(token))
                else:
                    right = stack.pop()
                    left = stack.pop()
                    operator_node = Node(token)
                    operator_node.left = left
                    operator_node.right = right
                    stack.append(operator_node)
            return stack[0]

        tokens = []
        current_token = ''
        for char in expression:
            if char.isalnum():
                current_token += char
            elif current_token:
                tokens.append(current_token)
                current_token = ''
                tokens.append(char)
            else:
                tokens.append(char)
        if current_token:
            tokens.append(current_token)
        postfix_expression = infix_to_postfix(tokens)
        expression_tree = build_tree_from_postfix(postfix_expression)
        return expression_tree


class ComplexCalculatorInterface(InterfaceDefinition):
    """
    class ComplexCalculatorInterface represents the interface of the complex calculator

    Attributes:
        calculator (Calculator): the complex calculator
    
    Static Attributes:
        languages (dict): the dictionary of languages

    Methods:
        textInterface: show the interface
    """

    languages = {
        "ita":{
            "insertExpression": "Inserisci l'espressione (vuoto per uscire): ",
            "assignVariables": "Assegna le variabili:",
            "result": "Risultato: ",
            "genericError": "Si è verificato un errore.",
            "expectedFormat": "Formato atteso: 3+2i",
            "pressEnterToContinue": "\nPremi Invio per continuare...",
            "invalidInput": "Input non valido.",
            "goodbye": "Arrivederci!"
        },
        "eng": {
            "insertExpression": "Insert the expression (blank to exit): ",
            "assignVariables": "Assign the variables:",
            "result": "Result: ",
            "genericError": "An error occurred.",
            "expectedFormat": "Expected format: 3+2i",
            "pressEnterToContinue": "\nPress Enter to continue...",
            "invalidInput": "Invalid input.",
            "goodbye": "Goodbye!"
        }
    }

    def __init__(self, calculator = None):
        """
        Initialize the complex calculator interface

        Args:
            calculator (Calculator): the complex calculator

        Returns:
            None
        """
        self.calculator = calculator if calculator != None else Calculator()
        super().__init__(["Useless Complex caculator"], "0.1", "sb")

    def textInterface(self, lang="eng"):
        """
        Show the interface

        Args:
            lang (str): the language of the interface

        Returns:
            None
        """
        while True:
            super().drowPrologue()
            self.calculator.reset()
            expr = input(self.languages[lang]["insertExpression"])
            if expr == '':
                print(self.languages[lang]["goodbye"])
                return
            try:
                self.calculator.insertExpression(expr)
                self.calculator.setupVariables()
                print(self.languages[lang]["assignVariables"])
                for var in sorted(self.calculator.getNumbers()):
                    number_expr = input(f"{var}: ")
                    number = self.calculator.tryToConvert(self.calculator.removeSpaces(number_expr))
                    while number is None:
                        number_expr = input(f"{var}: ")
                        number = self.calculator.tryToConvert(self.calculator.removeSpaces(number_expr))
                    self.calculator.setNumber(var, number)
                print(f"{self.languages[lang]['result']}{self.calculator.calculateResult()}")
            except:
                print(self.languages[lang]["genericError"])
            input(self.languages[lang]["pressEnterToContinue"])


if __name__ == "__main__":
    ComplexCalculatorInterface().textInterface()