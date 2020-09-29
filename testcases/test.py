# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/7 11:03
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  test
#   function：
from selenium import webdriver
import time
from config.read_conf import GetConf
from pages.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common import exceptions as e
import unittest
from pages.loginpage import LoginPage
from pages.managepage import ManagePage


# driver = webdriver.Chrome()
# driver.get("https://governor.enesource.com")
# driver.maximize_window()
driver = webdriver.Chrome()
driver.get("https://governor.enesource.com")
base_page = BasePage(driver)
# driver.maximize_window()
username_locator = driver.find_element_by_xpath('//input[@placeholder="请输入用户名/手机号码/邮箱"]')
pwd_locator = driver.find_element_by_xpath('//input[@placeholder="输入密码"]')
login_button_locator = driver.find_element_by_xpath('//button[@class="el-button login-in cursor el-button--primary"]')

username_locator.send_keys("yoyo")
pwd_locator.send_keys("123456")
login_button_locator.click()
time.sleep(3)
# error_locator = driver.find_element_by_xpath('//div[@class="el-form-item__error"]')
# print(error_locator.text)

# shebeigaojing_h1 = driver.find_element_by_xpath(GetConf.locator("设备告警", "一级菜单"))
# shebeigaojing_h1.click()
#
# dangqiangaojing_h2 = driver.find_element_by_xpath(GetConf.locator("设备告警", "二级菜单_当前告警"))
# lishigaojing_h2 = driver.find_element_by_xpath(GetConf.locator("设备告警", "二级菜单_历史告警"))
# time.sleep(1)
# dangqiangaojing_h2.click()
# word_element_1 = BasePage(driver).wait_eleVisible(GetConf.locator("设备告警", "元素_当前未结数量"))
# print(word_element_1.text)

WebDriverWait(driver,20, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, '//span[text()="权限管理"]'))).click()
# time.sleep(1)
# WebDriverWait(driver,20, 1).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[text()="账号管理"]'))).click()
# WebDriverWait(driver,20, 1).until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[text()="新建账号"]'))).click()
# WebDriverWait(driver,20, 1).until(expected_conditions.presence_of_element_located((By.XPATH, '//form[@class="el-form el-form--label-top"]/div[2]/div[1]//input[@class="el-input__inner"]'))).send_keys("rrrere")

base_page.wait_eleclickable(GetConf.locator("权限管理", "一级菜单")).click()
base_page.wait_eleclickable(GetConf.locator("权限管理", "二级菜单_角色管理")).click()

role = base_page.ele_exist_or_not(GetConf.locator("权限管理", "元素_被删除的角色"))
print(role)


