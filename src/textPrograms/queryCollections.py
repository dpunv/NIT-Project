from interfaces.interfaceDefinition import InterfaceDefinition
import json
import os

class Table:
    """
    Class that represent a table

    Attributes:
        name (str): name of the table
        columns (list): list of columns, each column is a dictionary with the following keys:
            - name (str): name of the column
            - description (str): description of the column
            - required (bool): if the column is required
            - autoIncrement (bool): if the column is auto increment
            - unique (bool): if the column is unique
        data (list): list of data, each data is a dictionary
    
    Methods:
        addData: add data to the table
        getColumns: return the columns of the table
        queryData: query the data of the table
        addColumn: add a column to the table
        modifyData: modify the data of the table
        deleteData: delete the data of the table
        getColumnsRaw: return the columns of the table
        getDataRaw: return the data of the table
    """

    def __init__(self, name, columns):
        """
        Initialize the table

        Args:
            name (str): name of the table
            columns (list): list of columns, each column is a dictionary with the following keys:
                - name (str): name of the column
                - description (str): description of the column
                - required (bool): if the column is required
                - autoIncrement (bool): if the column is auto increment
                - unique (bool): if the column is unique

        Returns:
            None
        """
        self.name = name
        self.columns = columns
        self.data = []
    
    def addData(self, data: dict):
        """
        Add data to the table

        Args:
            data (dict): data to add to the table

        Returns:
            None
        """
        for name in data.keys():
            if name not in [column["name"] for column in self.columns]:
                raise ValueError(f"Wrong data: column {name} not in this table")
        for index, value in enumerate(self.columns):
            if value["autoIncrement"] and value["name"] not in data.keys():
                data[value["name"]] = (max([column[value["name"]] for column in self.data]) + 1) if len(self.data) > 0 else 1
            if value["name"] not in data.keys() and value["required"]:
                raise ValueError(f"Wrong data: column {value['name']} is required")
            if value["unique"] and value["name"] in data.keys():
                if any(row[value["name"]] == data[value["name"]] for row in self.data):
                    raise ValueError(f"Wrong data: column {value['name']} must be unique")
        for row in self.data:
            if all(row[key] == value for key, value in data.items()):
                raise ValueError(f"Wrong data: row {data} already exists")
        self.data.append(data)

    def getColumns(self):
        """
        Return the columns of the table

        Returns:
            list: columns of the table
        """
        return [column["name"] for column in self.columns]
    
    def queryData(self, query: dict):
        """
        Query the data of the table

        Args:
            query (dict): query to execute
            
        Returns:
            list: data of the table
        """
        result = []
        for row in self.data:
            if all(row[key] == value for key, value in query["WHERE"].items()):
                object = {}
                if "*" in query["SELECT"]:
                    object = row
                else:
                    for key in query["SELECT"]:
                        if key not in [column["name"] for column in self.columns]:
                            raise ValueError(f"Wrong query: column {key} not in this table")
                        object[key] = row[key]    
                result.append(object)
        return result

    def addColumn(self, name: str, description: str, required: bool, autoIncrement: bool, unique: bool):
        """
        Add a column to the table

        Args:
            name (str): name of the column
            description (str): description of the column
            required (bool): if the column is required
            autoIncrement (bool): if the column is auto increment
            unique (bool): if the column is unique

        Returns:
            None
        """
        if name in [[column["name"] for column in self.columns]]:
            raise ValueError(f"Column {name} already exists")
        self.columns["name"] = name
        self.columns["description"] = description
        self.columns["required"] = required
        self.columns["autoIncrement"] = autoIncrement
        self.columns["unique"] = unique
    
    def modifyData(self, oldData, newData):
        """
        Modify the data of the table

        Args:
            oldData (dict): old data
            newData (dict): new data

        Returns:
            bool: True if the data has been modified, False otherwise
        """
        for row in self.data:
            if all(row[key] == value for key, value in oldData.items()):
                for key, value in newData.items():
                    row[key] = value
                return True
        return False
    
    def deleteData(self, data):
        """
        Delete the data of the table

        Args:
            data (dict): data to delete

        Returns:
            bool: True if the data has been deleted, False otherwise
        """
        for row in self.data:
            if all(row[key] == value for key, value in data.items()):
                self.data.remove(row)
                return True
        return False
    
    def getColumnsRaw(self):
        """
        Return the columns of the table
        
        Returns:
            list: columns of the table
        """
        return self.columns
    
    def getDataRaw(self):
        """
        Return the data of the table

        Returns:
            list: data of the table
        """
        return self.data

