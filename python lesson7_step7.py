from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)
z=browser.find_element(By.ID, "answer")
z.send_keys(y)
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
option2.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()