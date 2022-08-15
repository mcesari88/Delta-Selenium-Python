import logging

import pytest
import time
# How to invoke browsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#@pytest.mark.usefixtures("setup") # Here I am calling the fixture
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from testdatapage.Homepagedata import Homepagedata
from utilities.BaseClass import BaseClass

class TestHomepage(BaseClass):

    def test_formsubmission(self, getData): # We need to include the method (Fixture as parameter) / It will run two times, one per each datased / Need this parameter to run
        homepage = HomePage(self.driver)
        logging.info("First name is :"+getData["firstname"])
        homepage.getname().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        #homepage.getemail().send_keys("mmc@gmail.com")
        homepage.getpassword().send_keys("carcholo")
        homepage.getcheckbox().click()
        self.selectoptionByText(homepage.getgender(), getData["gender"])
        homepage.getbtnsuccess().click()
        alert = homepage.getalertmessage().text

        assert ("Success" in alert)
        self.driver.refresh() # Refresh to refresh the page after validate that it was right... Need to input new values
        time.sleep(5)

    @pytest.fixture(params= Homepagedata.getTestData("Testcase2")) # Each tuple will be trated as a test case. Is up to you
    def getData(self, request):
        return request.param





