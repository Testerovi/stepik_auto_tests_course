from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.CSS_SELECTOR, "button#book").click()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_field.click()
    input_field.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button#solve").click()
finally:
    print(browser.switch_to.alert.text)
    browser.quit()
