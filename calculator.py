from puzzle import PUZZLE
import copy
from collections import defaultdict

class Calculator():

    def __init__(self,puzzle):

        self.pzl_to_solve = puzzle
   



    def select_square(self,row,column):
        
        
        #SET min_row
        if row < 4:
            min_row = 1
       
        elif row < 7:
            min_row = 4
       
        elif row < 10:
            min_row = 7       
        
        #SET min_column
        if column < 4:
            min_column = 1
        
        elif column < 7:
            min_column = 4
        
        elif column < 10:
            min_column = 7   

        max_row = min_row+3
        max_column = min_column+3    

        return (min_row,min_column,max_row,max_column )


#******Reserve Methods******************************
    
    #***ROW***
    def reserve_row(self,row,value):        
        
        for cell in self.pzl_to_solve.puzzle[row].values():
                 
            if  cell.value == 0:
                if cell.pos_nums[value] == 0:
                    cell.pos_nums[value] = 1 
                    

        return self    
    
    
    #***COLUMN***
    def reserve_column(self,column,value):        
       
        for row in self.pzl_to_solve.puzzle.values():       
           
            if row[column].value == 0:
                
                if row[column].pos_nums[value] == 0:
                    row[column].pos_nums[value] = 1
                  
       
        return self    
    
   
    #***SQUARE***
    def reserve_square(self,row,column,value):      
        
        min_row,min_column,max_row,max_column=self.select_square(row,column)
        
      
        for row_temp in range(min_row,max_row):
            for column_temp in range(min_column,max_column):
                
                if self.pzl_to_solve.puzzle[row_temp][column_temp].value == 0:
                    if self.pzl_to_solve.puzzle[row_temp][column_temp].pos_nums[value] == 0:
                        self.pzl_to_solve.puzzle[row_temp][column_temp].pos_nums[value] = 1   

                       
        return self

#***********END of Reserve Methods****************************




#*******Reserve,row,column and square , cell by cell******
    
    def check_puzzle(self):
        
        for row in range(1,10):
            
            for column in range(1,10):
                
                if self.pzl_to_solve.puzzle[row][column].value != 0:               
                 
                    value = self.pzl_to_solve.puzzle[row][column].value
                   
                    self.reserve_row(row,value)
                    self.reserve_column(column,value) 
                    self.reserve_square(row,column,value)       

