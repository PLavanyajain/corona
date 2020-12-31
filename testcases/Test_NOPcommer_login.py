import pytest
from selenium import webdriver
from PageObjectModelss.LoginpagNOp import LoginPageNOP
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
import time

class Test_001_LoginNop:
    baseUrl=Readconfig.getApplicationURL()
    userID=Readconfig.getUserName()
    password=Readconfig.getPassword()

    logger=LogGen.loggen()
    def test_Login__NOp_001(self,setup):
        self.logger.info("******************Verifiying Loginpage*******************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.lpn=LoginPageNOP(self.driver)
        self.lpn.setMailID(self.userID)
        self.lpn.setMailPassword(self.password)
        self.lpn.Click_login()
        time.sleep(50)
        #self.driver.quit()
        self.logger.info("Loginpage is completely verified")








