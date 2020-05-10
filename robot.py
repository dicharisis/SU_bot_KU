from Locators import Locators
from puzzle import PUZZLE

import time

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
            raise NoSuchElementException
        
        except TimeoutException:
            print("Too many time to find difficulty link")  
            raise TimeoutException   
        
        
        web_elements[index[difficulty]].click()    
        
        
        return WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,Locators.MAIN_LOCATOR)))
        
    @property
    def find_cell(self):

        try:
            WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located(  (By.CSS_SELECTOR,Locators.MAIN_LOCATOR) ))
            web_elements=self.browser.find_elements_by_css_selector(Locators.MAIN_LOCATOR)

        except NoSuchElementException:
            print(f"Can not find {Locators.MAIN_LOCATOR} in order to select cell")

        except TimeoutException:
            print("Too many time to find cell in order to select it ")  

        for element in web_elements:
            yield element          
    
    
    def solve_the_puzzle(self,solved_list,elements,unsolved_list):
        
        try:    
            buttons=self.browser.find_elements_by_css_selector(Locators.BUTTON_NUM)         
       
        
        except NoSuchElementException: 
            print("**MAIN LOCATOR***NOTHING FOUND*****")


        print(f'Length of solved = {len(solved_list)} Length of elements = {len(elements)} Length of unsolved = {len(unsolved_list)} Length of buttons= {len(buttons)}')
       
        for index,item in enumerate(unsolved_list):

            if item!=0:
                
                continue
            
            else:
                time.sleep(0.5)
                self.browser.execute_script("arguments[0].click();", elements[index])
                time.sleep(0.5)
                self.browser.execute_script("arguments[0].click()",buttons[ solved_list[index]-1 ])
        



        


       
        
