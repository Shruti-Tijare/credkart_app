import allure
import pytest

from Utilities import Excel_Utils
from Utilities.Logger import log_generator_class
from Utilities.Read_Config import ReadConfigClass
from pageObjects.Login_Page import Login_Page_Class # user define class import

@pytest.mark.usefixtures("browser_setup")
class Test001:

    driver = None

    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login =  ReadConfigClass.get_login_url()
    homepage = ReadConfigClass.get_home_url()
    registration = ReadConfigClass.get_registration_url()

    log = log_generator_class.loggen_method()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("verify Application url")
    @allure.description("This test case is to validate credkart title functionality")
    @allure.link(homepage)
    @allure.epic("Epic 1")
    @allure.story("Story 1")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    #@pytest.mark.dependency()
    def test_Credkart_URL_001(self):
        self.log.info("This is info")
        self.log.warning("This is warning")
        self.log.error("This is error")
        self.log.critical("This is critical")
        self.log.info("Testcase test_Credkart_URL_001 is started")
        self.driver.get(self.homepage)
        self.log.info(f"Opening Browser and landing on {self.homepage}")
        self.log.info(f"Checking page title")
        if self.driver.title == "CredKart":
            self.log.info(f"Page title is correct and landed on correct url -->{self.driver.title}")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\CredKart_Home_Page_pass.png")
            self.log.info("Testcase test_Credkart_URL_001 is pass")
        else:
            self.log.info(f"Page title is incorrect and landed on url -->{self.driver.title}")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\CredKart_Home_Page_fail.png")
            self.log.info("Testcase test_Credkart_URL_001 is Fail")
            assert False
            self.log.info("Testcase test_Credkart_URL_001 is completed")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("verify login")
    @allure.description("This test case is to validate login succsesfull or not ")
    @allure.link(login)
    @allure.epic("Epic 1")
    @allure.story("Story 2")
    @pytest.mark.smoke
    @pytest.mark.regression
    #@pytest.mark.dependency(depends=["test_Credkart_URL_001"])
    def test_Credkart_login_excel_002(self):
        excel_path = ".\\TestData\\Test_Data.xlsx"
        sheet_name = "Login_Data"

        self.lp = Login_Page_Class(self.driver)
        self.rows = Excel_Utils.get_row_count(excel_path,sheet_name)
        print(f"number of rows in excel sheet : {self.rows}")
#run up to this and output is :   number of rows in "excel"sheet : 5

        result_list=[]
        for i in range(2,self.rows+1):
            self.driver.get(self.login)
            self.email = Excel_Utils.read_data(excel_path,sheet_name,i,2)
            self.password = Excel_Utils.read_data(excel_path,sheet_name,i,3)
            self.expected_result = Excel_Utils.read_data(excel_path,sheet_name,i,4)


            #enter email
            self.lp.enter_email(self.email)

            #enter password
            self.lp.enter_password(self.password)


            #click on login button
            self.lp.click_submit()

            #verify status and move forward

            if self.lp.verify_menu() == "Pass":

                self.lp.click_menu()
                self.lp.click_logout()
                self.driver.save_screenshot(f".\\Screenshots\\user_login_pass.png")
                allure.attach.file(".\\Screenshots\\user_login_pass.png", name="User_Login_Pass",
                                   attachment_type=allure.attachment_type.PNG)
                actual_result = "login_pass"

            else:
                self.driver.save_screenshot(f".\\Screenshots\\user_login_fail.png")
                allure.attach.file(".\\Screenshots\\user_login_fail.png", name="User_Login_Fail" , attachment_type=allure.attachment_type.PNG)
                actual_result = "login_fail"

            #writing data into "excel" of actual result
            Excel_Utils.write_data(excel_path,sheet_name,i,5,actual_result)

            #now we verify testcase result
            if self.expected_result == actual_result :
                test_case_status = "Pass"

            else:
                test_case_status = "Fail"
            result_list.append(test_case_status)

            #write data of testcase status

            Excel_Utils.write_data(excel_path,sheet_name,i,6,test_case_status)

            #verify kr "rahe" ki "konsi" test case fail ho rhi against chl rhi meet nhi ho actual vs expected
            #kyuki ye sare data milker ek hi test case manta so puri test case fail hongi

        if "Fail" not in result_list:
            print("All test casess are passed ")
            assert True

        else:
            print(f"some test cases are failed")
            assert False