#*********************************************************




    
    def row_solver(self):
        print("ROW SOLVER")

        single = 0
        doubles = defaultdict(dict)
        
        for num in range(1,10):
            
            for row in range(1,10):
                check_list = []
                
                for column,cell in self.pzl_to_solve.puzzle[row].items():
                    if cell.value == 0:
                        
                        if cell.pos_nums[num] == 0:
                            check_list.append(column)
                        

                        if len(check_list) > 2:
                            
                            break


                if len(check_list) == 1 :
                    self.pzl_to_solve.puzzle[row][check_list[0]].value = num  
                    self.pzl_to_solve.puzzle[row][check_list[0]].pos_nums={i:1 for i in self.pzl_to_solve.puzzle[row][check_list[0]].pos_nums }                  
                   
                    print("ROW SOLVER SOLVES")
                    print("\t********")
                    print(f'\tvalue = {num} in ') 
                    print(f'\trow = {row} column = {check_list[0]}')                    
                    print("\t********")
                 
                    self.reserve_column(check_list[0],num)
                   
                    self.reserve_square(row,check_list[0],num)
                   
                    single += 1
             
            
                elif len(check_list) == 2:

                    doubles[num][row] = check_list
        
        return single,doubles




    
    def column_solver(self):
        print("COLUMN SOLVER")
        single = 0
        doubles = defaultdict(dict)
        
        for num in range(1,10):

            for column in range(1,10):
                check_list = []
                
                for row in range(1,10):
                    cell=self.pzl_to_solve.puzzle[row][column]
                    if cell.value == 0:
                    
                        if cell.pos_nums[num] == 0:
                            check_list.append(row)

                        if len(check_list) > 2:
                            break 
               



                if len(check_list) == 1:
                    self.pzl_to_solve.puzzle[check_list[0]][column].value = num 
                    self.pzl_to_solve.puzzle[check_list[0]][column].pos_nums={i:1 for i in self.pzl_to_solve.puzzle[check_list[0]][column].pos_nums}  
                    
                    print("COLUMN SOLVER SOLVES")
                    print("\t********")
                    print(f'\tvalue = {num} in ') 
                    print(f'\trow = {check_list[0]} column = {column} ')                     
                    print("\t********")
                    self.reserve_row(check_list[0],num)
                    self.reserve_square(check_list[0],column,num)

                    single += 1
             
                elif len(check_list) == 2:

                    doubles[num][column] = check_list
        
        return single,doubles   
      




    
    def square_solver(self):      
        
        print("SQUARE SOLVER")
        
        single = 0
        doubles = defaultdict(dict) 
        
        for min_row in range(1,8,3):
       
            for min_column in range(1,8,3):

                for num in range(1,10):                
                    check_list=[]

                    for row in range(min_row,min_row+3):
                        
                        for column in range(min_column,min_column+3):

                            cell=self.pzl_to_solve.puzzle[row][column]
                            
                            if cell.value == 0:
                                if cell.pos_nums[num] == 0:
                                    check_list.append( (row,column) )
                                    

                                if len(check_list) > 2:
                                    
                                    break    
                        

                        if len(check_list) > 2:
                                
                                break                   
                

                

                if len(check_list) == 1:
                    
                    self.pzl_to_solve.puzzle[check_list[0][0]][check_list[0][1]].value = num
                    self.pzl_to_solve.puzzle[check_list[0][0]][check_list[0][1]].pos_nums={i:1 for i in self.pzl_to_solve.puzzle[check_list[0][0]][check_list[0][1]].pos_nums}  
                    
                    print("SQUARE SOLVER SOLVES")
                    print("\t********")
                    print(f'\tvalue = {num} in ') 
                    print(f'\trow = {check_list[0][0]} column = {check_list[0][1]} ')                    
                    print("\t********")
                   
                    self.reserve_row( check_list[0][0] , num )
                    self.reserve_column( check_list[0][1] , num )


                    single += 1

                elif len(check_list) == 2:
                    
                    doubles[num][(min_row,min_column)]=check_list

        return single,doubles       



    
    def cell_solver(self):
        print("CELL SOLVER")
        single = 0
        doubles = defaultdict(dict)   

        for row in range(1,10):
        
            for column,cell in self.pzl_to_solve.puzzle[row].items():
                check_list =  [ ] 
                if self.pzl_to_solve.puzzle[row][column].value == 0:
                 
                    for num in range(1,10):
                        
                        if cell.pos_nums[num] == 0:
                            check_list.append( num )
                        
                        
                        if len(check_list) > 2:
                            
                            break
                    
                    if len(check_list) == 1:
                        self.pzl_to_solve.puzzle[row][column].value = check_list[0]
                        
                    
                        print("CELL SOLVER SOLVES")
                        print("\t********")
                        print(f'\t value = {check_list[0]} in ') 
                        print(f'\trow = {row} column = {column}')                        
                        print("\t********")
                        
                        
                        self.reserve_row( row,check_list[0] )
                        self.reserve_column( column,check_list[0] )
                        self.reserve_square( row,column,check_list[0] )

                        single += 1

                    elif len(check_list) == 2:

                        doubles[row][column]=check_list

        return single,doubles            
         




    def solver(self):
        
        if self.simple_solver():
            print(f"Puzzle solved with Solver Level 1 ")
            return 1

        else:
            if self.advanced_solver():
                return 1    
            
            else:
                return 0 

    
                


    def simple_solver(self):           
                   
        
        print([self.pzl_to_solve])

        
        while(True  ):
            cell_solv=self.row_solver()[0]
            row_solv=self.cell_solver()[0] 
            col_solv= self.column_solver()[0]
            squ_solv= self.square_solver()[0]
            
           
            if row_solv==0 and col_solv==0 and squ_solv==0 and cell_solv==0:
                break

        self.rsolver=(self.row_solver()[1],'Rsolver')                  
        self.csolver=(self.cell_solver()[1],'Csolver')
        self.colsolver=(self.column_solver()[1],'Colsolver')
        self.sqsolver=(self.square_solver()[1],'Sqsolver')     
        

        for row in range(1,10):
            for column in range(1,10):                
                
                if self.pzl_to_solve.puzzle[row][column].value==0:
                    
                    print("Puzzle can not be solved with Simple Solver")                  
                    return 0             
                               
                
                      
        self.pzl_to_solve.solved = True 
        return 1
    

    
    
    def advanced_solver(self):
        
        
        bin_list=[]               
        temp=copy.deepcopy(self.pzl_to_solve.puzzle)

        sequence=self.select_solver_sequence()       
        

        for solver in sequence:   
            possibs=[len(item) for item in solver[0].values() ]            
            combinations= (2**sum(possibs))     
        
            print(f'Pairs = {sum(possibs)}')
            print(f'Possible combinations = 2^pairs = {combinations}')

            for combination in range(combinations):            
            
                bin_list=self.convert(combination,sum(possibs))        

                print(f'Solver\'s contents are: {solver[0]}')
                print(f"Trying combination {combination}")
                print(f'in binary {bin_list}')   
            
            
                self.advanced_worker(solver,bin_list)

                if self.simple_solver():
                    print(f"Puzzle solved with advanced solver -> {solver[1]}")
                    print(f'The combination is {combination} binary = {bin_list}  in total combinations {combinations}' )
               
                    return 1
           
                else:
                    print("Trying next combination")
                    self.pzl_to_solve.puzzle= copy.deepcopy(temp)
                        
    
        return 0     



    def advanced_worker(self,solver,bin_list):

        if solver[1]=='Csolver':
            index=0
            for row,elements in solver[0].items():
                for column,item in elements.items():
                    #print(bin_list)
                    #print(f'row = {row} column = {column} item = {item}')                        
                    self.pzl_to_solve.puzzle[row][column].pos_nums[ item[ bin_list[index]]  ] = 1
                    index+=1                         
            
                    print(self.pzl_to_solve.puzzle[row][column].pos_nums) 

        elif solver[1]=='Rsolver':
            
            index=0
            for num,elements in solver[0].items():
                for row,column_list in elements.items():
                    #print(bin_list)
                    #print(f'row = {row} num = {num} column = {column_list[bin_list[index]]} ')                        
                    self.pzl_to_solve.puzzle[row][ column_list[ bin_list[index] ]].pos_nums ={ i:1 if i!=num else 0 for i in  self.pzl_to_solve.puzzle[row][ column_list[ bin_list[index] ]].pos_nums} 
                    
                    index+=1                         
        
       
        elif solver[1]=='Colsolver':
            index=0
            for num,elements in solver[0].items():
                for column,row_list in elements.items():
                    #print(bin_list)
                    #print(f'row = {row_list[bin_list[index]]} num = {num} column = {column} ')                        
                    self.pzl_to_solve.puzzle[row_list[bin_list[index]]][column].pos_nums ={ i:1 if i!=num else 0 for i in  self.pzl_to_solve.puzzle [row_list[bin_list[index]]] [column].pos_nums} 
                    
                    index+=1                       

                    


    def select_solver_sequence(self):
        
        cell_solver_size=( sum( [ len(i) for i in self.csolver[0].values() ] ),self.csolver )
        column_solver_size=( sum( [ len(i) for i in self.colsolver[0].values() ] ),self.colsolver )
        row_solver_size=(sum( [ len(i) for i in self.rsolver[0].values() ] ),self.rsolver )
        
        
        
        sorted=[cell_solver_size,column_solver_size,row_solver_size]

        sorted.sort(key=lambda x: x[0])
       
        for j in sorted:
            print(f'Solver {j[1][1]} has {j[0]} pairs')        
        
        result = [x[1] for x in sorted ]

        return result


    
    @staticmethod
    def convert(combination,combinations):        
                
        binary=[int(i) for i in  bin(combination)[2:]]
        
        result =[ 0 for i in range((combinations+1)-len(binary))  ]
        
        result[-1:]=binary
        
        return result

