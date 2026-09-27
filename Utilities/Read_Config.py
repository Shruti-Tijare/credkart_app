import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfigClass:
    @staticmethod
    def get_data_for_email():
        email = config.get("login_data", "email")
        return email

    @staticmethod
    def get_data_for_password(): #not write self bcz we call method by class
        password = config.get("login_data","password")
        return password

    @staticmethod
    def get_home_url():
        homepage = config.get("app_urls" ,"home_page_url")
        return homepage

    @staticmethod
    def get_login_url():
        loginpage = config.get("app_urls", "login_url")
        return loginpage

    @staticmethod
    def get_registration_url():
        registration_page = config.get("app_urls" , "registration_url")
        return registration_page