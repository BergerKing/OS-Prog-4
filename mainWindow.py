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

    #time quanta label
    timeLabel = StringVar()
    timeQuanta = Label(processSchedualerPage, textvariable=timeLabel, relief=FLAT )

    timeLabel.set("Time Quanta")
    timeQuanta.pack()

    #user Entry for time quanta
    userTimeQuanta = Entry(processSchedualerPage, bd =5)
    userTimeQuanta.pack()

    #process display field
    processes = Text(processSchedualerPage)
    processes.insert(INSERT, "Process          Burst Time          Arrival          Priority\n")
    processes.pack()

    #Gantt Chart Label
    ganttString = StringVar()
    ganttLabel = Label(processSchedualerPage, textvariable=timeLabel, relief=FLAT )

    ganttString.set("Gantt Chart")
    ganttLabel.pack()

    #Gantt Chart
    

    # start button
    processBtn = ui.Button(processSchedualerPage, text ="Start", command = helloCallBack)
    processBtn.pack()


    # second page
    memoryManagementPage = ttk.Frame(notebook)

    # third page
    pagingPage = ttk.Frame(notebook)

    #checkboxes
    FIFOVar = IntVar()
    optimalVar = IntVar()
    LRUVar = IntVar()
    LFUVar = IntVar()
    NRUVar = IntVar()
    
    FIFOCheckbox = Checkbutton(pagingPage, text = "FIFO", variable = FIFOVar, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    optimalCheckbox = Checkbutton(pagingPage, text = "Optimal", variable = optimalVar, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    LRUCheckbox = Checkbutton(pagingPage, text = "LRU", variable = LRUVar, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    LFUCheckbox = Checkbutton(pagingPage, text = "LFU", variable = LFUVar, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    NRUCheckbox = Checkbutton(pagingPage, text = "NRU", variable = NRUVar, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
    FIFOCheckbox.pack()
    optimalCheckbox.pack()
    LRUCheckbox.pack()
    LFUCheckbox.pack()
    NRUCheckbox.pack()

    # frames label
    frameString = StringVar()
    frameLabel = Label(pagingPage, textvariable=frameString, relief=FLAT )

    frameString.set("Number of Frames")
    frameLabel.pack()

    #user Entry for frame number
    frameNumber = Entry(pagingPage, bd =5)
    frameNumber.pack()

    # reference string label
    referenceString = StringVar()
    referenceLabel = Label(pagingPage, textvariable=referenceString, relief=FLAT )

    referenceString.set("Reference String")
    referenceLabel.pack()

    #user Entry for frame number
    referenceEntry = Entry(pagingPage, bd =5)
    referenceEntry.pack()
    
    

    notebook.add(processSchedualerPage, text='Process Schedualer')
    notebook.add(memoryManagementPage, text='Memory Management')
    notebook.add(pagingPage, text='Page Replacement')
    
    notebook.pack(expand=1, fill="both")

    root.mainloop()

def helloCallBack():
    print("I work")

if __name__ == "__main__":
    demo()
