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
    C1.pack()
    C2.pack()
    C3.pack()

    #label
    timeLabel = StringVar()
    timeQuanta = Label(processSchedualerPage, textvariable=timeLabel, relief=FLAT )

    timeLabel.set("Time Quanta")
    timeQuanta.pack()

    #user Entry for time quanta
    userTimeQuanta = Entry(processSchedualerPage, bd =5)
    userTimeQuanta.pack()

    #process display field
    processes = Text(processSchedualerPage)
    processes.insert(INSERT, "Hello.....")
    processes.insert(END, "Bye Bye.....")
    processes.pack()
    

    # start button
    processBtn = ui.Button(processSchedualerPage, text ="Start", command = helloCallBack)
    processBtn.pack()


    # second page
    memoryManagementPage = ttk.Frame(notebook)

    # third page
    pagingPage = ttk.Frame(notebook)

    notebook.add(processSchedualerPage, text='Process Schedualer')
    notebook.add(memoryManagementPage, text='Memory Management')
    notebook.add(pagingPage, text='Page Replacement')
    
    notebook.pack(expand=1, fill="both")

    root.mainloop()

def helloCallBack():
    print("I work")

if __name__ == "__main__":
    demo()
