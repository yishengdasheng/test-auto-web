# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/27 10:33
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  basepage
#   function：将常用的操作封装

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from log.dolog import DoLog
import random
import os
import time
from common import contants


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maxmize_window()
        self.logger = DoLog()

    # 等待元素可见
    def wait_eleVisible(self, locator, by=By.XPATH, wait_time=40):
        try:
            WebDriverWait(self.driver, wait_time, 1).until(expected_conditions.presence_of_element_located((by, locator)))
        except InvalidSelectorException as e:
            self.logger.error("元素定位表达式不正确，请修正：{}".format(locator))
            self.save_screenshot()
            raise e
        except NoSuchElementException as e:
            self.logger.error("没有找到该元素")
            raise e
        except TimeoutError as e:
            self.logger.error("等待页面超时")
            raise e

    # 截图函数
    def save_screenshot(self):
        r = ""
        for i in range(3):
            r += str(random.randint(1000, 10000))

        file_path = os.path.join(contants.screenshot_dir, "{}.png".format(time.strftime("%Y%m%d_%H%M%S_{}".format(r))))
        self.driver.save_screenshot(file_path)
        self.logger.info("已截取当前页面，文件路径：{}".format(file_path))
