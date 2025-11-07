from selenium.webdriver.common.by import By

class AuthLocators:
    email = (By.XPATH, "//input[@id = 'email']")
    password = (By.XPATH, "//input[@id = 'pass']")
    enter_bttn = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-success')]")

class AllPetsLocators:
    images = (By.XPATH, "//div/div[@class='card']/div/img")
    names = (By.XPATH, "//div/div[@class='card']/div/h5")
    descriptions = (By.XPATH, "//div/div[@class='card']/div/p")