

from selenium import webdriver

chrome_driver_path = r"localhost\Ubuntu\home\aalsaedi265\development\work\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com")
driver.quit()