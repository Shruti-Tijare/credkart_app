from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):
    text_name_id = "name"
    text_confirm_password_xpath = "//input[@id='password-confirm']"

    def __init__(self,driver):
        self.driver = driver

    def enter_name(self,name):
        self.driver.find_element(By.ID,self.text_name_id).send_keys(name)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(By.XPATH,self.text_confirm_password_xpath).send_keys(confirm_password)
