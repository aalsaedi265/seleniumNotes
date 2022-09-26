

from selenium.webdriver.common.by import By

class MainPageLocators(object): #item of interest will located, ID of GO button is submit
    GO_BUTTON = (By.ID, 'submit')
    
    LAUNCH_SHELL_BUTTON = (By.ID, 'start-shell')
    
class SearchResultsPageLocators(object):
    #you type something go to new page
    #locator code like class above placed here
    pass

class SourceCodePageLocators_In_DowloadDropdown(object):
    pass