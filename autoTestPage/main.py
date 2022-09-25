
# https://selenium-python.readthedocs.io/page-objects.html

import unittest
from selenium import webdriver
import page 

class PythOrgSeach(unittest.TestCase):#test new page or functoin of website (test case)
    
    def setUp(self):#constructor for unittest, called per test case
        print('SET UP CALLED SUCESSFULLY')
        self.driver = webdriver.Chrome(r"C:\Users\16075\Documents\chromeD\chromedriver.exe")
        self.driver.get("https://www.python.org/") #testing python website
        
    def test_example(self):#start with test, INSURES unittest will run
        print('TEST BEING CALLED SUCESSFULLY')
        assert True
        
    # def test_title(self):
    #     mainPage= page.MainPage(self.driver)
    #     assert mainPage.is_title_matches()#if false, raise's assertion error
           
    def test_search_python(self):
        
        mainPage= page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        #Sets the text of search textbox to "pycon"
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        #go to page serch pycon
        search_results_page = page.SearchResultPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found()
        
    def test_hoverOverDownloads_go_to_openSource(self):
        
        mainPage= page.MainPage(self.driver)
        mainPage.hover_downloads()
        
        search_sourceCode_page = page.DownloadsPage(self.driver)
        assert search_sourceCode_page.source_code()
        print("SOURCE CODE REACHED")

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()