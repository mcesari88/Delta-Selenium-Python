from selenium import webdriver
import pytest
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager # Chrome
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)  # Webdriver of Chrome
#driver = None

@pytest.fixture(scope="class") # Defining in scope = Class will be executed once per each test cases
def setup(request):
   # global driver # It will use the global object and not create a new variable
   global driver
   driver.implicitly_wait(5)
   driver.get("http://www.rahulshettyacademy.com/angularpractice/")
   driver.maximize_window()
   request.cls.driver = driver # We are assigning the local driver of the fixture to the local driver...
   yield
   driver.quit() # USE THIS TO AVOID SESSION ERROR

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

# Yield and return cannot be used in a joint way
# We have an standard in practice for these scenarios



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name) #The driver will use the global variable

