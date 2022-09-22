from selenium import webdriver
from selenium.webdriver.common.keys import Keys #access enter and space, tab,etc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver_path = r"C:\Users\16075\Documents\chromeD\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

print(type(driver.title))

search = driver.find_element("name", "s") #search box, search box name = s
search.send_keys('test') #what is going in the search box

search.send_keys(Keys.RETURN)

# https://selenium-python.readthedocs.io/locating-elements.html
#documenation in case there update
try:
    main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
    articles = main.find_elements('tag name',"article")
    for article in articles:
        header = article.find_element('class name', 'entry-summary')
        print(header.text)
   # print(main.text) #printed content in id main, search result for test key word
    
    #except: runs when try fails
finally: # runs no matter what
    driver.quit()
    
#main = driver.find_element("id", "main")

# time.sleep(5)

# print(main.text)

driver.quit()