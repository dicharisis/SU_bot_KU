class CELL():

    def __init__(self,value):
       
       self.pos_nums={} 
       self.value=value

       self.pos_nums={x:0 if self.value==0 else 1 for x in range(1,10)}
       

class PUZZLE():
    
    def __init__(self,puzzle_list):
        
        self.puzzle={}
        cells_of_obj={}
        row=1
        column=1
        for item in puzzle_list:
            if column<10:
                cells_of_obj[column]=CELL(item)
                column+=1 
            if column==10:
                self.puzzle[row]=cells_of_obj 
                column=1
                row+=1
                cells_of_obj={}
                
                
    def __getitem__(self,pos):
        return self.puzzle[pos[0]][pos[1]].value

    def __str__(self):       
        

        return f'object.puzzle is a dict with {len(self.puzzle)} members each of them is dict of {len(self.puzzle[1])} objects of type CELL '


    def __repr__(self):

        for j,i in self.puzzle.items():
            print("  ")           
            print(f'ROW {j}')
            my_list=[i[k].value for k in range(1,10)]
            print(my_list)               
            print("END of ROW")
            print("  ")    
        return f'The above printing shows the values of sudoku row by row'    

    
    def reserve_row(self,row,value):
        
        for cell in self.puzzle[row].values():
             cell.pos_nums[value]=1 

        return self    
    
    
    def reserve_column(self,column,value):
        
        for row in self.puzzle.values():
           row[column].pos_nums[value]=1
       
        return self    
    
    def reserve_square(self,row,column,value):

        if row<4:
            min_row=1
        elif row<7:
            min_row=4
        elif row<10:
            min_row=7       
   
        if column<4:
            min_column=1
        elif column<7:
            min_column=4
        elif column<10:
            min_column=7   

        for row in range(min_row,min_row+3):
            for column in range(min_column,min_column+3):
                self.puzzle[row][column].pos_nums[value]=1    

        return self

    @property
    def check_puzzle(self):

        for row in range(1,10):
            for column in range(1,10):
                if self.puzzle[row][column].value!=0:
                    value=self.puzzle[row][column].value
                    self.reserve_row(row,value)
                    self.reserve_column(column,value)
                    self.reserve_square(row,column,value)       

    @property
    def row_solver(self):
        counter=0
        for row in range(1,10):
            for column,cell in self.puzzle[row].items():
                newDict = dict(filter(lambda elem: elem[1] == 0, cell.pos_nums.items()))
                if len(newDict) ==1:
                    self.puzzle[row][column].value=list(newDict.keys())[0]
                    counter+=1
                    value= self.puzzle[row][column].value
                    self.reserve_row(row,value)
                    self.reserve_column(column,value)
                    self.reserve_square(row,column,value)
        
        return counter



    @property
    def column_solver(self):
        counter=0
        for column in range(1,10):
            for row,cell in self.puzzle.items():
                newDict = dict(filter(lambda elem: elem[1] == 0, cell[column].pos_nums.items()))
                if len(newDict) ==1:
                    self.puzzle[row][column].value=list(newDict.keys())[0]
                    counter+=1 
                    value=self.puzzle[row][column].value
                    self.reserve_row(row,value)
                    self.reserve_column(column,value)
                    self.reserve_square(row,column,value)
        
        return counter    

    @property
    def solver_level_1(self):

        counter=1
        while(self.row_solver!=0 and self.column_solver!=0) :
            counter+=1
        
        for row in range(1,10):
            for column in range(1,10):
                if self.puzzle[row][column].value==0:
                    
                    print("Puzzle can not be solved with Solver Level 1")      
                    return 0 

        
        
        
        print(f"Puzzle solved with Solver Level 1 in {counter} steps")
        return 1