class CollectionDatabase:
    """
    Class that represent a collection database

    Attributes:
        fileName (str): name of the file
        tables (dict): dictionary of tables

    Methods:
        createDatabase: create a database
        load: load the database
        save: save the database
        createTable: create a table
        getTable: get a table
        deleteTable: delete a table
        query: query the database
        addColumn: add a column to the database
        modifyData: modify the data of the database
        deleteData: delete the data of the database
        addData: add data to the database
        getTables: get the tables of the database
        getTableColumns: get the columns of a table
    """

    def __init__(self, fileName=None):
        """
        Initialize the collection database

        Args:
            fileName (str): name of the file

        Returns:
            None
        """
        self.fileName = fileName
        self.tables = {}
        if fileName is not None:
            self.load()
    
    def createDatabase(self, path, name):
        """
        Create a database

        Args:
            path (str): path of the database
            name (str): name of the database

        Returns:
            None
        """
        if os.path.exists(path) and os.path.isdir(path):
            self.fileName = os.path.join(path, name)
            self.tables = {}
            self.save()
        else:
            raise ValueError(f"Path {path} does not exist or is not a directory")

    def load(self):
        """
        Load the database

        Returns:
            None
        """
        if os.path.exists(self.fileName):
            with open(self.fileName, "r") as file:
                data = json.load(file)
                for table in data:
                    self.tables[table] = Table(table, data[table]["columns"])
                    for row in data[table]["data"]:
                        self.tables[table].addData(row)
        else:
            raise ValueError(f"File {self.fileName} does not exist")
    
    def save(self):
        """
        Save the database

        Returns:
            None
        """
        try:
            data = {}
            for table in self.tables:
                data[table] = {
                    "columns": self.tables[table].getColumnsRaw(),
                    "data": self.tables[table].getDataRaw()
                }
            with open(self.fileName, "w") as file:
                json.dump(data, file)
        except Exception as e:
            print(e)

    def createTable(self, name, columns):
        """
        Create a table

        Args:
            name (str): name of the table
            columns (list): list of columns, each column is a dictionary with the following keys:
                - name (str): name of the column
                - description (str): description of the column
                - required (bool): if the column is required
                - autoIncrement (bool): if the column is auto increment
                - unique (bool): if the column is unique

        Returns:
            None
        """
        if name in self.tables:
            raise ValueError(f"Table {name} already exists")
        self.tables[name] = Table(name, columns)
    
    def getTable(self, name):
        """
        Get a table

        Args:
            name (str): name of the table
        
        Returns:
            Table: table
        """
        if name not in self.tables:
            raise ValueError(f"Table {name} does not exist")
        return self.tables[name]
    
    def deleteTable(self, name):
        """
        Delete a table

        Args:
            name (str): name of the table

        Returns:
            None
        """
        if name not in self.tables:
            raise ValueError(f"Table {name} does not exist")
        del self.tables[name]

    def query(self, table, query):
        """
        Query the database

        Args:
            table (str): name of the table
            query (dict): query to execute

        Returns:
            list: data of the table
        """
        return self.tables[table].queryData(query)

    def addColumn(self, table, name, description):
        """
        Add a column to the database

        Args:
            table (str): name of the table
            name (str): name of the column
            description (str): description of the column

        Returns:
            None
        """
        self.tables[table].addColumn(name, description)

    def modifyData(self, table, oldData, newData):
        """
        Modify the data of the database

        Args:
            table (str): name of the table
            oldData (dict): old data
            newData (dict): new data

        Returns:
            bool: True if the data has been modified, False otherwise
        """
        return self.tables[table].modifyData(oldData, newData)
    
    def deleteData(self, table, data):
        """
        Delete the data of the database

        Args:
            table (str): name of the table
            data (dict): data to delete

        Returns:
            bool: True if the data has been deleted, False otherwise
        """
        return self.tables[table].deleteData(data)

    def addData(self, table, data):
        """
        Add data to the database

        Args:
            table (str): name of the table
            data (dict): data to add to the database

        Returns:
            None
        """
        self.tables[table].addData(data)

    def getTables(self):
        """
        Get the tables of the database

        Returns:
            list: tables of the database
        """
        return list(self.tables.keys())

    def getTableColumns(self, table):
        """
        Get the columns of a table

        Args:
            table (str): name of the table

        Returns:
            list: columns of the table
        """
        return self.tables[table].getColumns()


