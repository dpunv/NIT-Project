import re
from fractions import Fraction

class Complex_number:
    def __init__(self, r, i):
        self.real = Fraction(r).limit_denominator()
        self.imaginary = Fraction(i).limit_denominator()

    def getReal(self):
        return self.real

    def getImaginary(self):
        return self.imaginary

    def add(self, other):
        return Complex_number(self.real + other.real, self.imaginary + other.imaginary)

    def subtract(self, other):
        return Complex_number(self.real - other.real, self.imaginary - other.imaginary)

    def multiply(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex_number(real_part, imag_part)

    def divide(self, other):
        denominator = other.real**2 + other.imaginary**2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex_number(real_part, imag_part)

    def __str__(self):
        return f"{self.real}{' + ' if self.imaginary > 0 else ' - '}{abs(self.imaginary)}i"


"""
class Node represents a node in the expression tree
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Calculator:

    pattern = r'^([+\-]?)(\d*(\.\d*)?)\s*([+\-]?)(\d*(\.\d*)?)(i?)$'
    operators = {
        '+': Complex_number.add, 
        '-': Complex_number.subtract, 
        '*': Complex_number.multiply, 
        '/': Complex_number.divide
    }

    def __init__(self):
        self.numbers = {}
        self.expr = ''
        self.expression_tree = None

    
    def getNumbers(self):
        return [var for var in self.numbers.keys()]


    def setNumber(self, key, value):
        self.numbers[key] = value


    def insertExpression(self, e):
        exprInput = e
        expr = self.removeSpaces(exprInput)
        while len(expr)%2 == 0 or len(expr) < 3:
            exprInput = input()
            expr = self.removeSpaces(exprInput)
        self.expr = expr
        self.buildExpressionTree()


    def buildExpressionTree(self):
        self.expression_tree = self.build_tree(self.expr)


    def evaluateExpressionTree(self, node):
        if node.value.isalnum():
            return self.numbers[node.value]
        else:
            left_result = self.evaluateExpressionTree(node.left)
            right_result = self.evaluateExpressionTree(node.right)
            operation = self.operators[node.value]
            return operation(left_result, right_result)


    def calculateResult(self):
        result = self.evaluateExpressionTree(self.expression_tree)
        print("Result:", result)


    def setupVariables(self):
        variables = set([self.expr[i] for i in range(len(self.expr)) if self.expr[i].isalpha()])
        self.numbers = {name: None for name in variables}


    def tryToConvert(self, expr: str) -> Complex_number:
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
        return string.replace(" ", "")    


    def reset(self):
        self.numbers = {}
        self.expr = ''
        self.expression_tree = None


    def build_tree(self, expression):
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

    languages = {
        "ita":{
            "insertExpression": "",
            "assignVariables": "",
            "result": "",
            "genericError": "",
            "expectedFormat": "",
            "pressEnterToContinue": "",
            "invalidInput": "",
            "goodbye": ""
        },
        "eng": {
            "insertExpression": "",
            "assignVariables": "",
            "result": "",
            "genericError": "",
            "expectedFormat": "",
            "pressEnterToContinue": "",
            "invalidInput": "",
            "goodbye": ""
        }
    }

    def __init__(self, calculator = None):
        self.calculator = calculator if calculator != None else Calculator()
        super().__init__(["Useless Complex caculator"], "0.1", "sb")

    def textInterface(self, lang):
        while True:
            super().drowPrologue()
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



calc = Calculator()
calc.insertExpression()
calc.setupVariables()
calc.calculateResult()