        ###################################################################################
        # second page #####################################################################
        ###################################################################################
        self.memoryManagementPage = ttk.Frame(self.notebook)

        self.missCounter = 0
        self.hitCounter = 0


        # Table Look Up label label
        self.lookUpTimeString = StringVar()
        self.lookUpTime = Label(self.memoryManagementPage, textvariable=self.lookUpTimeString, relief=FLAT )

        self.lookUpTimeString.set("Table Lookup Time: ")
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
        self.leftBoxLineToBuffer = self.memoryArcitectureCanvas.create_line( 110, 110, 200, 200, arrow=LAST )
        self.rightBoxLineToBuffer = self.memoryArcitectureCanvas.create_line( 200, 200, 270, 100, arrow=LAST )


        #lines that connect double boxes
        self.topLineLeft = self.memoryArcitectureCanvas.create_line( 170, 100, 270, 80, arrow=FIRST )
        self.topLineRight = self.memoryArcitectureCanvas.create_line( 270, 80, 330, 90, arrow=FIRST )

        #right hand side double box
        self.rightBoxLeftHalf = self.memoryArcitectureCanvas.create_rectangle( 270, 90, 310, 110, fill="" )
        self.rightBoxRightHalf = self.memoryArcitectureCanvas.create_rectangle( 310, 90, 350, 110, fill="" )

        #farthest right hand line segment to memory pages
        self.memoryArcitectureCanvas.create_line( 350, 100, 400, 200, arrow=LAST )

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
        
        self.displayMemAccTimeNumber.insert(0, float("{0:.2f}".format(self.hitMissRatio( self.hitCounter,\
            int(self.memoryLookUpTimeNumber.get()), self.missCounter,\
            int(self.lookUpTimeNumber.get()) ) )))
        

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
        self.missNumber = Label(self.memoryManagementPage, textvariable=self.missNumberString, relief=FLAT )
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

        self.memoryArcitectureCanvas.itemconfig(self.rightBoxLineToBuffer, fill="blue")

        self.memoryArcitectureCanvas.itemconfig(self.rightBoxMemoryValue, text="value", fill="black")
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
