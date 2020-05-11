  


class Calculator():

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

    
    def simple_solver(self):
        
        self.check_puzzle
        
        solved_list=[]
        counter=1
        
        while(self.row_solver!=0 and self.column_solver!=0) :
            counter+=1
        
        for row in range(1,10):
            for column in range(1,10):
                if self.puzzle[row][column].value==0:
                    
                    print("Puzzle can not be solved with Simple Solver")      
                    return 0 

                else:
                    solved_list.append(self.puzzle[row][column].value)
        
        
        print(f"Puzzle solved with Solver Level 1 in {counter} steps")
        return solved_list

    
    
    def solve(self):
        
        simple_solver=self.simple_solver()
        
        
        if simple_solver==0:
 
            self.advanced_solver()
            return 0

        else:

            return simple_solver   



    
    
    
   
    def advanced_solver(self):
        
        possibs_in_row=defaultdict(dict)
        possibs_combinations=0
        #counter=0
        for row in range(1,10):
            for column,cell in self.puzzle[row].items():
                newDict = dict(filter(lambda elem: elem[1] == 0, cell.pos_nums.items()))
                if len(newDict) ==2:
                   possibs_in_row[row][column]=newDict
        
        for value in possibs_in_row.values():
            possibs_combinations+=len(value)
            print(value)           

        # possibs_combinations=int(math.pow(2,possibs_combinations))
        # print(f'Possible combinations in row = {possibs_combinations}')

        self.try_the_combinations(possibs_in_row,possibs_combinations)

    
    
    
    def try_the_combinations(self,possibs_in_row,combinations):
        
        bin_list=[]
        temp=dict(self.puzzle)


        print(f"bin_list length = {len(bin_list)}")    
            


        for combination in range(int(math.pow(2,combinations))):
            
            # binary=bin(int(math.pow(2,comb)))
      
            # print(f'binary list = {len(binary[2:])}') 
            
            # for j,item in enumerate(binary[2:]):
            
           bin_list[j]=self.convert(combination)

             
            index=0
        
            for row,items in possibs_in_row.items():
                for column,item in items.items():
                    key=list(item.keys())                        
                    temp[row][column].pos_nums[ key[bin_list[index]]  ]=1
                    index+=1
                          
            
                    print(temp[row][column].pos_nums) 