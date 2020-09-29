# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/9/17 13:43
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  test_operationMonitor
#   function：告警页面的测试用例
# 当前告警和历史告警页面都是主查询，其他内容没有太多测试意义，只要保证告警功能正常即可，所以只要告警在正常产生，就判断页面功能正常
import unittest
from config.read_conf import GetConf
from pages.basepage import BasePage


class TestOperationMonitor(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base_page = BasePage('https://governor.enesource.com')
        cls.base_page.logger.info("================================")
        user = eval(GetConf.datas("LOGIN", "user_ok"))
        cls.base_page.login(user["username"], user["password"])

    def test_alarm(self):
        self.base_page.wait_eleVisible((GetConf.locator("设备告警", "一级菜单"))).click()
        self.base_page.wait_eleVisible((GetConf.locator("设备告警", "二级菜单_当前告警"))).click()
        alarm_num = self.base_page.wait_eleVisible((GetConf.locator("设备告警", "元素_当前未结数量")))
        try:
            self.assertFalse(alarm_num.text == 0 or alarm_num.text is None)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_alarm 用例断言失败")
            self.base_page.save_screenshot()
            raise e


