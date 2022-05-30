import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from eveningclass545.POM.locators.locations import locators2


class pages2:

    def loginpage(self):
        lc = locators2()
        path = 'C:\\Selenium\\chromedriver.exe'
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        driver = self.driver
        driver.get(lc.url)
        driver.find_element(By.ID, lc.login).click()

        driver.implicitly_wait(10)

        loginfield = driver.find_element(By.XPATH, lc.username)
        loginfield.send_keys('testmorning')
        driver.find_element(By.XPATH, lc.password).send_keys('test123')
        driver.find_element(By.XPATH, lc.button).click()
        time.sleep(5)

