import tkinter as tk

class BasicGUI:

    def changeLabel(self):
        self.label.config(text=self.textbox.get("1.0","end-1c"))

    def resetLabel(self):
        self.label.config(text="The 'Change Label' button can change this label")

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x300")
        self.root.resizable(width=False, height=False)
        self.root.title("Basic GUI")
        

        self.label = tk.Label(self.root, text="The 'Change Label' button can change this label", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root, font=('Arial', 16), height=3)
        self.textbox.pack()

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        
        self.btnLabelChange = tk.Button(self.buttonFrame, text="Change label", command=self.changeLabel) 
        self.btnLabelChange.grid(row=0, column=0, sticky=tk.W+tk.E)
        
        self.btnResetLabel = tk.Button(self.buttonFrame, text="Reset Label", command=self.resetLabel) 
        self.btnResetLabel.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.buttonFrame.pack()

        self.root.mainloop(n=1)


BasicGUI()