
from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    #html name for  seach box = q for python website
    locator= "q"

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
    
class MainPage(BasePage):
    
    search_text_element = SearchTextElement()

# https://selenium-python.readthedocs.io/getting-started.html
    def is_title_matches(self): 
        return "Python" in self.driver.title
    #wirte test in main file
    
    def click_go_button(self):
        #https://selenium-python.readthedocs.io/locating-elements.html
        element = self.driver.find_element( *MainPageLocators.GO_BUTTON )
        #https://selenium-python.readthedocs.io/navigating.html
        element.click()
        #go to locater,make button
        

class SearchResultPage(BasePage):
    
    def is_results_found(self):
        return "No results found." not in self.driver.page_source