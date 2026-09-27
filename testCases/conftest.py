import pytest
from selenium import webdriver



# Python -v -s --browser firefox


def pytest_addoption(parser):
    parser.addoption("--browser")
# Here we are going to add - - browser is a command line argument which is user define or custom argument you can say.

# --browser chrome
# --browser firefox
# --browser edge

@pytest.fixture(scope = 'class')   #new
def browser_setup(request):
    browser = request.config.getoption("--browser") # we are going to share --browser value at the time of execution(pytest command)
    if browser == "chrome":
        print("Launching Chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Launching Edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("Launching chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver #new
    yield driver
    driver.quit()


# Use Name --> CredenceTest_5005@credence.in
# Password --> Password@123

@pytest.fixture(params=[
    ('CredenceTest_5005@credence.in', 'Password@123', 'login_pass'),
    ('CredenceTest_50051@credence.in', 'Password@123', 'login_fail'),
    ('CredenceTest_5005@credence.in', 'Password@1232', 'login_fail'),
    ('CredenceTest_50051@credence.in', 'Password@1232', 'login_fail')
])
def credkart_login_data(request):
    return request.param

#just to enhance "html" "report
def pytest_metadata(metadata):
    metadata["Project Name"] = "Credkart Automation Testing"
    metadata["Module Name"]  = "Login"
    metadata["Tester Name"]  = "Shruti Tijare"

    #to remove metadata from report
    del metadata["Platform"]