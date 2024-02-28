from interfaces.interfaceDefinition import InterfaceDefinition

class push:
    """
    Class that represent the PUSH command
    """
    def __call__(self, executor, value):
        executor.stack.append(value)

    def toCpp(self, executor, value):
        return f"\n        stack.push(Element(\"{value}\"));\n"

class pop:
    """
    Class that represent the POP command
    """
    def __call__(self, executor):
        executor.stack.pop()

    def toCpp(self, executor):
        return "\n        stack.pop();\n"

class print_:
    """
    Class that represent the PRINT command
    """
    def __call__(self, executor):
        print(executor.stack[-1])

    def toCpp(self, executor):
        return f"\n        std::cout << stack.top() << std::endl;\n"

class add:
    """
    Class that represent the ADD command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop() + executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele1 + ele2);\n"

class sub:
    """
    Class that represent the SUB command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop(-2) - executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele2 - ele1);\n"

class mul:
    """
    Class that represent the MUL command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop() * executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele1 * ele2);\n"

class div:
    """
    Class that represent the DIV command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop(-2) / executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele2 / ele1);\n"

class swap:
    """
    Class that represent the SWAP command
    """
    def __call__(self, executor):
        executor.stack[-1], executor.stack[-2] = executor.stack[-2], executor.stack[-1]

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele1);\n        stack.push(ele2);\n"

class dup:
    """
    Class that represent the DUP command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack[-1])

    def toCpp(self, executor):
        return "\n        stack.push(stack.top());\n"

class end:
    """
    Class that represent the END command
    """
    def __call__(self, executor):
        executor.terminated = True

    def toCpp(self, executor):
        return "\n        return 0;\n"

class clear:
    """
    Class that represent the CLEAR command
    """
    def __call__(self, executor):
        executor.stack.clear()

    def toCpp(self, executor):
        return "\n        while(!stack.empty())\n            stack.pop();\n"

class mod:
    """
    Class that represent the MOD command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop(-2) % executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele2 % ele1);\n"

class min_:
    """
    Class that represent the MIN command
    """
    def __call__(self, executor):
        executor.stack.append(min(executor.stack.pop(), executor.stack.pop()))

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(std::min(ele1.intValue, ele2.intValue));\n"

class max_:
    """
    Class that represent the MAX command
    """
    def __call__(self, executor):
        executor.stack.append(max(executor.stack.pop(-2), executor.stack.pop()))

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(std::max(ele1.intValue, ele2.intValue));\n"

class equal:
    """
    Class that represent the EQUAL command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop(-2) == executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele1 == ele2);\n"

class greater:
    """
    Class that represent the GREATER command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop(-2) > executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele1 < ele2);\n"

class less:
    """
    Class that represent the LESS command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop(-2) < executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele1 > ele2);\n"

class not_:
    """
    Class that represent the NOT command
    """
    def __call__(self, executor):
        executor.stack.append(not executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        stack.push(!ele1);\n"

class and_:
    """
    Class that represent the AND command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop(-2) and executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele1 && ele2);\n"

class or_:
    """
    Class that represent the OR command
    """
    def __call__(self, executor):
        executor.stack.append(executor.stack.pop(-2) or executor.stack.pop())

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        stack.push(ele1 || ele2);\n"

class goto:
    """
    Class that represent the GOTO command
    """
    def __call__(self, executor, offset=0):
        if executor.stack.pop():
            if int(executor.stack[-1]) == executor.stack[-1]:
                executor.index = executor.stack.pop()+offset-1

    def toCpp(self, executor, offset):
        s = "\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        if(ele1.intValue){\n            switch(ele2.intValue+"+str(offset)+"){\n"
        for i in range(len(executor.instructions)-1):
            s += f"                case {str(i)}:\n                    goto instr_{str(i)};\n"
        s += "            }\n        }\n"
        return s

class num:
    """
    Class that represent the NUM command
    """
    def __call__(self, executor):
        executor.stack.append(len(executor.stack))

    def toCpp(self, executor):
        return "\n        stack.push(stack.size());\n"

class input_:
    """
    Class that represent the INPUT command
    """
    def __call__(self, executor):
        executor.stack.append(input("INSERT VALUE: "))

    def toCpp(self, executor):
        return "\n        std::cout<<\"INSERT VALUE: \";\n        std::cin >> str1;\n        stack.push(Element(str1));\n"

