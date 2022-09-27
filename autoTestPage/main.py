
# https://selenium-python.readthedocs.io/page-objects.html

import unittest
from selenium import webdriver
import page 

class PythOrgSeach(unittest.TestCase):#test new page or functoin of website (test case)
    
    def setUp(self):#constructor for unittest, called per test case
        print('SET UP CALLED SUCESSFULLY')
        self.driver = webdriver.Chrome(r"C:\Users\16075\Documents\work\chromeD\chromedriver.exe")
        self.driver.get("https://www.python.org/") #testing python website
        
    def test_example(self):#start with test, INSURES unittest will run
        print('TEST BEING CALLED SUCESSFULLY')
        assert True
           
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
        
    def test_download_sourceCode_latestRelease_Py3(self):
       
        mainPage = page.MainPage(self.driver)
        mainPage.from_mainPage_to_gitHub()       
        print('SOURCE CODE click on Python 3.10.7')
        
        search = page.Latest_In_Python3(self.driver)
        assert search.is_results_found()
        print('PEP 623')

    def tearDown(self):
        self.driver.close()
        
        
if __name__ == '__main__':
    unittest.main()
    
