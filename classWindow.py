from tkinter import *
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.master = master
        self.master.title("Simulation Project")
        self.pack(fill=BOTH, expand=1) 
        
root = Tk()

app = Window(root)

root.mainloop()