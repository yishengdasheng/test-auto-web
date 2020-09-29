# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/9/18 10:51
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  managepage
#   function：权限管理页面的操作封装
from pages.basepage import BasePage
from config.read_conf import GetConf
from selenium.webdriver.common.action_chains import ActionChains


class ManagePage(BasePage):
    def submit_user(self, user, name, phone=None, email=None):
        self.wait_eleVisible(GetConf.locator("权限管理", "元素_账号输入")).send_keys(user)
        self.wait_eleVisible(GetConf.locator("权限管理", "元素_姓名输入")).send_keys(name)
        if phone:
            self.wait_eleVisible(GetConf.locator("权限管理", "元素_手机号输入")).send_keys(phone)
        if email:
            self.wait_eleVisible(GetConf.locator("权限管理", "元素_邮箱输入")).send_keys(email)
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_创建账号_确认键")).click()

    def submit_group(self):
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_新建组织")).click()
        self.wait_eleVisible(GetConf.locator("权限管理", "元素_组织名称输入")).send_keys(GetConf.datas("CREATEUSER", "group_name"))
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_选择左边所有选项")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_移动选项到右边")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_创建组织_确认键")).click()

    def submit_role(self):
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_创建角色")).click()
        self.wait_eleVisible(GetConf.locator("权限管理", "元素_角色名称输入")).send_keys(GetConf.datas("CREATEUSER", "role_name"))
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_下一步")).click()

    def add_group_user(self):
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_成员管理")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_已创建的账号")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_移动选项到右边")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_成员管理_确认键")).click()

    def add_role_user(self):
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_选择创建的账号")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_批量分配角色")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_创建的角色")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_移动选项到右边")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_批量分配角色_确认键")).click()

    def del_user(self):
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_删除账号")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_删除账号_确认键")).click()

    def del_group(self):
        # 鼠标hover上去，出现操作键，再点击，出现删除按钮
        last_group = self.wait_eleVisible(GetConf.locator("权限管理", "元素_最后一个组织"))
        ActionChains(self.driver).move_to_element(last_group).perform()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_threepoints操作键")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_删除按钮")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_删除组织_确认键")).click()

    def del_role(self):
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_删除角色")).click()
        self.wait_eleclickable(GetConf.locator("权限管理", "元素_删除角色_确认键")).click()







