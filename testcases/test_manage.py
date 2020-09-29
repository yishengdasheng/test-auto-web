# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/9/18 9:41
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  test_manage
#   function：权限管理的测试用例
import unittest
from config.read_conf import GetConf
from pages.managepage import ManagePage
import time


class TestManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manage_page = ManagePage('https://governor.enesource.com')
        cls.manage_page.logger.info("================================")
        user = eval(GetConf.datas("LOGIN", "user_ok"))
        cls.manage_page.login(user["username"], user["password"])

    def test_1_create_user(self):
        data = eval(GetConf.datas("CREATEUSER", "user"))
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_账号管理")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "元素_新建账号")).click()
        self.manage_page.submit_user(user=data["username"], name=data["name"])
        try:
            seccess_locator = self.manage_page.wait_eleVisible(GetConf.locator("权限管理", "元素_操作成功提示"))
            self.assertTrue(data["expected"] == seccess_locator.text)
            self.manage_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.manage_page.logger.error("test_1_create_user 用例断言失败")
            self.manage_page.save_screenshot()
            raise e

    def test_2_create_group(self):
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_组织管理")).click()
        self.manage_page.submit_group()
        try:
            seccess_locator = self.manage_page.wait_eleVisible(GetConf.locator("权限管理", "元素_操作成功提示"))
            self.assertTrue("操作成功！" == seccess_locator.text)
            self.manage_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.manage_page.logger.error("test_2_create_group 用例断言失败")
            self.manage_page.save_screenshot()
            raise e

    def test_3_create_role(self):
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_角色管理")).click()
        self.manage_page.submit_role()
        try:
            seccess_locator = self.manage_page.wait_eleVisible(GetConf.locator("权限管理", "元素_操作成功提示"), 5)
            self.assertTrue("新增角色成功" == seccess_locator.text)
            self.manage_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.manage_page.logger.error("test_3_create_role 用例断言失败")
            self.manage_page.save_screenshot()
            raise e

    def test_4_group_to_user(self):
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_组织管理")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "元素_最后一个组织")).click()
        self.manage_page.add_group_user()
        try:
            seccess_locator = self.manage_page.wait_eleVisible(GetConf.locator("权限管理", "元素_操作成功提示"))
            self.assertTrue("操作成功" == seccess_locator.text)
            self.manage_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.manage_page.logger.error("test_4_group_to_user 用例断言失败")
            self.manage_page.save_screenshot()
            raise e

    def test_5_role_to_user(self):
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_账号管理")).click()
        self.manage_page.add_role_user()
        try:
            seccess_locator = self.manage_page.wait_eleVisible(GetConf.locator("权限管理", "元素_操作成功提示"))
            self.assertTrue("操作成功！" == seccess_locator.text)
            self.manage_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.manage_page.logger.error("test_5_role_to_user 用例断言失败")
            self.manage_page.save_screenshot()
            raise e

    def test_6_delete_role(self):
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_角色管理")).click()
        self.manage_page.del_role()
        time.sleep(1)
        try:
            role = self.manage_page.ele_exist_or_not(GetConf.locator("权限管理", "元素_被删除的角色"))
            self.assertFalse(role)
            self.manage_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.manage_page.logger.error("test_6_delete_role 用例断言失败")
            self.manage_page.save_screenshot()
            raise e

    def test_7_delete_group(self):
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_组织管理")).click()
        self.manage_page.del_group()
        try:
            seccess_locator = self.manage_page.wait_eleVisible(GetConf.locator("权限管理", "元素_操作成功提示"))
            self.assertTrue("操作成功！" == seccess_locator.text)
            self.manage_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.manage_page.logger.error("test_7_delete_group 用例断言失败")
            self.manage_page.save_screenshot()
            raise e

    def test_8_delete_user(self):
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
        self.manage_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_账号管理")).click()
        self.manage_page.del_user()
        try:
            seccess_locator = self.manage_page.wait_eleVisible(GetConf.locator("权限管理", "元素_操作成功提示"))
            self.assertTrue("操作成功！" == seccess_locator.text)
            self.manage_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.manage_page.logger.error("test_8_delete_user 用例断言失败")
            self.manage_page.save_screenshot()
            raise e




