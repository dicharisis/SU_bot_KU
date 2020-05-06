class CELL():

    def __init__(self,value):
       
       self.pos_nums={} 
       self.value=value
       
       for i in range(1,10):
           if self.value==0:
               self.pos_nums[i]=0 
           else:
               self.pos_nums[i]=1    


class PUZZLE():
    
    def __init__(self,puzzle_list):
        
        self.row={}
        self.column={}
        k=1
        l=1
        for item in puzzle_list:
            if l<10:
                self.column[l]=CELL(item)
                l+=1 
            if l==10:
                self.row[k]=self.column 
                l=1
                k+=1
                self.column={}
                

    def __str__(self):       
        

        return f'object.row is a dict with {len(self.row)} members each of them is dict of {len(self.row[1])} objects of type CELL '


    def __repr__(self):

        for i in self.row:
            print("  ")
            print("START ROW")
            print(f'ROW {i}')
            for j in self.row[i]:
                print(f'{self.row[i][j].value}')
            
            print("END of ROW")
            print("  ")    
        return f'The above printing shows the values of sudoku row by row'    