from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_category_navigation(driver):
    driver.get("http://books.toscrape.com/")
    driver.find_element(By.LINK_TEXT, "Fiction").click()
    assert driver.find_element(By.TAG_NAME, "h1").text == "Fiction"