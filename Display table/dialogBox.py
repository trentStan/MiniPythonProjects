import tkinter as tk
from customModules.MySQLModule import *
from MySQLTable import loadTable

class BasicGUI:

    def LoadTable(self):
        index = 0
        selectedColumns = []
        for checkState in self.checkStates:
            if checkState.get():
                selectedColumns.append(self.columns[index])

            index = index + 1
       
        loadTable(selectedColumns)

    def __init__(self):
        mydb=DB()
        self.columns = mydb.getColumns()

        self.root = tk.Tk()

        self.root.geometry("550x300")
        self.root.resizable(width=False, height=False)
        self.root.title("Basic GUI")
        

        self.label = tk.Label(self.root, text="Check the boxes of  columns you wish to see", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)
        self.checkFrame = tk.Frame(self.root)

        for number in range(len(self.columns)):
            self.checkFrame.columnconfigure(number, weight=1)
        self.checkBoxes = []
        self.checkStates =[]
        index = 0
        for column in self.columns:
            index = index + 1
            checkState = tk.IntVar(name=column)
            checkbox = tk.Checkbutton(self.checkFrame, variable=checkState ,text=column, font=("Arial", 13))
            
            self.checkStates.append(checkState)
            checkbox.grid(row=0, column=(index-1), sticky=tk.W+tk.E)
            self.checkBoxes.append(checkbox)
        self.checkFrame.pack()

        self.btnSubmit = tk.Button(self.root, text="Submit", command=self.LoadTable, font=("Arial", 13)) 
        self.btnSubmit.pack()
                
        self.root.mainloop()


if __name__ == "__main__":
    BasicGUI()