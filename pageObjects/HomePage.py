from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage: # I will call all the objects here
    def __init__(self, driver):
        self.driver = driver


    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    checkbox = (By.CSS_SELECTOR, "input[id='exampleCheck1']")
    gender = (By.ID, "exampleFormControlSelect1" )
    rad = (By.CSS_SELECTOR, "input[value='option2']")
    datebirth = (By.CSS_SELECTOR, "input[name='bday']")
    alertmes = (By.CSS_SELECTOR, "[class*='alert-success']")
    submit = (By.CSS_SELECTOR, ".btn-success")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() # With the star is taken as a tuple / Click direcly due it is an integratio point
        checkOutPage = CheckoutPage(self.driver) # Create the object of the new page
        return checkOutPage # return the object of the new page

    ''' Definition of Methods for HOMEPAGE TEST CASES'''

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getrad(self):
        return self.driver.find_element(*HomePage.rad)

    def getdatebirth(self):
        return self.driver.find_element(*HomePage.datebirth)

    def getalertmessage(self):
        return self.driver.find_element(*HomePage.alertmes)

    def getbtnsuccess(self):
        return self.driver.find_element(*HomePage.submit)




