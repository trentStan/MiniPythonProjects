from tkinter import *
from customModules.MySQLModule import *
from customModules.stringModifier import capitalise

class Table:
     
    def __init__(self,root):
        
        # code for creating table
        for i in range(total_rows):
        
            for j in range(total_columns):
                if i == 0:
                        
                        
                        self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'), borderwidth=3)
                        self.e.grid(row=i, column=j)
                        
                        self.e.insert(END, capitalise(columns[j]))  
                else:
                        self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16))
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, data[i][j])       
 # type: ignore                    
                

mydb=DB()
data = mydb.getStats("*")
x = len(data)
 # type: ignore
columns = mydb.getColumns()



total_rows = x
total_columns = len(columns) 

root = Tk()
t = Table(root)
root.title("List of Stats")
root.resizable(False, False)
root.mainloop()




