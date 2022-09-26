
from locator import *
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains
import time

class SearchTextElement(BasePageElement):
    #html name search box where search string is entered
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
    
    def click_ineractive_shell(self):
        element = self.driver.find_element( *MainPageLocators.LAUNCH_SHELL_BUTTON)
        element.click()
        
#https://www.tutorialspoint.com/how-can-i-perform-mouse-hover-action-in-selenium-python?ranMID=49144&ranEAID=a1LgFw09t88&ranSITEID=a1LgFw09t88-Sd8o.w9eFDO7w_gTzq.zdQ
    def hover_downloads(self):
        hover = ActionChains(self.driver)
        downloads = self.driver.find_element("link text","Downloads")
        hover.move_to_element(downloads).perform()
        
        drop_downMenu_item_of_interest = self.driver.find_element("link text","Source code")
        hover.move_to_element(drop_downMenu_item_of_interest).click().perform() 
        
    def from_mainPage_to_gitHub(self):
        self.hover_downloads()
        # time.sleep(3)
        sourcePage=self.driver.find_element("partial link text","Latest Python 3 Release")
        ActionChains(self.driver).move_to_element(sourcePage).click().perform()
        
        gitHubPage=self.driver.find_element("partial link text","PEP 623")
        ActionChains(self.driver).move_to_element(gitHubPage).click().perform()
        time.sleep(3)
        
class SearchResultPage(BasePage):
    
    def is_results_found(self):
        return "No results found." not in self.driver.page_source

class DownloadsPage(BasePage):
    def source_code(self):
        x= f"the title of the page: {self.driver.title}"
        print(x)
        return x
    
class Latest_In_Python3(BasePage):
    def is_results_found(self):
        x= f"the title of the page: {self.driver.title}"
        print(x.upper())
        return "No results found." not in self.driver.page_source