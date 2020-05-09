from Locators import Locators
from puzzle import PUZZLE

from collections import defaultdict

from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException



class Robot():

    def __init__(self,browser):

        self.browser=browser
      

    
    def select_difficulty(self,difficulty):

        index={'easy':0,'medium':1,'hard':2,'expert':3}

        try:
            WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located( (By.CLASS_NAME,Locators.SEL_DIF_BUTTON) ))           
          
            element = self.browser.find_element_by_class_name(Locators.SEL_DIF_BUTTON)
            
        except NoSuchElementException:
            print(f"Can not find {Locators.SEL_DIF_BUTTON} ")

        except TimeoutException:
            print("**To many time to  find difficulty MENU****")
            raise TimeoutException
        
        
        self.browser.execute_script("arguments[0].click();", element)
      
        

       
        try: 
            WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located( (By.CSS_SELECTOR,Locators.SEL_DIF_OPT) ))
            
            web_elements=self.browser.find_elements_by_css_selector(Locators.SEL_DIF_OPT)
        
        except NoSuchElementException:
            print(f"Can not find Locator {Locators.SEL_DIF_OPT}")
        
        except TimeoutException:
            print("Too many time to find difficulty link")  
            raise TimeoutException   
        
        
        web_elements[index[difficulty]].click()    
        
        
        return WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,Locators.MAIN_LOCATOR)))
        
    @property
    def select_cell(self):

        try:
            WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located(  (By.CSS_SELECTOR,Locators.MAIN_LOCATOR) ))
            web_elements=self.browser.find_elements_by_css_selector(Locators.MAIN_LOCATOR)

        except NoSuchElementException:
            print(f"Can not find {Locators.MAIN_LOCATOR} in order to select cell")

        except TimeoutException:
            print("Too many time to find cell in order to select it ")  

        for element in web_elements:
            yield element          
    
    
    def solve_the_puzzle(self,solved_puzzle,unsolved_puzzle):
       
        unsolved=defaultdict(dict)
        notsolved_puzzle=PUZZLE(unsolved_puzzle)
        
       
        
        for row in range(1,10):
            for column in range(1,10):
                
                val=notsolved_puzzle.__getitem__((row,column))
                if val!=0:
                    unsolved[row][column]=val

        
        gen=self.select_cell
        
        for row in range(1,10):
            for column in range(1,10):
                value=solved_puzzle.puzzle[row][column].value
                element=next(gen)
                cell=element.find_element_by_css_selector(Locators.LEVEL_1)
                self.browser.execute_script("arguments[0].click();", cell)
                return 0
                
  
                
