
# https://selenium-python.readthedocs.io/page-objects.html

import unittest
from selenium import webdriver
import page 

class PythOrgSeach(unittest.TestCase):#test new page or functoin of website (test case)
    
    def setUp(self):#constructor for unittest, called per test case
        print('setUp called')
        self.driver = webdriver.Chrome(r"C:\Users\16075\Documents\chromeD\chromedriver.exe")
        self.driver.get("https://www.python.org/") #testing python website
        
    def test_example(self):#start with test, unittest will ru n
        print('test')
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
        search_results_page = page.SearchResultPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found()

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()