import sys
from tkinter import ttk
from tkinter import *
import tkinter as ui


def demo():
    root = ui.Tk()
    root.title("OS Program 4")
    root.minsize(width=500, height=500)

    notebook = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook 
    # first page, which would get widgets gridded into it
    processSchedualerPage = ttk.Frame(notebook)

    # Checkboxes for Process sch.
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    C1 = Checkbutton(processSchedualerPage, text = "RR", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    C2 = Checkbutton(processSchedualerPage, text = "Priority", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    C3 = Checkbutton(processSchedualerPage, text = "SJF", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    C1.grid(row=0, column=0)
    C2.grid(row=0, column=1)
    C3.grid(row=0, column=2)

    #label
    timeLabel = StringVar()
    timeQuanta = Label(processSchedualerPage, textvariable=timeLabel, relief=FLAT )

    timeLabel.set("Time Quanta")
    timeQuanta.grid(row=1, column=1)

    #user Entry for time quanta
    userTimeQuanta = Entry(processSchedualerPage, bd =5)
    userTimeQuanta.grid(row=2, column=1)

    #process display field
    processes = Text(processSchedualerPage)
    processes.insert(INSERT, "Hello.....")
    processes.insert(END, "Bye Bye.....")
    processes.grid(row=3, column=1)
    

    # start button
    processBtn = ui.Button(processSchedualerPage, text ="Start", command = helloCallBack)
    processBtn.grid(row=4, column=1)


    # second page
    memoryManagementPage = ttk.Frame(notebook)

    # third page
    pagingPage = ttk.Frame(notebook)

    notebook.add(processSchedualerPage, text='Process Schedualer')
    notebook.add(memoryManagementPage, text='Memory Management')
    notebook.add(pagingPage, text='Page Replacement')
    
    notebook.grid(row=5, column=1)

    root.mainloop()

def helloCallBack():
    print("I work")

if __name__ == "__main__":
    demo()
