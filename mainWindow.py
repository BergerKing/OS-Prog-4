import sys
from tkinter import ttk
import tkinter as ui


def demo():
    root = ui.Tk()
    root.title("ttk.Notebook")

    notebook = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook 
    # first page, which would get widgets gridded into it
    processSchedualerPage = ttk.Frame(notebook)

    # second page
    memoryManagementPage = ttk.Frame(notebook)

    # third page
    pagingPage = ttk.Frame(notebook)

    notebook.add(processSchedualerPage, text='Process Schedualer')
    notebook.add(memoryManagementPage, text='Memory Management')
    notebook.add(pagingPage, text='Page Replacement')
    
    nb.pack(expand=1, fill="both")

    root.mainloop()

if __name__ == "__main__":
    demo()
