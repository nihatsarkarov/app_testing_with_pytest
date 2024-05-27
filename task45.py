import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

service = Service("C:/Users/lenovo/Desktop/task_selenium/pytest/chromedriver.exe")
options = Options()
driver = webdriver.Chrome(service=service, options=options)

def setup():
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    time.sleep(5) 

def test_color():
    try:
        eleCookiesDiv = driver.find_element(By.CSS_SELECTOR, 'div.cookies')
        assert eleCookiesDiv.value_of_css_property("background-color") == "rgba(255, 0, 0, 1)", "Test 1 fail"
    except NoSuchElementException:
        print("Element not found for test_color")
    except AssertionError as e:
        print(e)

def test_height():
    try:
        eleCookiesDiv = driver.find_element(By.CSS_SELECTOR, 'div.cookies')
        assert eleCookiesDiv.value_of_css_property("height") == "155.2px", "Test 2 fail"
    except NoSuchElementException:
        print("Element not found for test_height")
    except AssertionError as e:
        print(e)

def teardown():
    driver.quit()

if __name__ == "__main__":
    setup()
    try:
        test_color()
        test_height()
    finally:
        teardown()
