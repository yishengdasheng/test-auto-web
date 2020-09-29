# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/9/15 12:02
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  test_login
#   function：登录页面的测试用例,登录这个有点难搞，使用setupclass会出错
import unittest
from config.read_conf import GetConf
from pages.basepage import BasePage
import ddt


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.base_page = BasePage('https://governor.enesource.com')
        self.base_page.logger.info("================================")

    def tearDown(self):
        self.base_page.driver.quit()

    @ddt.data(*eval(GetConf.datas("LOGIN", "user_isnull")))
    def test_login1_user_or_pwd_isnull(self, userdata):
        self.base_page.logger.info("------------------------------------------------------------------")
        self.base_page.clear_username()
        self.base_page.clear_pwd()
        self.base_page.login(userdata["username"], userdata["password"])
        try:
            error_locator = self.base_page.wait_eleVisible(GetConf.locator("登录", "元素_不得为空提示"), wait_time=10)
            self.assertTrue(userdata["expected"] == error_locator.text)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_login_failed 用例断言失败")
            self.base_page.save_screenshot()
            raise e

    @ddt.data(*eval(GetConf.datas("LOGIN", "user_wrong")))
    def test_login2_user_or_pwd_wrong(self, userdata):
        self.base_page.logger.info("------------------------------------------------------------------")
        self.base_page.clear_username()
        self.base_page.clear_pwd()
        self.base_page.login(userdata["username"], userdata["password"])
        try:
            content_locator = self.base_page.wait_eleVisible(GetConf.locator("登录", "元素_密码错误提示"), wait_time=10)
            self.assertTrue(userdata["expected"] in content_locator.text)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_login_failed 用例断言失败")
            self.base_page.save_screenshot()
            raise e

    def test_login3_ok(self):
        self.base_page.logger.info("------------------------------------------------------------------")
        user = eval(GetConf.datas("LOGIN", "user_ok"))
        self.base_page.clear_username()
        self.base_page.clear_pwd()
        self.base_page.login(user["username"], user["password"])
        logo_locator = GetConf.locator("能源节度使", "logo")
        self.base_page.wait_eleVisible(logo_locator, wait_time=10)
        try:
            self.assertTrue('能源节度使' in logo_locator)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_login_ok 用例断言失败")
            self.base_page.save_screenshot()
            raise e

