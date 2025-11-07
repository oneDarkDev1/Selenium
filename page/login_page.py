from .base_page import BasePage
from .locators import AuthLocators

import  time,os

class AuthPage(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = os.getenv("LOGIN_URL") or "http://petfriends.skillfactory.ru/login"
       driver.get(url)

       self.email = driver.find_element(*AuthLocators.email)
       self.password = driver.find_element(*AuthLocators.password)
       self.btn = driver.find_element(*AuthLocators.enter_bttn)


   def enter_email(self, value):
       self.email.send_keys(value)

   def enter_pass(self, value):
       self.password.send_keys(value)

   def btn_click(self):
       self.btn.click()
