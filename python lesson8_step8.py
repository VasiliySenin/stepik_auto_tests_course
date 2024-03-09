from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
element1 = browser.find_element(By.NAME, "firstname")
element1.send_keys("s")
element2 = browser.find_element(By.NAME, "lastname")
element2.send_keys("ss")
element3 = browser.find_element(By.NAME, "email")
element3.send_keys("sss")
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys("C:/Users/senin/PycharmProjects/test3/venv/Lessons/example.txt")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()