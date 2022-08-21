import pytest
import time
# How to invoke browsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#@pytest.mark.usefixtures("setup") # Here I am calling the fixture
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger() # Invoke the corresponding logger
        homePage = HomePage(self.driver) # We create an object from Homepage type
        checkOutPage = homePage.shopItems()
        log.info("Getting all the card titles--Mariano changes new branch (NEW)")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getcardFooterButton()[i].click()
        confirmPage = checkOutPage.getcheckOutButton()
        confirmPage.getconfirmButton().click()
        log.info("Confirmation was done, we going to jump to next page")
        confirmPage.gettxtCountry().send_keys("ind")
        self.verifyLinkPresene("India") # Pass the parameter and could be invoked due is a method from base clas
        confirmPage.getvalueIndia().click()
        confirmPage.getcheckTerms().click()
        confirmPage.getbtnConfirm().click()
        SucText = confirmPage.getSuccText().text
        log.info("Text received from application is "+SucText)
        time.sleep(5)
        assert "Success" in SucText


        # In reference to errors we can use info, debug, warning, error, etc. (levels)






