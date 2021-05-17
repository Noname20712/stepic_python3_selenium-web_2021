from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
   #time.sleep(2)
   

    # Ваш код, который делает что то
    
    dollars = WebDriverWait(browser, 7).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id ("book")
    button.click()


    # Блок заполнения полей.
    x_block = browser.find_element_by_id ("input_value")
    x1 = x_block.text
    otvet = calc(x1)
    
    pole_vvoda = browser.find_element_by_id ("answer")
    pole_vvoda.send_keys(otvet)


    time.sleep(1)
  
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[id='solve']")
    button.click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    