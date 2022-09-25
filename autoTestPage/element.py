

from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    #locator defined in page.py
    
    def __set__(self,obj,value):
        driver = obj.driver #webdriver
        #wait 100sec until lamdba code is true
        WebDriverWait(driver,100).until(
            #looking at the HTLM of a page, under name, find value given to locator
            lambda driver:driver.find_element("name",self.locator)
            )# find the inpute box on the page
        driver.find_element("name",self.locator).clear()
        driver.find_element("name",self.locator).send_keys(value)
        
    def __get__(self,obj,owner):#implement functionality
        driver = obj.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element("name",self.locator) #wait to generate
            )
        element = driver.find_element("name",self.locator)#id,class,tag, etc
        return element.get_attribute("value") #present it