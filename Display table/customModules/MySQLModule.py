import mysql.connector
class DB:
    
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="covid"
        )
        
        print(self.mydb)
    
    def queryDB(self, statement) :
        cursor = self.mydb.cursor(named_tuple=True)
    
        cursor.execute(statement)
        

        if cursor._check_executed() == False:
            return

        x = cursor.fetchall()
        return x

    def getStats(self, columns):
        cursor = self.mydb.cursor()
        selectedColumns = ""
        index = 0
        for columnname in columns:
            if index == 0: 
                selectedColumns = selectedColumns + columnname
                index = index + 1
            else:
                selectedColumns = selectedColumns + ", " +columnname
        
        print(selectedColumns)
        cursor.execute("SELECT "+ selectedColumns +" FROM stats")
        
        
        if cursor._check_executed() == False:
            return
        
        x = cursor.fetchall()
        newList = list(x)

        for i in x:
            newList.append(i)

        print(newList)
        return newList

    def getColumns(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM stats")
        columnNames = cursor.column_names
        return columnNames