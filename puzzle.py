
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
                
        self.solved=False        
                
    def __getitem__(self,pos):
         return self.puzzle[pos[0]][pos[1]].value

    def __str__(self):       
        

        return f'object.puzzle is a dict with {len(self.puzzle)} members each of them is dict of {len(self.puzzle[1])} objects of type CELL '


    def __repr__(self):

    
        for row in range(1,10):
            print("")
            print("----------------------------------")
        
            for column in range(1,10):
            
                print('|{}|'.format(self.puzzle[row][column].value),end=" ")     
        
        print("  ")    
        print("----------------------------------")    
        
        return f'The above printing shows the values of sudoku row by row'    

  
            
    def solution(self):
        
        if self.solved:

            solution=[]
            
            for row in range(1,10):
                for column in range(1,10):
                    
                    solution.append(self.puzzle[row][column].value)

            return solution    

        else:
             return 0        
    

    def to_list(self):
        solution = []
        
        for row in range(1,10):
                for column in range(1,10):
                    
                    solution.append(self.puzzle[row][column].value)

        return solution            
    
       
       