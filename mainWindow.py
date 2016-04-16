import sys
from tkinter import ttk
import tkinter as ui


def demo():
    root = ui.Tk()
    root.title("ttk.Notebook")

    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook 
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb)

    # second page
    page2 = ttk.Frame(nb)

    # third page
    page3 = ttk.Frame(nb)

    nb.add(page1, text='One')
    nb.add(page2, text='Two')
    nb.add(page3, text='Three')
    
    nb.pack(expand=1, fill="both")

    root.mainloop()

if __name__ == "__main__":
    demo()
