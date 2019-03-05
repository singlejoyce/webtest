import time
import unittest
from selenium import webdriver


class L5ddlLogin(unittest.TestCase):
    def setUp(self):
        # 每个测试用例执行之前做操作
        self.driver = webdriver.Chrome(executable_path="D:\\chromedriver2.41.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url = "http://passport.ddianle.com/login.html"
        self.driver.get(self.base_url)

    def test_l5ddl_login_normal(self):
        username = 'testy01'
        password = 'a'

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("pwd").clear()
        self.driver.find_element_by_id("pwd").send_keys(password)
        time.sleep(2)
        # Selenium在定位的class含有空格的复合类的解决办法
        # 方法一：取单个class属性
        # self.driver.find_element_by_class_name("ddl_btn_pc").click()
        # 方法二：直接包含空格的CSS属性定位大法
        self.driver.find_element_by_css_selector("[class='ddl_btn_pc btn']").click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.assertEqual('账号管理', self.driver.title)

    def l5ddl_login_error(self, username, password):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("pwd").clear()
        self.driver.find_element_by_id("pwd").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_css_selector("[class='ddl_btn_pc btn']").click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        text = self.driver.find_element_by_xpath("//div[@class='errorsInput_pc']/span[@class='ng-binding']").text
        return text

    def test_l5ddl_login_error1(self):
        username = 'testy01111111111111111111'
        password = 'a'

        text = self.l5ddl_login_error(username, password)
        self.assertEqual(text, "用户名不存在.")

    def test_l5ddl_login_error2(self):
        username = ''
        password = ''

        text = self.l5ddl_login_error(username, password)
        self.assertEqual(text, "请输入正确的用户名")

    def test_l5ddl_login_error3(self):
        username = 'testy01'
        password = 'aaaaaaaa'

        text = self.l5ddl_login_error(username, password)
        self.assertEqual(text, "用户名或密码错误.")

    def test_click_register(self):
        self.driver.find_element_by_xpath("//div[@class='forget']/span[contains(text(),'注册新账户')]").click()
        time.sleep(2)
        self.assertEqual('通行证注册', self.driver.title)

    def test_click_register2(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'注册')]").click()
        time.sleep(2)
        self.assertEqual('通行证注册', self.driver.title)

    def test_click_forget(self):
        self.driver.find_element_by_xpath("//div[@class='forget']/span[contains(text(),'忘记密码')]").click()
        time.sleep(2)
        self.assertEqual('找回方式', self.driver.title)

    def tearDown(self):
        # 每个测试用例执行之后做操作
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

