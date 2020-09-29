# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/27 10:33
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  basepage
#   function：将常用的操作封装

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from log.dolog import DoLog
import random
import os
import time
from common import contants
from config.read_conf import GetConf


class BasePage:
    def __init__(self, url):
        self.driver = webdriver.Chrome(service_args=["--verbose"])
        self.driver.get(url)
        # 设置全局等待
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.logger = DoLog()

    def login(self, name, pwd):
        username_locator = self.driver.find_element_by_xpath(GetConf.locator("登录", "用户名"))
        pwd_locator = self.driver.find_element_by_xpath(GetConf.locator("登录", "密码"))
        login_button_locator = self.driver.find_element_by_xpath(GetConf.locator("登录", "登录"))

        username_locator.send_keys(name)
        pwd_locator.send_keys(pwd)
        login_button_locator.click()

    # 等待元素可见
    def wait_eleVisible(self, locator, by=By.XPATH, wait_time=40):
        try:
            # 找到这个元素后，一定要返回，不然后面测试用例里接收不到元素的值
            # 方法还是用可点击和可见 比较好
            return WebDriverWait(self.driver, wait_time, 1).until(expected_conditions.visibility_of_element_located((by, locator)))
        except Exception as e:
            self.save_screenshot()
            self.logger.error(e)
            raise e

    # 等待元素可点击
    def wait_eleclickable(self, locator, by=By.XPATH, wait_time=40):
        try:
            return WebDriverWait(self.driver, wait_time, 1).until(expected_conditions.element_to_be_clickable((by, locator)))
        except Exception as e:
            self.save_screenshot()
            self.logger.error(e)
            raise e

    # 判断某个元素是否存在页面上
    def ele_exist_or_not(self, locator):
        try:
            self.driver.find_element_by_xpath(locator)
            return True
        except:
            return False

    # 截图函数
    def save_screenshot(self):
        r = ""
        for i in range(3):
            r += str(random.randint(1000, 10000))

        file_path = os.path.join(contants.screenshot_dir, "{}.png".format(time.strftime("%Y%m%d_%H%M%S_{}".format(r))))
        self.driver.save_screenshot(file_path)
        self.logger.info("已截取当前页面，文件路径：{}".format(file_path))

    def clear_username(self):
        return self.wait_eleVisible(GetConf.locator("登录", "用户名")).clear()

    def clear_pwd(self):
        return self.wait_eleVisible(GetConf.locator("登录", "密码")).clear()

    def quit_sys(self):
        self.wait_eleclickable(GetConf.locator("登录", "元素_右上角下拉箭头")).click()
        self.wait_eleclickable(GetConf.locator("登录", "元素_退出")).click()


if __name__ == "__main__":
    a = BasePage('https://governor.enesource.com')

