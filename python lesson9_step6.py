from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
but=browser.find_element(By.CSS_SELECTOR, "button")
but.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
z=browser.find_element(By.ID, "answer")
z.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
browser.quit()