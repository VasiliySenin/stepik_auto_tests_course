from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.NAME, 'first_name')
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, 'firstname')
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

    # успеваем скопировать код за 30 секунд
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла