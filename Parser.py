from Locators import Locators
from Numbers_Draw import Nums

from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

class Parser():

    def __init__(self,browser):

      self.browser=browser
     
    
    @property
    def parse_page(self):

        print("******Parsing*********")

        #Find all elements of Locator.MAIN_LOCATOR  

        print(f'Find web elements with tag ({Locators.MAIN_LOCATOR})')  

        # try:
        #     WebDriverWait(self.browser,10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR,Locators.MAIN_LOCATOR)) )
        try:    
            self.parsed_elements=self.browser.find_elements_by_css_selector(Locators.MAIN_LOCATOR)  
        
        # except TimeoutException:
        #     print(f"Too many time to Locate {Locators.MAIN_LOCATOR} ")
        
        except NoSuchElementException: 
            
            print("**MAIN LOCATOR***NOTHING FOUND*****")



        
        #Find all elements of Locator.LEVEL_1  

        print(f'Find web elements with tag ({Locators.LEVEL_1})')  

        try:
            WebDriverWait(self.browser,10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR,Locators.LEVEL_1)) )
            
            web_elements_level_1=self.browser.find_elements_by_css_selector(Locators.LEVEL_1)  
        
        except TimeoutException:
            print(f"Too many time to Locate {Locators.LEVEL_1} ")
        
        except NoSuchElementException: 
            
            print("**LEVEL_1***NOTHING FOUND*****")
     
        
        #Find all elements of Locator.LEVEL_2
        print(f'Find ({Locators.LEVEL_2}) tags in already parsed webelements')
        
        
        try:
            WebDriverWait(self.browser,10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR,Locators.LEVEL_2)) )
           
            web_elements_level_2=[]  
            
             

            for element in web_elements_level_1:
                
                try:
                    web_elements_level_2.append(element.find_element_by_css_selector(Locators.LEVEL_2))   
                    print("Command executed")
                
                except NoSuchElementException:
                    web_elements_level_2.append(0)    
        
        except TimeoutException:
            print("page took too long")

       
            
        
        return web_elements_level_2   
     
       
    
    
    
    @property
    def extract_info(self):   

        #Find all elements of Locator.LEVEL_3
        parsed_page=self.parse_page
        numbers=Nums()
     
        web_elements_level_3=[]
        for element in parsed_page:
           
            if type(element)!=int:           
                web_elements_level_3.append(element.get_attribute(Locators.LEVEL_3) )           
            else:
                web_elements_level_3.append(0)
        
        print("Find numbers from SVG draw")
        sudoku_nums_list=[]
        
        for item in web_elements_level_3:
                     
            if item in numbers.num:
                sudoku_nums_list.append(numbers.num[item])
                
            else:
                sudoku_nums_list.append(0)    


        self.unsolved=sudoku_nums_list
        
        return sudoku_nums_list

           
    