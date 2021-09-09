class Cell:    
    def __init__(self, idx, rw, cl, blk):
        self.index = idx
        self.row = rw
        self.col = cl
        self.block = blk
        self.hasValue = False
        
    def SetCellValue(self, val):
        self.value = val
        self.hasValue = True
        
class Block:
    def __init__(self, idx, cells):
        self.index = idx
        self.cells = cells

class Row:
    def __init__(self, idx, cells):
        self.index = idx
        self.cells = cells
        
class Column:
    def __init__(self, idx, cells):
        self.index = idx
        self.cells = cells

class Board:
    def __init__(self, rows, cols, blks):
        self.rows = rows
        self.cols = cols
        self.blks = blks
        
    def CreateBoard(self):
        self.cells = []
        self.values = '000270180009005000800000507930000020450708691680492703008950006700000010'
        index = 0
        for value in self.values:
            row = index%9 + 1
            col = index/9 + 1
            block = SetBlock(index)
            cell = Cell(index, row, col, block)
            self.cells.insert(index, cell)
            
    
    