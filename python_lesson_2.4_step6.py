from selenium import webdriver
import time


try: 
    browser = webdriver.Chrome()
    
   # browser.implicitly_wait(5)
    
    browser.get("http://suninjuly.github.io/cats.html")

    time.sleep(2)

    button = browser.find_element_by_id("button")
    button.click()

    
finally:
    time.sleep(2)
    browser.quit()