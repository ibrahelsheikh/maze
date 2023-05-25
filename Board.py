from Constants import NUM_ROWS, CELL_VALUES, TERMINAL_CELLS

class Board(object):
    cellValues = {}  #  attribute Maps cell (x, y) to reward  or penalty

    def __init__(self, numRows = NUM_ROWS):  #method to initialize the board
        self.numRows = numRows  #set the number of rows using the default value if no
        self.initCellRewards()   #method to initialize the reward



    def initCellRewards(self):     #iterate each cell in cell values giving reward =0
        for xPos in range(NUM_ROWS):
            for yPos in range(NUM_ROWS):
                self.cellValues[(xPos, yPos)] = 0


    def createPenaltyCells(self):    # update some cell values to give them penalty
        for cell, val in CELL_VALUES:
            self.cellValues[cell[0], cell[1]] = val    #givving a penalty ex . cell(2,2)= -10



    def isTerminalCell(self, coord):   # ckeck if coordenates are of terminal or not
        return coord in TERMINAL_CELLS    # we assumed terminals are [(4, 5), (7, 4)]



    def isValidCell(self, coord, action):   # takes the coordenates and gets the new after action
        xCoord, yCoord = self.getCellAfterAction(coord, action)
        return (0 <= xCoord < NUM_ROWS  and 0 <= yCoord < NUM_ROWS)  # limits the move in the board only

    def getCellAfterAction(self, coord, action):
        xCoord, yCoord = coord
        if action == 'left':
            xCoord-=1
        elif action == 'right':
            xCoord+=1
        elif action == 'up':
            yCoord+=1
        elif action == 'down':
            yCoord-=1
        return (xCoord, yCoord) # new coordenated cell




    def getCellValue(self, coord): # to get the values of some cells
        return self.cellValues[coord]

    def getCells(self):  
        return self.cellValues.keys()# to get the position of cell

    def getCellMap(self): #mapping each cell to each value 
        return self.cellValues

    def getRewardCellsMap(self):
        return {cell: val for cell, val in self.cellValues.items() if val > 0} # reward of cell if reward >0

    def getPenaltyCellsMap(self):
        return {cell: val for cell, val in self.cellValues.items() if val < 0} # penatly of cell if reward <0
