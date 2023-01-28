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

    def getStats(self, *columns):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM stats")
        

        if cursor._check_executed() == False:
            return
        
        x = cursor.fetchall()
        newList = list(x)

        for i in x:
            newList.append(i)

        
        return newList

    def getColumns(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM stats")
        columnNames = cursor.column_names
        return columnNames