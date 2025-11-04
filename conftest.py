# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # start full screen
    driver = webdriver.Chrome(service=service, options=options)

    yield driver  # provide the fixture value to tests

    # Teardown
    driver.quit()
