#Link--http://demo.guru99.com/V4/
class LoginPageNOP:
    Email_name ="Email"
    password_id ="Password"
    Login_click_by_xpath ="//input[@class='button-1 login-button']"



    def __init__(self,driver):
        self.driver=driver

    def setMailID(self,mailid):
        self.driver.find_element_by_id(self.Email_name).clear()
        self.driver.find_element_by_id(self.Email_name).send_keys(mailid)

    def setMailPassword(self,passwords):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(passwords)

    def Click_login(self):
        self.driver.find_element_by_xpath(self.Login_click_by_xpath).click()