class int_:
    """
    Class that represent the INT command
    """
    def __call__(self, executor):
        executor.stack.append(int(executor.stack.pop()))

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        if(ele1.type==1)\n            stack.push(ele1);\n        if (ele1.type==2)\n            stack.push(Element(std::stoi(ele1.stringValue)));\n        if(ele1.type==3)\n            stack.push(Element((int) ele1.floatValue));\n"

class float_:
    """
    Class that represent the FLOAT command
    """
    def __call__(self, executor):
        executor.stack.append(float(executor.stack.pop()))

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        if(ele1.type==1)\n            stack.push((float) ele1.intValue);\n        if (ele1.type==2)\n            stack.push(Element(std::stof(ele1.stringValue)));\n        if(ele1.type==3)\n            stack.push(ele1);\n"

class string:
    """
    Class that represent the STRING command
    """
    def __call__(self, executor):
        executor.stack.append(str(executor.stack.pop()))

    def toCpp(self, executor):
        return "\n        ele1 = stack.top();\n        stack.pop();\n        if(ele1.type==1)\n            stack.push(Element(std::to_string(ele1.intValue)));\n        if (ele1.type==2)\n            stack.push(ele1);\n        if(ele1.type==3)\n            stack.push(std::to_string(ele1.floatValue));\n"

class comment:
    """
    Class that represent the COMMENT command
    """
    def __call__(self, executor):
        pass

    def toCpp(self, executor):
        return "\n"

class store:
    """
    Class that represent the STORE command
    """
    def __call__(self, executor):
        executor.variables[executor.stack.pop()] = executor.stack.pop()

    def toCpp(self, executor):
        return  f"\n        ele1 = stack.top();\n        stack.pop();\n        ele2 = stack.top();\n        stack.pop();\n        variables[ele2.stringValue] = ele1;\n"

class load:
    """
    Class that represent the LOAD command
    """
    def __call__(self, executor):
        executor.stack.append(executor.variables[executor.stack.pop()])

    def toCpp(self, executor):
        return f"\n        ele1 = stack.top();\n        stack.pop();\n        stack.push(variables[ele1.stringValue]);\n"

class import_:
    """
    Class that represent the IMPORT command
    """
    def __call__ (self, executor):
        filename = executor.stack.pop()
        offset = len(executor.instructions)
        with open(filename, "r") as file:
            for line in file:
                executor.addInstruction(line, offset)
    def toCpp(self, executor):
        return "\n"

class define:
    """
    Class that represent the DEFINE command
    """
    def __call__(self, executor):
        numberOfInstructions = executor.stack.pop()
        name = executor.stack.pop()
        instructions = []
        for i in range(numberOfInstructions):
            istr = Instruction()
            istr.command = executor.stack.pop()
            instructions.append(istr)
            if instructions[-1].command == "PUSH":
                instructions[-1].value = executor.stack.pop()
        executor.functions[name] = instructions

    def toCpp(self, executor):
        return "\n"

