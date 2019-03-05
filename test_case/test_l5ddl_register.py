import time
import unittest
from selenium import webdriver


class L5ddlRegister(unittest.TestCase):
    def setUp(self):
        # 每个测试用例执行之前做操作
        self.driver = webdriver.Chrome(executable_path="D:\\chromedriver2.41.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # self.base_url = "http://passport.ddianle.com/"
        self.base_url = "http://passport.ddianle.com/register.html"
        self.driver.get(self.base_url)

    def register_by_self(self, username, pwd, truename, idcard, phonenum):
        self.driver.find_element_by_xpath("//span[contains(text(),'自定义账号注册')]").click()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("pwd1").clear()
        self.driver.find_element_by_id("pwd1").send_keys(pwd)
        self.driver.find_element_by_id("confirmpwd1").clear()
        self.driver.find_element_by_id("confirmpwd1").send_keys(pwd)
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='regByself_pc']/table[2]/tbody/tr[1]/td[2]/input").clear()
        self.driver.find_element_by_xpath("//div[@class='regByself_pc']/table[2]/tbody/tr[1]/td[2]/input").send_keys(truename)
        self.driver.find_element_by_xpath("//div[@class='regByself_pc']/table[2]/tbody/tr[3]/td[2]/input").clear()
        self.driver.find_element_by_xpath("//div[@class='regByself_pc']/table[2]/tbody/tr[3]/td[2]/input").send_keys(idcard)
        self.driver.find_element_by_xpath("//div[@class='regByself_pc']/table[2]/tbody/tr[5]/td[2]/input[1]").clear()
        self.driver.find_element_by_xpath("//div[@class='regByself_pc']/table[2]/tbody/tr[5]/td[2]/input[1]").send_keys(phonenum)

        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='regByself_pc']/table[2]/tbody/tr[8]/td[2]/button").click()
        time.sleep(2)
        text = self.driver.find_element_by_xpath("//div[@class='regByself_pc']/table[1]/tbody/tr[1]/td[2]/div/span").text
        return text

    def test_register_by_self(self):
        username = "testaccount01"
        pwd = "123456"
        truename = "jy"
        idcard = "110101199003073693"
        phonenum = "13585869812"
        text = self.register_by_self(username, pwd, truename, idcard, phonenum)
        self.assertEqual(text, "请填写图片验证码")

    def test_register_by_self1(self):
        username = "testaccount01"
        pwd = "123456"
        truename = "jy"
        idcard = "123456"
        phonenum = "13585869812"
        text = self.register_by_self(username, pwd, truename, idcard, phonenum)
        self.assertEqual(text, "请输入正确的身份证号")

    def test_register_by_self2(self):
        username = ""
        pwd = ""
        truename = ""
        idcard = ""
        phonenum = ""
        text = self.register_by_self(username, pwd, truename, idcard, phonenum)
        self.assertEqual(text, "请输入正确的用户名")

    def test_register_by_self3(self):
        username = "testaccount01"
        pwd = "123456"
        truename = "jy"
        idcard = "110101199003073693"
        phonenum = ""
        text = self.register_by_self(username, pwd, truename, idcard, phonenum)
        self.assertEqual(text, "联系方式和邮箱必须要填写一个")

    def tearDown(self):
        # 每个测试用例执行之后做操作
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

