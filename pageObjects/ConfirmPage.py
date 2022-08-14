from selenium.webdriver.common.by import By


class ConfirmPage: # I will call all the objects here
    def __init__(self, driver):
        self.driver = driver

#                 SucText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

    checkoutConfirm = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    textcountry = (By.ID, "country")
    valueIndia = (By.LINK_TEXT, "India")
    checkTerms = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    btnConfirm = (By.XPATH, "//input[@type='submit']")
    lblSuccText = (By.CLASS_NAME, "alert-success")

    def getconfirmButton(self):
        return self.driver.find_element(*ConfirmPage.checkoutConfirm) # With the star is taken as a tuple

    def gettxtCountry(self):
        return self.driver.find_element(*ConfirmPage.textcountry)

    def getvalueIndia(self):
        return self.driver.find_element(*ConfirmPage.valueIndia)

    def getcheckTerms(self):
        return self.driver.find_element(*ConfirmPage.checkTerms)

    def getbtnConfirm(self):
        return self.driver.find_element(*ConfirmPage.btnConfirm)

    def getSuccText(self):
        return self.driver.find_element(*ConfirmPage.lblSuccText)