class compile:
    """
    Class that represent the COMPILE command
    """
    def __call__(self, executor):
        filename = executor.stack.pop()
        s = """
#include <iostream>
#include <stack>
#include <unordered_map>
#include <string>

struct Element {
    int intValue;
    std::string stringValue;
    float floatValue;
    int type;
    Element() : intValue(0), stringValue(""), floatValue(0.0), type(0) {}
    Element(int value) : intValue(value), stringValue(""), floatValue(0.0), type(1) {}
    Element(std::string value) : intValue(0), stringValue(value), floatValue(0.0), type(2) {}
    Element(float value) : intValue(0), stringValue(""), floatValue(value), type(3) {}
    Element(const Element& other) : intValue(other.intValue), stringValue(other.stringValue), floatValue(other.floatValue), type(other.type) {}
    Element& operator=(const Element& other) {
        intValue = other.intValue;
        stringValue = other.stringValue;
        floatValue = other.floatValue;
        type = other.type;
        return *this;
    }
    Element operator+(const Element& other) const {
        if (type == 2 && other.type == 2) {
            return Element(stringValue + other.stringValue);
        } else if (type == 3 && other.type == 3) {
            return Element(floatValue + other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue + other.intValue);
        }
        return Element();
    }
    Element operator-(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue - other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue - other.intValue);
        }
        return Element();
    }
    Element operator*(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue * other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue * other.intValue);
        }
        return Element();
    }
    Element operator/(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue / other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue / other.intValue);
        }
        return Element();
    }
    Element operator%(const Element& other) const {
        if (type == 1 && other.type == 1) {
            return Element(intValue % other.intValue);
        }
        return Element();
    }
    Element operator>(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue > other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue > other.intValue);
        }
        return Element();
    }
    Element operator<(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue < other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue < other.intValue);
        }
        return Element();
    }
    Element operator>=(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue >= other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue >= other.intValue);
        }
        return Element();
    }
    Element operator<=(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue <= other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue <= other.intValue);
        }
        return Element();
    }
    Element operator==(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue == other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue == other.intValue);
        } else if (type == 2 && other.type == 2) {
            return Element(stringValue == other.stringValue);
        }
        return Element();
    }
    Element operator!=(const Element& other) const {
        if (type == 3 && other.type == 3) {
            return Element(floatValue != other.floatValue);
        } else if (type == 1 && other.type == 1) {
            return Element(intValue != other.intValue);
        } else if (type == 2 && other.type == 2) {
            return Element(stringValue != other.stringValue);
        }
        return Element();
    }
    Element operator&&(const Element& other) const {
        if (type == 1 && other.type == 1) {
            return Element(intValue && other.intValue);
        }
        return Element();
    }
    Element operator||(const Element& other) const {
        if (type == 1 && other.type == 1) {
            return Element(intValue || other.intValue);
        }
        return Element();
    }
    Element operator!() const {
        if (type == 1) {
            return Element(!intValue);
        }
        return Element();
    }
    friend std::ostream& operator<<(std::ostream& os, const Element& ele) {
        if (ele.type == 1) {
            os << ele.intValue;
        } else if (ele.type == 2) {
            os << ele.stringValue;
        } else if (ele.type == 3) {
            os << ele.floatValue;
        }
        return os;
    }
};

int main() {
    std::stack<Element> stack;
    std::unordered_map<std::string, Element> variables;
    Element ele1, ele2;
    std::string str1;
"""
        for index, instruction in enumerate(executor.instructions):
            if index != len(executor.instructions)-1:
                s += f"    instr_{index}: //{instruction.command}{instruction.toCpp(executor)}"
        s = s + "\n}"
        with open(filename, "w") as file:
            file.write(s)

    def toCpp(self, executor):
        return "\n"

class include:
    """
    Class that represent the INCLUDE command
    """
    def __call__ (self, executor):
        number = 0
        offset = len(executor.instructions)
        filename = executor.stack.pop()
        with open(filename, "r") as file:
            for line in file:
                executor.addInstruction(line, offset)
                number += 1
        executor.index += number

    def toCpp(self, executor):
        return "\n"

class Instruction:
    """
    Class that represent an instruction

    Attributes:
        string (str): the string of the instruction
        command (str): the command of the instruction
        value (str): the value of the instruction
        decoration (str): the decoration of the instruction
        offset (int): the offset of the instruction
    
    Methods:
        parse(string, offset): parse the string of the instruction
        execute(executor): execute the instruction
        toCpp(executor): return the C++ code of the instruction
    """
    def __init__(self):
        """
        Constructor of the class
        
        Returns:
            None
        """
        self.string = ""
        self.command = ""
        self.value = None
        self.decoration = None
        self.offset = 0
    
    def parse(self, string, offset=0):
        """
        Parse the string of the instruction

        Args:
            string (str): the string of the instruction
            offset (int): the offset of the instruction

        Returns:
            None
        """
        self.string = string
        self.offset = offset
        self.command = string.split()[0].upper()
        if len(string.split()) > 1 and self.command != "PUSH":
            self.decoration = string.split()[1]
        elif len(string.split()) > 1 and self.command == "PUSH":
            self.value = string.split()[1]
        if len(string.split()) > 2:
            self.decoration = string.split()[2]
    
    def execute(self, executor):
        """
        Execute the instruction

        Args:
            executor (Executor): the executor of the instruction

        Returns:
            None
        """
        if self.command == "PUSH":
            executor.instructionsDict[self.command](executor, self.value)
        elif self.command == "GOTO":
            executor.instructionsDict[self.command](executor, self.offset)
        elif self.command in executor.functions:
            for instruction in executor.functions[self.command]:
                instruction.execute(executor)
        else:
            executor.instructionsDict[self.command](executor)
    
    def toCpp(self, executor):
        """
        Return the C++ code of the instruction

        Args:
            executor (Executor): the executor of the instruction

        Returns:
            str: the C++ code of the instruction
        """
        if self.command == "PUSH":
            return executor.instructionsDict[self.command].toCpp(executor, self.value)
        elif self.command == "GOTO":
            return executor.instructionsDict[self.command].toCpp(executor, self.offset)
        elif self.command in executor.functions:
            s = ""
            for instruction in executor.functions[self.command]:
                s += instruction.toCpp()
            return s
        else:
            return executor.instructionsDict[self.command].toCpp(executor)

