import sys
from random import randint
from operator import itemgetter
from tkinter import ttk
from tkinter import *
import tkinter as ui

class OsDemo():
    def __init__(self):
        self.demo()

    def demo(self):
        self.root = ui.Tk()
        self.root.title("OS Program 4")
        self.root.minsize(width=500, height=500)

        self.notebook = ttk.Notebook(self.root)

        # adding Frames as pages for the ttk.Notebook 
        # first page, which would get widgets gridded into it
        self.processSchedualerPage = ttk.Frame(self.notebook)

        # Checkboxes for Process sch.
        self.CheckVar = StringVar()

        self.C1 = Radiobutton(self.processSchedualerPage, text = "RR", variable = self.CheckVar, value= "RR")
        self.C2 = Radiobutton(self.processSchedualerPage, text = "Priority", variable = self.CheckVar, value= "Priority")
        self.C3 = Radiobutton(self.processSchedualerPage, text = "SJF", variable = self.CheckVar, value= "SJF")
        self.C1.grid(row=0, column=0)
        self.C2.grid(row=0, column=1)
        self.C3.grid(row=0, column=2)

        #time quanta label
        self.timeLabel = StringVar()
        self.timeQuanta = Label(self.processSchedualerPage, textvariable=self.timeLabel, relief=FLAT )

        self.timeLabel.set("Time Quanta")
        self.timeQuanta.grid(row=1, column=1)

        #user Entry for time quanta
        self.userTimeQuanta = Entry(self.processSchedualerPage, bd =5)
        self.userTimeQuanta.grid(row=2, column=1)

        #process display field
        self.processChart = Text(self.processSchedualerPage)
        self.processChart.insert(INSERT, "Process          Burst Time          Arrival          Priority\n")
        self.processChart.grid(row=3, column=1)
        

        # start button
        self.processBtn = ui.Button(self.processSchedualerPage, text ="Start", command = self.processCallBack)
        self.processBtn.grid(row=6, column=1)











        # second page
        self.memoryManagementPage = ttk.Frame(self.notebook)

        # third page
        self.pagingPage = ttk.Frame(self.notebook)

        #checkboxes
        self.pageVar = StringVar()
        
        self.FIFORadio = Radiobutton(self.pagingPage, text = "FIFO", variable = self.pageVar, value = "FIFO")
        self.optimalRadio = Radiobutton(self.pagingPage, text = "Optimal", variable = self.pageVar, value = "Optimal")
        self.LRURadio = Radiobutton(self.pagingPage, text = "LRU", variable = self.pageVar, value = "LRU")
        self.LFURadio = Radiobutton(self.pagingPage, text = "LFU", variable = self.pageVar, value = "LFU")
        self.NRURadio = Radiobutton(self.pagingPage, text = "NRU", variable = self.pageVar, value = "NRU")
        
        self.FIFORadio.grid(row=0, column=0)
        self.optimalRadio.grid(row=0, column=1)
        self.LRURadio.grid(row=0, column=2)
        self.LFURadio.grid(row=0, column=3)
        self.NRURadio.grid(row=0, column=4)

        # frames label
        self.frameString = StringVar()
        self.frameLabel = Label(self.pagingPage, textvariable=self.frameString, relief=FLAT )

        self.frameString.set("Number of Frames:")
        self.frameLabel.grid(row=1, column=1)

        #user Entry for frame number
        self.frameNumber = Entry(self.pagingPage, bd =5)
        self.frameNumber.grid(row=1, column=2)

        # reference string label
        self.referenceString = StringVar()
        self.referenceLabel = Label(self.pagingPage, textvariable=self.referenceString, relief=FLAT )

        self.referenceString.set("Reference String")
        self.referenceLabel.grid(row=2, column=1)

        #for reference string
        self.referenceEntry = Entry(self.pagingPage, bd =5)
        self.referenceEntry.grid(row=2, column=2)

        # blank space Labels
        emptyLabelForSpacing1 = Label(self.pagingPage, relief=FLAT)
        emptyLabelForSpacing1.grid(row=3, column=0)
        emptyLabelForSpacing2 = Label(self.pagingPage, relief=FLAT)
        emptyLabelForSpacing2.grid(row=4, column=0)
        emptyLabelForSpacing3 = Label(self.pagingPage, relief=FLAT)
        emptyLabelForSpacing3.grid(row=5, column=0)
        
        
        
        # frame stack Label
        self.frameStackString = StringVar()
        self.frameStackLabel = Label(self.pagingPage, textvariable=self.frameStackString, relief=FLAT )

        self.frameStackString.set("Frame Stack")
        self.frameStackLabel.grid(row=9, column=1)

        # frames
        frameRow = 10
        self.frameEntry = []
        self.frameString = []
        for num in range(3):
            self.frameString.append(StringVar())
            self.frameEntry.append(Entry(self.pagingPage, textvariable = self.frameString[num], bd=5 ) )
            self.frameEntry[num].grid(row=frameRow, column=2)
            self.setFrames()
            frameRow = frameRow + 1
            

        # page faults label
        self.faultString = StringVar()
        self.faultLabel = Label(self.pagingPage, textvariable=self.faultString, relief=FLAT )

        self.faultString.set("Page Fault")
        frameRow = frameRow + 1
        self.faultLabel.grid(row=frameRow, column=1)

        #Entry for frame number
        self.faultEntry = Entry(self.pagingPage, bd =5)
        frameRow = frameRow + 1
        self.faultEntry.grid(row=frameRow, column=2)

        #page start button
        self.pageBtn = ui.Button(self.pagingPage, text ="Start", command = self.pageCallBack)
        frameRow = frameRow + 1
        self.pageBtn.grid(row=frameRow, column=2)

        self.pushBtn = ui.Button(self.pagingPage, text ="Push", command = self.Optimal)
        self.pushBtn.grid(row=frameRow, column=3)
        
        

        self.notebook.add(self.processSchedualerPage, text='Process Schedualer')
        self.notebook.add(self.memoryManagementPage, text='Memory Management')
        self.notebook.add(self.pagingPage, text='Page Replacement')
        
        self.notebook.grid(row=5, column=1)

        self.root.mainloop()

    def processCallBack(self):
        
        self.process = self.generateProcesses()
        self.writeOutProcess()

        if(self.CheckVar.get() == "RR"):
            self.roundRobin()
        if(self.CheckVar.get() == "Priority"):
            self.priority()
        if(self.CheckVar.get() == "SJF"):
            self.SJF()


    def generateProcesses(self):
        processes = []

        for i in range(4):
           current = []
           current.append("P" + str(i))
           current.append(randint(1, 9))
           current.append(randint(1,9))
           current.append(randint(1,5))

           processes.append(current)

        return processes

    def writeOutProcess(self):
        self.processChart.delete('1.0', END)
        self.processChart.insert(INSERT, "Process          Burst Time          Arrival          Priority\n")
        for i in range(4):
            self.processChart.insert(INSERT, str(self.process[i][0]) + "                        " + str(self.process[i][1]) + "               " \
                                 + str(self.process[i][2]) + "              "  + str(self.process[i][3]) + "\n")
    def roundRobin(self):
        time = int(self.userTimeQuanta.get())
        
        processSort = self.process
        processSort = sorted(processSort, key=itemgetter(2))
        timeTaken = processSort[0][2]
        gantt = []
        ganttTimeUsed = [0]
        timeCount = 0
        while ( processSort[0][1] > 0 or processSort[1][1] > 0 or processSort[2][1] > 0 or processSort[3][1] > 0 ):
            for t in range(4):
                if (processSort[t][2] <= timeTaken and processSort[t][1] > 0):
                    gantt.append(processSort[t][0])
                    timeCount += time
                    ganttTimeUsed.append(timeCount)
                    processSort[t][1] -= time
                timeTaken += time
                
                    
                

        self.generateGantt(gantt, ganttTimeUsed)

    def SJF(self):
        processSort = self.process
        processSort = sorted(processSort, key=itemgetter(2))
        processSort = sorted(processSort, key=itemgetter(1))
        gantt = []
        for t in range(4):
            gantt.append(processSort[t][0])
            
        ganttTimeUsed = [0]
        for t in range(4):
            ganttTimeUsed.append((ganttTimeUsed[t] + processSort[t][1]))

        self.generateGantt(gantt, ganttTimeUsed)

    def priority(self):
        print("here")
        processSort = self.process
        processSort = sorted(processSort, key=itemgetter(2))
        processSort = sorted(processSort, key=itemgetter(3))
        gantt = []
        ganttTimeUsed = [0]
        for t in range(4):
            gantt.append(processSort[t][0])
            ganttTimeUsed.append((ganttTimeUsed[t] + processSort[t][1]))

        self.generateGantt(gantt, ganttTimeUsed)


            
    def generateGantt(self, gantt, ganttTimeUsed):
        self.processChart.insert(INSERT, "\n \n \n")
        self.processChart.insert(INSERT, "Gantt Chart: \n")
        processOrder = "   "
        processTime = ""
        for proc in gantt:
            processOrder = processOrder + proc.rjust(6)
        for time in ganttTimeUsed:
            if (time == 0):
                processTime = str(time).rjust(6)
            elif (time > 9):
                 processTime = processTime + str(time).rjust(6)
            else:
                processTime = processTime + str(time).rjust(6)
            
        self.processChart.insert(INSERT, processOrder + "\n")
        self.processChart.insert(INSERT, processTime + "\n")


    #THRID PAGE OF FUNCTIONS
    def pageCallBack(self):
        self.generateRefString()

    def generateRefString(self):
        self.refList = []
        self.refString = ""
        for index in range(11):
            self.refList.append(randint(0, 9))
        for index in self.refList:
            self.refString = self.refString + " " + str(index)

        self.referenceEntry.delete(0, END)
        self.referenceEntry.insert(0, self.refString)
        self.referenceEntry.configure(state='readonly')

    def setFrames(self):
        for index in self.frameEntry:
            index.delete(0, END)
            index.insert(0, "N/A")

    def FIFO(self):
        faultCount = 0
        for index in self.refList:
            flag = False
            for val in self.frameEntry:
                if (str(index) == val.get()):
                    flag = True
                    
            if (flag == False):
                faultCount += 1
                for val in range(3):
                        
                    if (val != 0):
                        frame = self.frameEntry[val].get()
                        self.frameEntry[val].delete(0, END)
                        self.frameEntry[val].insert(0, curr)
                        curr = frame
                    else:
                        curr = self.frameEntry[0].get()
                        self.frameEntry[0].delete(0, END)
                        self.frameEntry[0].insert(0, index)

        
        self.faultEntry.delete(0, END)
        self.faultEntry.insert(0, faultCount)    
        return

    def Optimal(self):
        checkList = self.refList
        faultCount = 0
        for index in range(len(self.refList)):
            
            flag = False
            for val in self.frameEntry:
                if (str(self.refList[index]) == val.get()):
                    flag = True
                    break
                elif (val.get() == "N/A"):
                    val.delete(0, END)
                    val.insert(0, self.refList[index])
                    faultCount += 1
                    flag = True
                    break

                    
            if (flag == False):
                maxDist = 0
                found = -1
                faultCount += 1
                for val in range(3):

                    found = -1
                    frame = self.frameEntry[val].get()
                    dist = 0
                    curr = index
                    while (curr < len(checkList) ):
                        dist += 1
                        
                        if (str(checkList[curr]) == frame):
                            if(dist >= maxDist):
                                maxDist = dist
                                found = val
                            break
                        else:
                            curr += 1
                            
                    if (found == -1):
                        maxDist = 100
                        found = val
                        break
                        
                if (found != -1):
                    self.frameEntry[found].delete(0, END)
                    self.frameEntry[found].insert(0, self.refList[index])

                    
        self.faultEntry.delete(0, END)
        self.faultEntry.insert(0, faultCount)
        return

    
    def LRU(self):
        
        faultCount = 0
        indexprocessed = []
        for index in self.refList:
            
            flag = False
            for val in self.frameEntry:
                if (str(index) == val.get()):
                    indexprocessed.append(str(index))
                    flag = True
                    break
                elif (val.get() == "N/A"):
                    val.delete(0, END)
                    val.insert(0, index)
                    faultCount += 1
                    flag = True
                    indexprocessed.append(str(index))
                    break
                    
            if (flag == False):
                maxDist = 0
                found = -1
                faultCount += 1
                for val in range(3):
                    
                    frame = self.frameEntry[val].get()
                    dist = 0
                    for process in reversed(indexprocessed):
                        dist += 1
                        if (process == frame):
                            if(dist >= maxDist):
                                maxDist = dist
                                found = val
                                break
                            else:
                                break
                            
                if (found != -1):
                    self.frameEntry[found].delete(0, END)
                    self.frameEntry[found].insert(0, index)
                    indexprocessed.append(str(index))
                
        self.faultEntry.delete(0, END)
        self.faultEntry.insert(0, faultCount)    
        return
    
    def LFU(self):
        refCount = [0,0,0,0,0,0,0,0,0,0]
        faultCount = 0
        leastRefCount = 100
        
        for index in self.refList:
            
            flag = False
            for val in self.frameEntry:
                if (str(index) == val.get()):
                    refCount[int(index)] += 1
                    flag = True
                    break
                elif (val.get() == "N/A"):
                    val.delete(0, END)
                    val.insert(0, index)
                    faultCount += 1
                    refCount[int(index)] += 1
                    flag = True
                    break
                
            if (flag == False):
                found = -1
                faultCount += 1
                refCount[int(index)] += 1
                for val in range(3):
                    
                    frame = self.frameEntry[val].get()
                    if (refCount[int(frame)] < leastRefCount):
                        leastRefCount = refCount[int(frame)]
                        found = val
                            
                if (found != -1):
                    self.frameEntry[found].delete(0, END)
                    self.frameEntry[found].insert(0, index)
                    leastRefCount = 100
                
        self.faultEntry.delete(0, END)
        self.faultEntry.insert(0, faultCount)    

        
        return
    def NRU(self):

        #needs a pair for each frame

        framePairs = []
        
        faultCount = 0
        for index in self.refList:

            flag = False
            for val in self.frameEntry:
                if (str(index) == val.get()):
                    flag = True
                    break
                elif (val.get() == "N/A"):
                    val.delete(0, END)
                    val.insert(0, index)
                    faultCount += 1
                    flag = True
                    break

                    
            if (flag == False):
                found = -1
                faultCount += 1
                for val in range(3):

                    found = -1
                    frame = self.frameEntry[val].get()
                    curr = index

                    #if (0,0) put in (0,0) list

                    #if (0,1) put in (0,1) list

                    #if (1,0) put in (1,0) list

                    #if (1,1) ignore actually don't do this thing
                            
                    if (found == -1):
                        maxDist = 100
                        found = val
                        break

                #delete random from (0,0) list

                #if none deleted
                #delete random from (0,1) list

                #if none deleted
                #delete random from (1,0) list

                #if none deleted
                #delete random from all frames

                    
                if (found != -1):
                    self.frameEntry[found].delete(0, END)
                    self.frameEntry[found].insert(0, self.refList[index])

                    
        self.faultEntry.delete(0, END)
        self.faultEntry.insert(0, faultCount)

        
        return
        
        
            
        
        
        
    

if __name__ == "__main__":
    OsDemo()
