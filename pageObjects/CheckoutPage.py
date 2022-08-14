from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage: # I will call all the objects here

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div/h4/a")
    cardFooterButton = (By.CSS_SELECTOR, ".card-footer button")
    checkOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle) # With the star is taken as a tuple

    def getcardFooterButton(self):
        return self.driver.find_elements(*CheckoutPage.cardFooterButton)

    def getcheckOutButton(self): # Another integration point for another page, I am creating the object
        self.driver.find_element(*CheckoutPage.checkOutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