class Executor:
    """
    Class that represent the executor of the instructions

    Attributes:
        variables (dict): the dictionary of the variables of the executor
        stack (list): the stack of the executor
        instructions (list): the list of the instructions of the executor
        functions (dict): the functions of the executor
        index (int): the index of the executor, representing the current instruction
        terminated (bool): the boolean value representing if the executor is terminated
        instructionsDict (dict): the dictionary of the instructions objects of the executor

    Methods:
        addInstruction(instruction, offset): add an instruction to the executor
        executeInstruction(): execute the current instruction of the executor
        execute(): execute all the instructions of the executor
        resetIndex(): reset the index of the executor
        reset(): reset the executor
    """

    def __init__(self):
        """
        Constructor of the class

        Returns:
            None
        """
        self.variables = {}
        self.stack = []
        self.instructions = []
        self.functions = {}
        self.index = 0
        self.terminated = False
        self.instructionsDict = {
            "PUSH": push(),
            "POP": pop(),
            "PRINT": print_(),
            "ADD": add(),
            "SUB": sub(),
            "MUL": mul(),
            "DIV": div(),
            "SWAP": swap(),
            "DUP": dup(),
            "CLEAR": clear(),
            "MOD": mod(),
            "MIN": min_(),
            "MAX": max_(),
            "EQUAL": equal(),
            "GREATER": greater(),
            "LESS": less(),
            "NOT": not_(),
            "AND": and_(),
            "OR": or_(),
            "GOTO": goto(),
            "NUM": num(),
            "INPUT": input_(),
            "INT": int_(),
            "FLOAT": float_(),
            "STRING": string(),
            "COMMENT": comment(),
            "STORE": store(),
            "LOAD": load(),
            "IMPORT": import_(),
            "END": end(),
            "DEFINE": define(),
            "COMPILE": compile(),
            "INCLUDE": include()
        }
    
    def addInstruction(self, instruction, offset=0):
        """
        Add an instruction to the executor

        Args:
            instruction (str): the instruction to add
            offset (int): the offset of the instruction

        Returns:
            None
        """
        instr = Instruction()
        instr.parse(instruction, offset)
        self.instructions.append(instr)
    
    def executeInstruction(self):
        """
        Execute the current instruction of the executor

        Returns:
            None
        """
        instruction = self.instructions[self.index]
        instruction.execute(self)

    def execute(self):
        """
        Execute all the instructions of the executor

        Returns:
            None
        
        Note:
            This method starts the execution of the instructions from the current index, and the index is not resetted after the execution
        """
        while not self.terminated and self.index < len(self.instructions):
            try:
                self.executeInstruction()
            except Exception as e:
                raise e
            finally:
                self.index += 1
    
    def resetIndex(self):
        """
        Reset the index of the executor

        Returns:
            None
        """
        self.index = 0
    
    def reset(self):
        """
        Reset the executor

        Returns:
            None
        """
        self.variables = {}
        self.stack = []
        self.instructions = []
        self.functions = {}
        self.index = 0
        self.terminated = False

