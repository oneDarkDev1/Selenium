import pytest
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def login(selenium):
    selenium.get("https://petfriends.skillfactory.ru/login")

    email_f = selenium.find_element(By.XPATH, "//input[@id = 'email']")
    email_f.send_keys("pineappleplay906@gmail.com")
    pass_f = selenium.find_element(By.XPATH, "//input[@id = 'pass']")
    pass_f.send_keys("12345678")
    submit_btn = selenium.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-success')]")
    submit_btn.click()

    time.sleep(5)
    return selenium

def test_cards_validity(login):
    driver = login
    images = driver.find_elements(By.XPATH, "//div/div[@class='card']/div/img")
    names = driver.find_elements(By.XPATH, "//div/div[@class='card']/div/h5")
    descriptions = driver.find_elements(By.XPATH, "//div/div[@class='card']/div/p")

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', "no pic"
        assert names[i].text != ''
        assert descriptions[i].text != ''
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0