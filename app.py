from Parser import Parser
from Locators import Locators
from puzzle import PUZZLE
from robot import Robot
from calculator import Calculator

import os
import time


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#**********CREATE EXECUTABLE PATH FOR chrome driver**************

start=time.time()
os.chdir('utils')
chrome_driver_path=os.getcwd()
os.chdir('..')

#*****************************************************************





#**********INSTANTIATE chrome web driver wiht "https://sudoku.com/"*

chrome=webdriver.Chrome(executable_path=chrome_driver_path+"/chromedriver")
chrome.get("https://sudoku.com/")

#*******************************************************************




#********FIND IF ALL DESIRED ELEMENTS EXIST*********************

try:
    WebDriverWait(chrome,11).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR,Locators.MAIN_LOCATOR)) )
    print("page is ready")
except TimeoutException:
    print("Page loading took too much")

#**************************************************************** 






#*******Rbobot SELECT DIFFICULTY********************************
robot=Robot(chrome)

difficulty=input('Select the difficulty of Sudoku : easy || medium || hard || expert :')

if robot.select_difficulty(difficulty):
    pass
#****************************************************************


#*******PUZZLE SOLVER LOGIC**************************************

parser=Parser(chrome)

my_puzzle=PUZZLE(parser.extract_info)


my_calc=Calculator(my_puzzle)

my_calc.check_puzzle()

if my_calc.solver():
    
    #Print solved puzzle
    print([my_calc.pzl_to_solve])
    
    #Convert puzzle to list if it is solved in order robot can solve it.
    solved=my_calc.pzl_to_solve.solution()
    
    #***********ROBOT SOLVES THE PUZZLE IF CAN BE SOLVED************* 
    robot.solve_the_puzzle(solved,parser.parsed_elements,parser.unsolved)

#****************************************************************


end=time.time()


print(f"App took {end-start} seconds to complete")
chrome.close()
          