class NALM(InterfaceDefinition):
    """
    Class that represent the NALM program
    
    Static Attributes:
        languages (dict): dictionary that contains all the languages supported by the program
        
    Methods:
        textInterface(lang): show the NALM interface
    """

    languages = {
        "ita":{
            "help": """NALM è un linguaggio di programmazione testuale. I comandi disponibili sono:
PUSH <valore>     -->    Inserisce un valore nello stack
POP               -->    Rimuove l'ultimo valore inserito nello stack
PRINT             -->    Stampa l'ultimo valore inserito nello stack
ADD               -->    Somma gli ultimi due valori inseriti nello stack
SUB               -->    Sottrae il penultimo valore inserito nello stack dall'ultimo
MUL               -->    Moltiplica gli ultimi due valori inseriti nello stack  
DIV               -->    Divide il penultimo valore inserito nello stack per l'ultimo
SWAP              -->    Scambia i due valori in cima allo stack
DUP               -->    Duplica l'ultimo valore inserito nello stack
CLEAR             -->    Svuota lo stack
MOD               -->    Calcola il resto della divisione tra il penultimo valore inserito nello stack e l'ultimo
MIN               -->    Restituisce il minore tra i due ultimi valori inseriti nello stack
MAX               -->    Restituisce il maggiore tra i due ultimi valori inseriti nello stack
EQUAL             -->    Restituisce True se i due ultimi valori inseriti nello stack sono uguali
GREATER           -->    Restituisce True se il penultimo valore inserito nello stack è maggiore dell'ultimo
LESS              -->    Restituisce True se il penultimo valore inserito nello stack è minore dell'ultimo
NOT               -->    Restituisce il valore booleano opposto all'ultimo valore inserito nello stack
AND               -->    Restituisce True se entrambi gli ultimi due valori inseriti nello stack sono True
OR                -->    Restituisce True se almeno uno degli ultimi due valori inseriti nello stack è True
GOTO              -->    Salta a un'istruzione in base al valore inserito nello stack
NUM               -->    Restituisce il numero di valori inseriti nello stack
INPUT             -->    Chiede un input all'utente e lo inserisce nello stack
INT               -->    Trasforma l'ultimo valore inserito nello stack in un intero
FLOAT             -->    Trasforma l'ultimo valore inserito nello stack in un float
STRING            -->    Trasforma l'ultimo valore inserito nello stack in una stringa
COMMENT           -->    Ignora l'istruzione
STORE             -->    Salva un valore nello stack con una chiave
LOAD              -->    Carica un valore dallo stack con una chiave
IMPORT            -->    Importa un file di istruzioni, il cui nome è inserito nello stack
END               -->    Termina l'esecuzione del programma
DEFINE            -->    Definisce una funzione
            """,
            "goodbye": "Arrivederci",
            "error": "Si è verificato un errore"
        },
        "eng":{
            "help": """NALM is a text-based programming language. The available commands are:
PUSH <value>      -->    Pushes a value into the stack
POP               -->    Removes the last value pushed into the stack
PRINT             -->    Prints the last value pushed into the stack
ADD               -->    Sums the last two values pushed into the stack
SUB               -->    Subtracts the penultimate value pushed into the stack from the last one
MUL               -->    Multiplies the last two values pushed into the stack
DIV               -->    Divides the penultimate value pushed into the stack by the last one
SWAP              -->    Swaps the two values on top of the stack
DUP               -->    Duplicates the last value pushed into the stack
CLEAR             -->    Empties the stack
MOD               -->    Calculates the remainder of the division between the penultimate value pushed into the stack and the last one
MIN               -->    Returns the smallest between the last two values pushed into the stack
MAX               -->    Returns the greatest between the last two values pushed into the stack
EQUAL             -->    Returns True if the last two values pushed into the stack are equal
GREATER           -->    Returns True if the penultimate value pushed into the stack is greater than the last one
LESS              -->    Returns True if the penultimate value pushed into the stack is less than the last one
NOT               -->    Returns the opposite boolean value of the last value pushed into the stack
AND               -->    Returns True if both the last two values pushed into the stack are True
OR                -->    Returns True if at least one of the last two values pushed into the stack is True
GOTO              -->    Jumps to an instruction based on the value pushed into the stack
NUM               -->    Returns the number of values pushed into the stack
INPUT             -->    Asks for an input to the user and pushes it into the stack
INT               -->    Transforms the last value pushed into the stack into an integer
FLOAT             -->    Transforms the last value pushed into the stack into a float
STRING            -->    Transforms the last value pushed into the stack into a string
COMMENT           -->    Ignores the instruction
STORE             -->    Saves a value into the stack with a key
LOAD              -->    Loads a value from the stack with a key
IMPORT            -->    Imports an instruction file, whose name is pushed into the stack
END               -->    Terminates the program execution
DEFINE            -->    Defines a function
            """,
            "goodbye": "Goodbye",
            "error": "An error occurred"
        }
    }
    
    def __init__(self):
        """
        Constructor of the class

        Returns:
            None
        """
        super().__init__(["NALM"], "0.1", "dp")
    
    def textInterface(self, lang="eng"):
        """
        Show the NALM interface

        Args:
            lang (str): the language of the interface

        Returns:
            None
        """
        executor = Executor()
        super().drowPrologue()
        while True:
            try:
                rawChoice = input(">>> ")
                if(rawChoice.upper() == "HELP"):
                    print(self.languages[lang]["help"])
                else:
                    executor.addInstruction(rawChoice)
                    executor.execute()
                    if(executor.terminated):
                        print(self.languages[lang]["goodbye"])
                        return
            except Exception:
                print(self.languages[lang]["error"])

if __name__ == "__main__":
    nalm = NALM().textInterface()
