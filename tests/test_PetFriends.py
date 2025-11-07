import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from page.login_page import AuthPage
from page.home_page import AllPetsPage
from page.locators import *


@pytest.fixture()
def login(selenium):
    login = AuthPage(selenium)

    login.enter_email("pineappleplay906@gmail.com")
    login.enter_pass("12345678")
    login.btn_click()

    return selenium

    selenium.quit()


def click_nav_toggler(driver):
    for attempt in range(3):
        try:
            WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'navbar-toggler')]"))
            ).click()
            break
        except TimeoutException:
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

def test_cards_validity(login):
    driver = login
    all_pets_page = AllPetsPage(driver)

    all_pets_page.wait_for_load(AllPetsLocators.images)
    all_pets_page.wait_for_load(AllPetsLocators.names)
    all_pets_page.wait_for_load(AllPetsLocators.descriptions)

    images = all_pets_page.images
    names = all_pets_page.names
    descriptions = all_pets_page.descriptions

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', f"no pic on card {i}"
        assert names[i].text != '', f"name is empty on card {i}"
        assert descriptions[i].text != '', f"no details on card {i}"
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

def test_my_pets_table(login):
    driver = login
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    click_nav_toggler(driver)

    my_pets_bttn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/my_pets']"))
    )
    my_pets_bttn.click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'col-sm-4')]"))
    )
    info = driver.find_element(By.XPATH, "//div[contains(@class, 'col-sm-4')]").text
    total = int(info.split('\n')[1].split(': ')[1])

    wait.until(
        EC.visibility_of_element_located((By.ID, "all_my_pets"))
    )
    images = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-hover')]/tbody/tr/th/img")
    names = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-hover')]/tbody/tr/td[1]")
    pet_types = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-hover')]/tbody/tr/td[2]")
    ages = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-hover')]/tbody/tr/td[3]")


    foto_count = 0
    previous_names = set()
    pets = []

    assert total == len(names)
    for i in range(len(names)):
        if images[i].get_attribute("src") != '':
            foto_count += 1
        assert names[i].text != '' and pet_types[i].text != '' and ages[i].text != ''
        assert names[i] not in previous_names
        previous_names.add(names[i].text)
        pet = {"name": names[i].text, "type": pet_types[i].text, "age": ages[i].text}
        assert pet not in pets
        pets.append(pet)
    assert foto_count >= len(names)/2