class QueryCollections(InterfaceDefinition):
    """
    Class that represent the query collections program

    Static Attributes:
        languages (dict): dictionary that contains all the languages supported by the program

    Methods:
        printTable: print a table
        textInterface: show the interface
    """

    languages = {
        "ita": {
            "selectDatabasePath": "Inserisci il percorso delle collezioni: ",
            "viewTableChoice": "1. Visualizza tabelle",
            "createTableChoice": "2. Crea tabella",
            "executeQueryChoice": "3. Esegui query",
            "returnChoice": "4. Torna al menu precedente",
            "exitChoice": "5. Esci",
            "choice": "Scelta: ",
            "tableName": "Nome tabella: ",
            "column": "Colonna: ",
            "columnDescription": "Descrizione: ",
            "columnRequired": "Richiesta (y/n): ",
            "columnAutoIncrement": "Auto increment (y/n): ",
            "columnUnique": "Unica (y/n): ",
            "queryTypeChoiceSearch": "1. Ricerca",
            "queryTypeChoiceAdd": "2. Aggiungi",
            "queryTypeChoiceModify": "3. Modifica",
            "queryTypeChoiceDelete": "4. Elimina",
            "queryType": "Tipo di query: ",
            "select": "Select: ",
            "from": "From: ",
            "where": "Where: ",
            "wrongQuery": "Query errata",
            "table": "Tabella: ",
            "oldData": "Vecchi dati ",
            "newData": "Nuovi dati ",
            "deleteData": "Dati da eliminare ",
            "addData": "Dati da aggiungere ",
            "wrongData": "Dati errati",
            "choiceNotValid": "Scelta non valida",
            "fileNotFound": "File non trovato",
            "goodbye": "Arrivederci",
            "pressEnter": "\nPremi invio per continuare...",
            "selectFolderPath": "Inserisci il percorso della cartella: ",
            "selectDatabaseName": "Inserisci il nome del database: ",
            "choiceSelectDatabase": "1. Seleziona database",
            "choiceCreateDatabase": "2. Crea database",
            "choiceExit": "3. Esci",
            "noData": "Nessun dato da mostrare",
            "dataAdded": "Dati aggiunti",
            "dataModified": "Dati modificati",
            "dataDeleted": "Dati eliminati"
        },
        "eng": {
            "selectDatabasePath": "Insert the path of the collections: ",
            "viewTableChoice": "1. View tables",
            "createTableChoice": "2. Create table",
            "executeQueryChoice": "3. Execute query",
            "returnChoice": "4. Torna al menu precedente",
            "exitChoice": "5. Exit",
            "choice": "Choice: ",
            "tableName": "Table name: ",
            "column": "Column: ",
            "columnDescription": "Description: ",
            "columnRequired": "Required (y/n): ",
            "columnAutoIncrement": "Auto increment (y/n): ",
            "columnUnique": "Unique (y/n): ",
            "queryTypeChoiceSearch": "1. Search",
            "queryTypeChoiceAdd": "2. Add",
            "queryTypeChoiceModify": "3. Modify",
            "queryTypeChoiceDelete": "4. Delete",
            "queryType": "Query type: ",
            "select": "Select: ",
            "from": "From: ",
            "where": "Where: ",
            "wrongQuery": "Wrong query",
            "table": "Table: ",
            "oldData": "Old data ",
            "newData": "New data ",
            "deleteData": "Data to delete ",
            "addData": "Data to add ",
            "wrongData": "Wrong data",
            "choiceNotValid": "Choice not valid",
            "fileNotFound": "File not found",
            "goodbye": "Goodbye",
            "pressEnter": "\nPress enter to continue...",
            "selectFolderPath": "Insert the path of the folder: ",
            "selectDatabaseName": "Insert the name of the database: ",
            "choiceSelectDatabase": "1. Select database",
            "choiceCreateDatabase": "2. Create database",
            "choiceExit": "3. Exit",
            "noData": "No data to show",
            "dataAdded": "Data added",
            "dataModified": "Data modified",
            "dataDeleted": "Data deleted"
        }
    }

    def __init__(self):
        """
        Initialize the query collections program

        Returns:
            None
        """
        super().__init__(["Query Collections"], "0.1", "dp")
    
    def printTable(self, data, lang="eng"):
        """
        Print a table of data

        Args:
            data (list): data to print
            lang (str): language

        Returns:
            None
        """
        if len(data) == 0:
            print(self.languages[lang]["noData"])
            return
        columns = list(data[0].keys())
        for row in data:
            for column in row.keys():
                if column not in columns:
                    columns.append(column)
        columnsLength = {column: len(column) for column in columns}
        for row in data:
            for column in row.keys():
                if len(str(row[column])) > columnsLength[column]:
                    columnsLength[column] = len(str(row[column]))
        for column in columns:
            print("| " + column.ljust(columnsLength[column] + 1), end="")
        print("|")
        for column in columns:
            print("|", end="")
            print(" " + "-" * (columnsLength[column]) + " ", end="")
        print("|")
        for row in data:
            print("| ", end="")
            for column in columns:
                print((str(row[column]).ljust(columnsLength[column] + 1) if column in row.keys() else (" " * (columnsLength[column] + 2))) + "| ", end="")
            print()
    
    def textInterface(self, lang="eng"):
        """
        Show the interface

        Args:
            lang (str): language

        Returns:
            None
        """
        while True:
            super().drowPrologue()
            alreadyPressed = False
            print(self.languages[lang]["choiceSelectDatabase"])
            print(self.languages[lang]["choiceCreateDatabase"])
            print(self.languages[lang]["choiceExit"])
            choice = input(self.languages[lang]["choice"])
            if choice == "1":
                pathToDB = input(self.languages[lang]["selectDatabasePath"])
                try:
                    db = CollectionDatabase(pathToDB)
                    continueLoop = True
                    while continueLoop:
                        super().drowPrologue()
                        print(self.languages[lang]["viewTableChoice"])
                        print(self.languages[lang]["createTableChoice"])
                        print(self.languages[lang]["executeQueryChoice"])
                        print(self.languages[lang]["returnChoice"])
                        print(self.languages[lang]["exitChoice"])
                        choice = input(self.languages[lang]["choice"])
                        if choice == "1":
                            for table in db.getTables():
                                print(table)
                        elif choice == "2":
                            name = input(self.languages[lang]["tableName"])
                            columns = []
                            continueInnerLoop = True
                            while continueInnerLoop:
                                column = input(self.languages[lang]["column"])
                                if column == "":
                                    continueInnerLoop = False
                                else:
                                    description = input(self.languages[lang]["columnDescription"])
                                    isRequired = True if input(self.languages[lang]["columnRequired"]) == "y" else False
                                    isAutoIncrement = True if input(self.languages[lang]["columnAutoIncrement"]) == "y" else False
                                    isUnique = True if input(self.languages[lang]["columnUnique"]) == "y" else False
                                    columns.append({"name": column, "description": description, "required": isRequired, "autoIncrement": isAutoIncrement, "unique": isUnique})
                            db.createTable(name, columns)
                            db.save()
                        elif choice == "3":
                            super().drowPrologue()
                            print(self.languages[lang]["queryTypeChoiceSearch"])
                            print(self.languages[lang]["queryTypeChoiceAdd"])
                            print(self.languages[lang]["queryTypeChoiceModify"])
                            print(self.languages[lang]["queryTypeChoiceDelete"])
                            queryType = input(self.languages[lang]["queryType"])
                            if(queryType == "1"):
                                try:
                                    selectPart = input(self.languages[lang]["select"])
                                    fromPart = input(self.languages[lang]["from"])
                                    wherePart = input(self.languages[lang]["where"])
                                    query = {
                                        "SELECT": [columnName.strip() for columnName in selectPart.split(",")],
                                        "FROM": fromPart,
                                        "WHERE": {columnName.strip().split("=")[0].strip(): columnName.strip().split("=")[1].strip() for columnName in wherePart.split("AND")} if wherePart != "" else {}
                                    }
                                    self.printTable(db.query(query["FROM"], query), lang)
                                except:
                                    print(self.languages[lang]["wrongQuery"])
                            elif(queryType == "2"):
                                try:
                                    table = input(self.languages[lang]["table"])
                                    data = {}
                                    for column in db.getTableColumns(table):
                                        data[column] = input(self.languages[lang]["addData"] + column + ": ")
                                        if data[column] == "":
                                            del data[column]
                                    db.addData(table, data)
                                    print(self.languages[lang]["dataAdded"])
                                except:
                                    print(self.languages[lang]["wrongData"])
                            elif(queryType == "3"):
                                try:
                                    table = input(self.languages[lang]["table"])
                                    oldData = {}
                                    newData = {}
                                    for column in db.getTableColumns(table):
                                        oldData[column] = input(self.languages[lang]["oldData"] + column + ": ")
                                        if oldData[column] == "":
                                            del oldData[column]
                                        newData[column] = input(self.languages[lang]["newData"] + column + ": ")
                                        if newData[column] == "":
                                            del newData[column]
                                    db.modifyData(table, oldData, newData)
                                    print(self.languages[lang]["dataModified"])
                                except:
                                    print(self.languages[lang]["wrongData"])
                            elif(queryType == "4"):
                                try:
                                    table = input(self.languages[lang]["table"])
                                    data = {}
                                    for column in db.getTableColumns(table):
                                        data[column] = input(self.languages[lang]["deleteData"] + column + ": ")
                                        if data[column] == "":
                                            del data[column]
                                    db.deleteData(table, data)
                                    print(self.languages[lang]["dataDeleted"])
                                except:
                                    print(self.languages[lang]["wrongData"])
                            else:
                                print(self.languages[lang]["choiceNotValid"])
                            db.save()
                        elif choice == "4":
                            continueLoop = False
                            alreadyPressed = True
                        elif choice == "5":
                            print(self.languages[lang]["goodbye"])
                            return
                        else:
                            print(self.languages[lang]["choiceNotValid"])
                        input(self.languages[lang]["pressEnter"])
                except:
                    print(self.languages[lang]["fileNotFound"])
            elif choice == "2":
                try:
                    db = CollectionDatabase()
                    path = input(self.languages[lang]["selectFolderPath"])
                    name = input(self.languages[lang]["selectDatabaseName"])
                    db.createDatabase(path, name)
                except:
                    print(self.languages[lang]["fileNotFound"])
            elif choice == "3":
                print(self.languages[lang]["goodbye"])
                return
            if not alreadyPressed:
                input(self.languages[lang]["pressEnter"])

def construct():
    """
    Construct a query collections program

    Returns:
        QueryCollections: a query collections program
    """
    return QueryCollections()

if __name__ == "__main__":
    QueryCollections().textInterface()