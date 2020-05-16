from puzzle import PUZZLE


from collections import defaultdict

class Calculator():

    def __init__(self,puzzle):

        self.pzl_to_solve = puzzle
        self.squares=defaultdict(list)
        self.rows=defaultdict(list)
        self.columns=defaultdict(list)
   



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
    def reserve_row(self,row,value):
        print("**IN RESERVE ROW")
        
        for k,cell in self.pzl_to_solve.puzzle[row].items():
                 
            if  cell.value == 0:
                if cell.pos_nums[value] == 0:
                    cell.pos_nums[value] = 1 
                    print(f" \t RESERVING value = {value} in row = {row} column = {k}  in cell poss_nums ={cell.pos_nums} ")
                    print("\t***************")

        return self    
    
    
    
    def reserve_column(self,column,value):
        print("**IN RESERVE Column")
       
        for k,row in self.pzl_to_solve.puzzle.items():       
           
            if row[column].value == 0:
                
                if row[column].pos_nums[value] == 0:
                    row[column].pos_nums[value] = 1
                    print(f" \t RESERVING value = {value} in row = {k} column = {column}  in cell poss_nums = {row[column].pos_nums} ")
                    print("\t***************")
       
        return self    
    
   
    
    def reserve_square(self,row,column,value):
        print("**IN RESERVE SQUARE")
        
      
        min_row,min_column,max_row,max_column=self.select_square(row,column)
        
      
        for row_temp in range(min_row,max_row):
            for column_temp in range(min_column,max_column):
                
                if self.pzl_to_solve.puzzle[row_temp][column_temp].value == 0:
                    if self.pzl_to_solve.puzzle[row_temp][column_temp].pos_nums[value] == 0:
                        self.pzl_to_solve.puzzle[row_temp][column_temp].pos_nums[value] = 1   

                        print(f'\tRESERVING value = {value} in row = {row_temp} column = {column_temp}  in cell poss_nums = {self.pzl_to_solve.puzzle[row_temp][column_temp].pos_nums}') 
                        print("\t***************")
        return self

#***********END of Reserve Methods****************************




#*******Reserve,row,column and square , cell by cell******
    
    def check_puzzle(self):
        print("IN CHECK PUZZLE")
        
        for row in range(1,10):
            
            for column in range(1,10):
                
                if self.pzl_to_solve.puzzle[row][column].value != 0:                
                 
                
                    value = self.pzl_to_solve.puzzle[row][column].value
                    print("\tITERATION IN CHECK PUZZLE")
                    print(f'\t row = {row} column = {column} value = {value} ')
                    print("\t***********")
                   
                    self.reserve_row(row,value)
                    self.reserve_column(column,value) 
                    self.reserve_square(row,column,value)       

#*********************************************************


    def my_iterator(self):
        square=0
                

        for row in range(1,10):            
                
            for column,cell in self.pzl_to_solve.puzzle[row].items():
                if column == 1 or column == 4 or column == 7:
                    square+=1

                if cell.value == 0:
                    self.rows[row].append(cell)
                    self.columns[column].append(cell)
                    self.squares[square].append(cell)

        print("ROWS")
        print(self.rows)
        print("**************************")
        print("COLUMNS")
        print(self.columns)          
        print("**************************")             
        print("SQUARES")
        print(self.squares)          
        print("**************************")          




    
    def row_solver(self):
        print("ROW SOLVER")

        single = 0
        doubles = defaultdict(dict)
        
        for num in range(1,10):
            
            for row in self.rows:
                check_list=[]
                
                for index,cell in enumerate(self.rows[row]):
                    
                    if cell.pos_nums[num] == 0:
                        check_list.append( (index,cell) )
                    
                    if len(check_list) > 2:
                       
                        break


                if len(check_list) == 1 :
                    self.rows[row].pop(check_list[0][0])
                      

                    
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
                    
                    if cell.pos_nums[num] == 0:
                        check_list.append(row)

                    if len(check_list) > 2:
                        break 
               



                if len(check_list) == 1:
                    self.pzl_to_solve.puzzle[check_list[0]][column].value = num 
                    self.pzl_to_solve.puzzle[check_list[0]][column].pos_nums={i:1 for i in self.pzl_to_solve.puzzle[check_list[0]][column].pos_nums}  
                    
                    print("COLUMN SOLVER SOLVES")
                    print("\t********")
                    print(f'\trow = {check_list[0]} column = {column} ')
                    print(f'\tnum = {num}')  
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
                    print(f'\trow = {check_list[0][0]} column = {check_list[0][1]} ')
                    print(f'\tnum = {num}')  
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
                 
                for num in range(1,10):
                    
                    if cell.pos_nums[num] == 0:
                        check_list.append( num )
                       
                    
                    if len(check_list) > 2:
                        
                        break
                    
                if len(check_list) == 1:
                    self.pzl_to_solve.puzzle[row][column].value = check_list[0]
                    
                   
                    print("CELL SOLVER SOLVES")
                    print("\t********")
                    print(f'\trow = {row} column = {column}')
                    print(f'\t num = {check_list[0]}')  
                    print("\t********")
                    print(self.pzl_to_solve.puzzle[row][column].pos_nums)
                    
                    self.reserve_row( row,check_list[0] )
                    self.reserve_column( column,check_list[0] )
                    self.reserve_square( row,column,check_list[0] )

                    single += 1

                elif len(check_list) == 2:

                    doubles[row][column]=check_list

        return single,doubles            
         

    
                


    def simple_solver(self):

       
        
        self.check_puzzle()
        
        print([self.pzl_to_solve])

        self.my_iterator()
        

    
    
    # def solve(self):
        
    #     simple_solver=self.simple_solver()
        
        
    #     if simple_solver==0:
 
    #         #self.advanced_solver()
    #         return 0

    #     else:

    #         return simple_solver   



    
    
    
   
    # def advanced_solver(self):
        
    #     possibs_in_row=defaultdict(dict)
    #     possibs_combinations=0
    #     #counter=0
    #     for row in range(1,10):
    #         for column,cell in self.puzzle[row].items():
    #             newDict = dict(filter(lambda elem: elem[1] == 0, cell.pos_nums.items()))
    #             if len(newDict) ==2:
    #                possibs_in_row[row][column]=newDict
        
    #     for value in possibs_in_row.values():
    #         possibs_combinations+=len(value)
    #         print(value)           

    #     # possibs_combinations=int(math.pow(2,possibs_combinations))
    #     # print(f'Possible combinations in row = {possibs_combinations}')

    #     self.try_the_combinations(possibs_in_row,possibs_combinations)

    
    
    
    # def try_the_combinations(self,possibs_in_row,combinations):
        
    #     bin_list=[]
    #     temp=dict(self.puzzle)


    #     print(f"bin_list length = {len(bin_list)}")    
            


    #     for combination in range(int(math.pow(2,combinations))):
            
    #         # binary=bin(int(math.pow(2,comb)))
      
    #         # print(f'binary list = {len(binary[2:])}') 
            
    #         # for j,item in enumerate(binary[2:]):
            
    #        bin_list[j]=self.convert(combination)

             
    #         index=0
        
    #         for row,items in possibs_in_row.items():
    #             for column,item in items.items():
    #                 key=list(item.keys())                        
    #                 temp[row][column].pos_nums[ key[bin_list[index]]  ]=1
    #                 index+=1
                          
            
    #                 print(temp[row][column].pos_nums) 