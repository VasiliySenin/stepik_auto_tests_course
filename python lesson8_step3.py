from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
a=browser.find_element(By.CSS_SELECTOR, '#num1').text
b=browser.find_element(By.CSS_SELECTOR, '#num2').text
sum=str(int(a)+int(b))
#browser.find_element(By.TAG_NAME, "select").click()
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(sum)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()