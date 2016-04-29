import sys
from random import randint
from random import randrange
from operator import itemgetter
from tkinter import ttk
from tkinter import *
import tkinter as ui

class OsDemo():
    def __init__(self):

        self.EntryFlag = False
        self.numberOfFrame = 3

        self.numberOfBufferFrames = 0
        self.numberOfMemoryPages  = 0
        self.MemoryFlag = False
        
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










        ###################################################################################
        # second page #####################################################################
        ###################################################################################
        self.memoryManagementPage = ttk.Frame(self.notebook)

        self.missCounter = 0
        self.hitCounter = 0


        # Table Look Up label label
        self.lookUpTimeString = StringVar()
        self.lookUpTime = Label(self.memoryManagementPage, textvariable=self.lookUpTimeString, relief=FLAT )

        self.lookUpTimeString.set("Tab Lookup Time: ")
        self.lookUpTime.grid(row=1, column=1)


        #user Entry for Table look up times
        self.lookUpTimeNumber = Entry(self.memoryManagementPage, bd =5)
        self.lookUpTimeNumber.grid(row=1, column=2)


        # Memery Look Up label label
        self.memoryLookUpTimeString = StringVar()
        self.memoryLookUpTime = Label(self.memoryManagementPage, textvariable=self.memoryLookUpTimeString, relief=FLAT )

        self.memoryLookUpTimeString.set("Memory Lookup Time: ")
        self.memoryLookUpTime.grid(row=1, column=3)


        #user Entry for memory look up times
        self.memoryLookUpTimeNumber = Entry(self.memoryManagementPage, bd =5)
        self.memoryLookUpTimeNumber.grid(row=1, column=4)


        # Number of Pages Label
        self.numberOfPagesString = StringVar()
        self.numberOfPages = Label(self.memoryManagementPage, textvariable=self.numberOfPagesString, relief=FLAT )

        self.numberOfPagesString.set("Number of Pages: ")
        self.numberOfPages.grid(row=2, column=4)


        #user Entry for number of pages
        #this is the number of pages in the page table in memory
        self.numberOfPagesNumber = Entry(self.memoryManagementPage, bd =5)
        self.numberOfPagesNumber.grid(row=2, column=5)


        # Number of Frames Label
        # This is the number of things in RAM
        self.numberOfFramesString = StringVar()
        self.numberOfFrames = Label(self.memoryManagementPage, textvariable=self.numberOfFramesString, relief=FLAT )

        self.numberOfFramesString.set("Number of Frames: ")
        self.numberOfFrames.grid(row=2, column=2)


        #user Entry for number of frames
        self.numberOfFramesNumber = Entry(self.memoryManagementPage, bd =5)
        self.numberOfFramesNumber.grid(row=2, column=3 )

    
        # blank space to push canvas down
        emptyLabelForSpacing1 = Label(self.memoryManagementPage, relief=FLAT)
        emptyLabelForSpacing1.grid(row=3, column=0)
        emptyLabelForSpacing2 = Label(self.memoryManagementPage, relief=FLAT)
        emptyLabelForSpacing2.grid(row=4, column=0)
        emptyLabelForSpacing3 = Label(self.memoryManagementPage, relief=FLAT)
        emptyLabelForSpacing3.grid(row=5, column=0)

        
        #The Canvas #################################################
        self.memoryArcitectureCanvas = Canvas(self.memoryManagementPage, width=600, height=200)
        self.memoryArcitectureCanvas.grid( row=6, column=1, columnspan=5, rowspan=3 )

        #cpu box and start line
        self.cpuBox = self.memoryArcitectureCanvas.create_rectangle( 30, 90, 70, 110, fill="" )
        self.cpuText = self.memoryArcitectureCanvas.create_text( 50, 100, text="CPU" )
        self.cpuToLeftBoxLine = self.memoryArcitectureCanvas.create_line( 70, 100, 90, 100 )

        #left hand side double box
        self.leftBoxLeftHalf = self.memoryArcitectureCanvas.create_rectangle( 90, 90, 130, 110, fill="" )
        self.leftBoxRightHalf = self.memoryArcitectureCanvas.create_rectangle( 130, 90, 170, 110, fill="" )

        #down pointing line to expanding table
        self.leftBoxLineToBuffer = self.memoryArcitectureCanvas.create_line( 110, 110, 200, 200 )
        self.rightBoxLineToBuffer = self.memoryArcitectureCanvas.create_line( 200, 200, 270, 100 )


        #lines that connect double boxes
        self.topLineLeft = self.memoryArcitectureCanvas.create_line( 170, 100, 270, 80 )
        self.topLineRight = self.memoryArcitectureCanvas.create_line( 270, 80, 330, 90 )

        #right hand side double box
        self.rightBoxLeftHalf = self.memoryArcitectureCanvas.create_rectangle( 270, 90, 310, 110, fill="" )
        self.rightBoxRightHalf = self.memoryArcitectureCanvas.create_rectangle( 310, 90, 350, 110, fill="" )

        #farthest right hand line segment to memory pages
        self.memoryArcitectureCanvas.create_line( 350, 100, 400, 200 )

        #left side double box inner values
        self.leftBoxMemoryValue = self.memoryArcitectureCanvas.create_text( 110, 100, text="val" )
        self.leftBoxDiskValue = self.memoryArcitectureCanvas.create_text( 150, 100, text="?" )

        #right side double box inner values
        self.rightBoxMemoryValue = self.memoryArcitectureCanvas.create_text( 290, 100, text="val" )
        self.rightBoxDiskValue = self.memoryArcitectureCanvas.create_text( 330, 100, text="ans" )
        # End of Canvas ##############################################

        largestFrameRow = 9


        #page start button
        self.newMemeryOperationButton = ui.Button(self.memoryManagementPage, text ="Run a Memory Operation", command = self.runMemoryOperation)
        largestFrameRow = largestFrameRow + 1
        self.newMemeryOperationButton.grid(row=largestFrameRow, column=2, columnspan=2)

        #Page Reset Button
        self.resetCountersButton = ui.Button(self.memoryManagementPage, text ="Reset Counters", command = self.resetSpeeds)
        self.resetCountersButton.grid(row=largestFrameRow, column=4, columnspan=2)

        ###################################################################################
        # end of second page ##############################################################
        ###################################################################################










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

        #set frame number button
        #set frame number button
        self.frameBtn = ui.Button(self.pagingPage, text ="Set Frame Number", command = self.setNumberOfFrames)
        self.frameBtn.grid(row=1, column=3)

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
        for num in range(self.numberOfFrame):
            self.frameString.append(StringVar())
            self.frameEntry.append(Entry(self.pagingPage, textvariable = self.frameString[num], bd=5 ) )
            self.frameEntry[num].grid(row=frameRow, column=2)
            self.setFrames()
            frameRow = frameRow + 1
                

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
        #print("here")
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

    ####################################################################
    #Second Page Functions #############################################
    ####################################################################

    def setInRamFrames(self):
        counter = 0
        self.logicalMemoryPositionInFrame = list()
        for index in self.inRamFrameEntry:
            index.delete(0, END)
            if( counter < len(self.logicalMemoryPosition)):
                index.insert(0, \
                    str(self.logicalMemoryPosition[counter]) \
                    + " / " + str(self.actualMemoryPosition[counter]))
                self.logicalMemoryPositionInFrame.append(self.logicalMemoryPosition[counter])
                counter = counter + 1
            else:
                index.insert(0, "N/A")

    def setInMemPages(self):
        counter = 0
        maxRand = 0
        self.logicalMemoryPosition = []
        self.actualMemoryPosition = []
        for index in self.inMemPageEntry:
            index.delete(0, END)
            maxRand = randint(maxRand + 1, maxRand + 6)
            self.logicalMemoryPosition.append(counter)
            self.actualMemoryPosition.append(maxRand)
            index.insert(0, str(counter) + "  /  " + str(maxRand))
            counter = counter + 1

    # Calculate hit miss ration
    def hitMissRatio(self, numberHit, memoryLookUpTime, numberMiss, tableLookupTime):
        if( (numberHit + numberMiss) == 0 ):
            return 0
        return ( (numberHit/(numberHit+numberMiss) * memoryLookUpTime) + (numberMiss/(numberMiss + numberHit) * tableLookupTime) )


    def runMemoryOperation(self):
        self.displayMemoryData()
        self.determineHit() 
        if( self.hit ):
            self.paintHit()
        else:
            self.paintMiss()
        #do things
        
        self.displayMemAccTimeNumber.insert(0, self.hitMissRatio( self.hitCounter,\
            int(self.memoryLookUpTimeNumber.get()), self.missCounter,\
            int(self.lookUpTimeNumber.get()) ) )
        

    def displayMemoryData(self):

        #reset positions for changing table size
        if(self.MemoryFlag == True):
            self.displayMemAccTimeNumber.grid_forget()
            self.effectiveMemoryTime.grid_forget()
            self.emptyLabelForSpacing93.grid_forget()
            """
            self.hitsLabel.grid_forget()
            self.missLabel.grid_forget()
            self.hitsNumber.grid_forget()
            self.missNumber.grid_forget()
            """
            frameRow = 10
            for num in range(self.numberOfBufferFrames):
                self.inRamFrameEntry[num].destroy()
            for num in range(self.numberOfMemoryPages):
                self.inMemPageEntry[num].destroy()


        #############
        # the buffer uses values from the page table, thus pages need to be first!!!!
        #############
        # Pages in memory list
        frameRow2 = 9
        self.inMemPageEntry = []
        self.inMemPageString = []
        self.numberOfMemoryPages = min(int(self.numberOfPagesNumber.get()), 10)
        for num in range(self.numberOfMemoryPages):
            #should populate page ##################################################
            self.inMemPageString.append(StringVar())
            self.inMemPageEntry.append(Entry(self.memoryManagementPage, textvariable = self.inMemPageString[num], bd=5 ) )
            self.inMemPageEntry[num].grid(row=frameRow2, column=4)
            self.setInMemPages()
            frameRow2 = frameRow2 + 1

        
        # frames in ram list
        frameRow = 9
        self.inRamFrameEntry = []
        self.inRamframeString = []
        self.numberOfBufferFrames = min(int(self.numberOfFramesNumber.get()), 10)
        for num in range(self.numberOfBufferFrames):
            #should populate at least some Frames ###########################################
            self.inRamframeString.append(StringVar())
            self.inRamFrameEntry.append(Entry(self.memoryManagementPage, textvariable = self.inRamframeString[num], bd=5 ) )
            self.inRamFrameEntry[num].grid(row=frameRow, column=2)
            self.setInRamFrames()
            frameRow = frameRow + 1

        
        largestFrameRow = max(frameRow, frameRow2)

        # blank space to push canvas down
        self.emptyLabelForSpacing93 = Label(self.memoryManagementPage, relief=FLAT)
        self.emptyLabelForSpacing93.grid(row=largestFrameRow, column=0)

        largestFrameRow = largestFrameRow + 1
        
        # effective memory access time due to TLB hits/misses
        self.effectiveMemoryTimeString = StringVar()
        self.effectiveMemoryTime = Label(self.memoryManagementPage, textvariable=self.effectiveMemoryTimeString, relief=FLAT )

        self.effectiveMemoryTimeString.set("Effective memory access time due to TLB hits/misses: ")
        self.effectiveMemoryTime.grid(row=largestFrameRow, column=1, columnspan=2)


        #Dispaly for memory access time due to TLB hits/misses
        self.displayMemAccTimeNumber = Entry(self.memoryManagementPage, bd =5)
        self.displayMemAccTimeNumber.grid(row=largestFrameRow, column=3 )

        
        largestFrameRow = largestFrameRow + 1
        

        """
        # display hit counter
        self.hitsString = StringVar()
        self.hitsLabel = Label(self.memoryManagementPage, textvariable=self.hitsString, relief=FLAT )

        self.hitsString.set("hits: ")
        self.effectiveMemoryTime.grid(row=largestFrameRow, column=3,)


        # display hit value
        self.hitsNumberString = StringVar()
        self.hitsNumber = Label(self.memoryManagementPage, textvariable=self.hitsNumberString, relief=FLAT )
        self.hitsString.set(str(self.hitCounter))
        self.hitsNumber.grid(row=largestFrameRow, column=4 )

        # display miss counter
        self.missString = StringVar()
        self.missLabel = Label(self.memoryManagementPage, textvariable=self.missString, relief=FLAT )

        self.missString.set("misses: ")
        self.effectiveMemoryTime.grid(row=largestFrameRow, column=5,)


        # display miss value
        self.missNumberString = StringVar()
        self.missNumber = Label(self.memoryManagementPage, textvariable=self.hitsNumberString, relief=FLAT )
        self.missString.set(str(self.missCounter))
        self.missNumber.grid(row=largestFrameRow, column=6 )
        """


        

        #page start button
        if( largestFrameRow > 0 ):
            self.newMemeryOperationButton.grid_forget()
            self.resetCountersButton.grid_forget()
            
        self.newMemeryOperationButton = ui.Button(self.memoryManagementPage, text ="Run a Memory Operation", command = self.runMemoryOperation)
        largestFrameRow = largestFrameRow + 1
        self.newMemeryOperationButton.grid(row=largestFrameRow, column=2, columnspan=2)

        self.resetCountersButton = ui.Button(self.memoryManagementPage, text ="Reset Counters", command = self.resetSpeeds)
        self.resetCountersButton.grid(row=largestFrameRow, column=4, columnspan=2)

        self.MemoryFlag = True
        return

    def determineHit(self):
        #loop though frame buffer, if address not there return false
        self.hit = False

        self.newAddress = randint(0, len(self.logicalMemoryPosition)-1)

        self.offsetList = []
        self.offsetString = ""
        self.logicalIndex = str(self.newAddress)
        for index in range(3):
            self.offsetList.append(randint(0, 9))
        for index in self.offsetList:
            self.offsetString = self.offsetString + " " + str(index)

        self.memoryArcitectureCanvas.itemconfig(self.leftBoxMemoryValue, text = (self.logicalIndex + self.offsetString))

        try:
            position = self.logicalMemoryPositionInFrame.index(self.newAddress)
        except ValueError:
            position = -1

        if ( position != -1 ):
            #change color of box at position
            self.memoryArcitectureCanvas.itemconfig(self.inRamFrameEntry[position], fill="green")
            self.actualMemoryString = str(self.actualMemoryPosition[position])
            self.hit = True
        else:
            #change color of page table box
            self.memoryArcitectureCanvas.itemconfig(self.inMemPageEntry[self.logicalMemoryPosition.index(self.newAddress)], fill="red")
            self.actualMemoryString = str(self.actualMemoryPosition[self.logicalMemoryPosition.index(self.newAddress)])
            self.hit = False


        if (self.hit):
            self.hitCounter = self.hitCounter + 1
        else:
            self.missCounter = self.missCounter + 1
        return

    def paintHit(self):
        #use the lables from the objects in the canvas to change item's color
        #hits will be green
        self.memoryArcitectureCanvas.itemconfig(self.cpuBox, fill="green")
        self.memoryArcitectureCanvas.itemconfig(self.cpuText, fill="white")
        self.memoryArcitectureCanvas.tag_raise(self.cpuText)
        self.memoryArcitectureCanvas.itemconfig(self.cpuToLeftBoxLine, fill="blue")
        
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxLeftHalf, fill="green")
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxMemoryValue, fill="white")
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxLineToBuffer, fill="green")
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxLineToBuffer, fill="blue")

        self.memoryArcitectureCanvas.itemconfig(self.rightBoxLineToBuffer, fill="green")

        self.memoryArcitectureCanvas.itemconfig(self.rightBoxMemoryValue, fill="black")
        self.memoryArcitectureCanvas.itemconfig(self.rightBoxLeftHalf, fill="")
        self.memoryArcitectureCanvas.itemconfig(self.rightBoxDiskValue, text="ans", fill="black")

        self.memoryArcitectureCanvas.itemconfig(self.topLineLeft, fill="black")
        self.memoryArcitectureCanvas.itemconfig(self.topLineRight, fill="black")

        #set on disk values
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxDiskValue, text=(self.actualMemoryString + self.offsetString), fill="black")

        self.memoryArcitectureCanvas.itemconfig(self.leftBoxRightHalf, fill="")
        self.memoryArcitectureCanvas.itemconfig(self.rightBoxRightHalf, fill="")
        
        return

    def paintMiss(self):
        #use the labels from the objects in the canvas to change item's color
        #misses will be red
        self.memoryArcitectureCanvas.itemconfig(self.cpuBox, fill="red")
        self.memoryArcitectureCanvas.itemconfig(self.cpuText, fill="white")
        self.memoryArcitectureCanvas.tag_raise(self.cpuText)
        self.memoryArcitectureCanvas.itemconfig(self.cpuToLeftBoxLine, fill="red")
        
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxLeftHalf, fill="red")
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxMemoryValue, text = (str(self.newAddress) + self.offsetString) , fill="white")
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxLineToBuffer, fill="red")
        self.memoryArcitectureCanvas.itemconfig(self.cpuToLeftBoxLine, fill="red")

        self.memoryArcitectureCanvas.itemconfig(self.rightBoxLineToBuffer, fill="red")
        self.memoryArcitectureCanvas.itemconfig(self.rightBoxMemoryValue, text = (str(self.newAddress) + self.offsetString), fill="white")
        self.memoryArcitectureCanvas.itemconfig(self.rightBoxLeftHalf, fill="red")
        self.memoryArcitectureCanvas.itemconfig(self.cpuToLeftBoxLine, fill="red")


        #set on disk values
        self.memoryArcitectureCanvas.itemconfig(self.rightBoxDiskValue, text=(self.actualMemoryString + self.offsetString), fill="white")

        self.memoryArcitectureCanvas.itemconfig(self.topLineLeft, fill="blue")
        self.memoryArcitectureCanvas.itemconfig(self.topLineRight, fill="blue")

        #set on disk values
        self.memoryArcitectureCanvas.itemconfig(self.leftBoxDiskValue, text=(self.actualMemoryString + self.offsetString), fill="white")

        self.memoryArcitectureCanvas.itemconfig(self.leftBoxRightHalf, fill="green")
        self.memoryArcitectureCanvas.itemconfig(self.rightBoxRightHalf, fill="green")
        
        return

    def resetSpeeds(self):
        self.missCounter = 0
        self.hitCounter = 0
        return


    ####################################################################
    #End of second page Functions ######################################
    ####################################################################

    #THRID PAGE OF FUNCTIONS
    def setNumberOfFrames(self):

        if (self.EntryFlag == True):
            self.faultLabel.grid_forget()
            self.faultEntry.grid_forget()
            self.pageBtn.grid_forget()
            self.pushBtn.grid_forget()
            frameRow = 10
            for num in range(self.numberOfFrame):
                self.frameEntry[num].destroy()

        self.numberOfFrame = int(self.frameNumber.get())


        # frames
        frameRow = 10
        self.frameEntry = []
        self.frameString = []
        for num in range(self.numberOfFrame):
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

        #Entry for fault number
        self.faultEntry = Entry(self.pagingPage, bd =5)
        frameRow = frameRow + 1
        self.faultEntry.grid(row=frameRow, column=2)

        #page start button
        self.pageBtn = ui.Button(self.pagingPage, text ="Generate Reference String", command = self.pageCallBack)
        frameRow = frameRow + 1
        self.pageBtn.grid(row=frameRow, column=2)

        self.pushBtn = ui.Button(self.pagingPage, text ="Run Algorithm", command = self.NRU)
        self.pushBtn.grid(row=frameRow, column=3)

        self.EntryFlag = True
        
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
                for val in range(self.numberOfFrame):
                        
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
                for val in range(self.numberOfFrame):

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
                for val in range(self.numberOfFrame):
                    
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
                for val in range(self.numberOfFrame):
                    
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
        
        for num in self.frameEntry:
            framePairs.append([0,0])
        
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
                zeroZeroList = []
                zeroOneList = []
                oneZeroList = []
                oneOneList = []
                faultCount += 1
                for val in range(self.numberOfFrame):

                    found = -1
                    frame = self.frameEntry[val].get()
                    curr = index

                    #if (0,0) put in (0,0) list
                    if (framePairs[val][0] == 0 and framePairs[val][1] == 0):
                        zeroZeroList.append(val)
                        

                    #if (0,1) put in (0,1) list
                    if (framePairs[val][0] == 0 and framePairs[val][1] == 1):
                        zeroOneList.append(val)

                    #if (1,0) put in (1,0) list
                    if (framePairs[val][0] == 1 and framePairs[val][1] == 0):
                        oneZeroList.append(val)

                    #if (1,1) ignore actually don't do this thing
                    if (framePairs[val][0] == 1 and framePairs[val][1] == 1):
                        oneOneList.append(val)


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
