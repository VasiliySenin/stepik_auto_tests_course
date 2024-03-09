from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
z=browser.find_element(By.ID, "answer")
z.send_keys(y)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option2.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()