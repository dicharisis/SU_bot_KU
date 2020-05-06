from Locators import Locators
from Numbers_Draw import Nums
from selenium.common.exceptions import NoSuchElementException

class Parser():

    def __init__(self,browser):

      self.browser=browser
    
    @property
    def parse_page(self):

        
        #Find all elements of Locator.LEVEL_1 
        print("******Parsing*********")
        print(f'Find web elements with tag ({Locators.LEVEL_1})')  

        try:

            web_elements_level_1=self.browser.find_elements_by_css_selector(Locators.LEVEL_1)  
        
        except NoSuchElementException: 
            
            print("*****NOTHING FOUND*****")
            
        
        #Find all elements of Locator.LEVEL_2
        print(f'Find ({Locators.LEVEL_2}) tags in already parsed webelements')

        web_elements_level_2=[]    
        for element in web_elements_level_1:
            try:
                web_elements_level_2.append(element.find_element_by_css_selector(Locators.LEVEL_2))   
            except:
                web_elements_level_2.append(0)    
        
        
        return web_elements_level_2   
     
       
    
    
    
    @property
    def extract_info(self):   

        #Find all elements of Locator.LEVEL_3
        print(f'Get ({Locators.LEVEL_3}) tag attribute the parsed page')

        numbers=Nums()
     
        web_elements_level_3=[]
        for element in self.parse_page:
           
            if type(element)!=int:           
                web_elements_level_3.append(element.get_attribute(Locators.LEVEL_3) )           
            else:
                web_elements_level_3.append(0)
        
        print("Match the tag 'path' attribute 'd' with a number")
        sudoku_nums_list=[]
        
        for item in web_elements_level_3:
           
            for number in numbers.num:
                
                if item==number:
                    sudoku_nums_list.append(numbers.num[number])
                    break
            else:
                sudoku_nums_list.append(0)    




        return sudoku_nums_list

            
    
       