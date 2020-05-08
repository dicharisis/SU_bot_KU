from Locators import Locators

from selenium.common.exceptions import NoSuchElementException



class Robot():

    def __init__(self,browser):

        self.browser=browser

    
    def select_difficulty(self,difficulty):

        index={'easy':0,'medium':1,'hard':2,'expert':3}

        try:
             web_element=self.browser.find_element_by_css_selector(Locators.SEL_DIF_BUTTON)    
            

        except NoSuchElementException:
            print("***********Can not find Difficulty menu***************")
        
        self.browser.implicitly_wait(1)    
        web_element.click()
        
        
        web_elements=self.browser.find_elements_by_css_selector(Locators.SEL_DIF_OPT)
        self.browser.implicitly_wait(1) 
        web_elements[index[difficulty]].click()    
        