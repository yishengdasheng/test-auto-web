# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/7 11:03
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  test
#   function：
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common import exceptions as e

driver = webdriver.Chrome()
driver.get("https://governor.enesource.com")
driver.maximize_window()
driver.implicitly_wait(30)
username = driver.find_element_by_xpath('//input[@placeholder="请输入用户名/手机号码/邮箱"]')
pwd = driver.find_element_by_xpath('//input[@placeholder="输入密码"]')
login_button = driver.find_element_by_xpath('//button[@class="el-button login-in cursor el-button--primary"]')

username.send_keys("yoyo")
pwd.send_keys("123456")
login_button.click()

logo = '//p[text()="能源节度使 "]'
try:
    WebDriverWait(driver, 5, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, logo)))
except Exception as error:

    print(error)



# 查询浏览器的窗口
print(driver.window_handles)
# 查询当前所在的窗口
print(driver.current_window_handle)
driver.switch_to.window(driver.window_handles[-1])
# 退出到主页面
driver.switch_to.default_content()