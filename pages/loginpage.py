# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/9/15 15:06
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  loginpage
#   function：登录页面的操作封装, 因为登录操作其他页面也会用到，所以放到basepage里了
from pages.basepage import BasePage
from config.read_conf import GetConf


class LoginPage(BasePage):
    # 子类集成父类的init不需要使用超继承，也不需要再次定义init的参数，直接用就行了
    username = GetConf.locator("登录", "用户名")
    pwd = GetConf.locator("登录", "密码")

    # 清除输入框里的内容
    def clear_username(self):
        return self.wait_eleVisible(self.username).clear()

    def clear_pwd(self):
        return self.wait_eleVisible(self.pwd).clear()


if __name__ == "__main__":
    pass