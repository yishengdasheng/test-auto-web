# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/7/21 10:22
#   email : youyou.xu@enesource.com
#   project_name :  test-auto-web
#   file_name :  test
#   function：测试用例
# 显性等待语法    WebDriverWait(webdriver对象, 等待时长，轮询周期).until(判断条件)
# 生成判断条件    expected_conditions.方法名((定位方式， 定位表达式))  元组格式
# 查找某元素是否存在  expected_conditions.presence_of_element_located((By.XPATH, logo))
import unittest
import pytest
from selenium import webdriver
from config.read_conf import ReadConf
from common import contants
from testcases.basepage import BasePage


governor_url = ReadConf(contants.conf).getvalue("URL", "governor_url")
datas = ReadConf(contants.datas)
name = datas.getvalue("USER", "username")
password = datas.getvalue("USER", "password")

options = ReadConf(contants.options)


class TestCases(unittest.TestCase, BasePage):
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument("--disable-infobars")  # 关闭浏览器的提示栏
        # 实例化chrome类，启动chrome浏览器
        driver = webdriver.Chrome(options=option, service_args=["--verbose"], service_log_path="chrome_server.log")
        driver.get(governor_url)
        # 设置全局等待
        driver.implicitly_wait(30)
        basepage = BasePage(driver)
        globals()["driver"] = driver

    @classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()

    def test_login(self):

        username = driver.find_element_by_xpath(options.getvalue("登录", "用户名"))
        pwd = driver.find_element_by_xpath(options.getvalue("登录", "密码"))
        login_button = driver.find_element_by_xpath(options.getvalue("登录", "登录"))

        username.send_keys(name)
        pwd.send_keys(password)
        login_button.click()

        # 检查登录后首页的logo元素有没有出现
        # logo = driver.find_element_by_xpath('//p[@class="title ml30 flex-row flex-center"]')  # presence_of_element_located() 后面的值一定要是str
        logo = options.getvalue("登录", "能源节度使")
        basepage.wait_eleVisible(logo, wait_time=5)

     # 能源驾驶舱
    def test_skyView(self):
        basepage = BasePage(driver)
        nengyuanjiashicang_h2 = driver.find_element_by_xpath(options.getvalue("能源驾驶舱", "二级菜单"))
        nengyuanjiashicang_h2.click()

        word_element = options.getvalue("能源驾驶舱", "本月累计电量")
        basepage.wait_eleVisible(word_element, wait_time=5)

    # 设备告警
    def test_operationMonitor(self):
        basepage = BasePage(driver)
        shebeigaojing_h1 = self.driver.find_element_by_xpath(options.getvalue("设备告警", "一级菜单"))
        shebeigaojing_h1.click()

        dangqiangaojing_h2 = self.driver.find_element_by_xpath(options.getvalue("设备告警", "二级菜单_当前告警"))
        lishigaojing_h2 = self.driver.find_element_by_xpath(options.getvalue("设备告警", "二级菜单_历史告警"))

        dangqiangaojing_h2.click()
        word_element_1 = options.getvalue("设备告警", "元素_当前未结")
        basepage.wait_eleVisible(word_element_1, wait_time=5)

        lishigaojing_h2.click()
        word_element_2 = options.getvalue("设备告警", "元素_查询按钮")
        basepage.wait_eleVisible(word_element_2, wait_time=5)


    # 实时监测
    # def test_currentAlarm(self):
    #
    #     shishijiance_h1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[3]/div/span')
    #     shishigongkuang_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[3]/ul/li/ul/li[1]/span')
    #     mingxichaxun_h2 = self.driver.find_element_by_xpath('//span[text()="明细查询"]')
    #
    #     shishijiance_h1.click()
    #     shishigongkuang_h2.click()
    #
    #     # 检查有没有出现弹窗提醒，有则点确定关掉弹窗
    #     time.sleep(3)
    #     try:
    #         ok = self.driver.switch_to.alert
    #         ok.accept()
    #     except e.NoAlertPresentException as noalert:
    #         print(noalert)
    #
    #     # 切换站点到 宜山大楼
    #     xiala_element = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/span/span/i')
    #     xiala_element.click()
    #     yishandalou = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[4]/span')
    #     yishandalou.click()
    #
    #     time.sleep(2)
    #     word_element_4 = '//*[@id="text4"]/text'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_4)))
    #     # except e.InvalidSelectorException as error:
    #     #     print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     #     self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     # except e.NoSuchElementException as error:
    #     #     print("没有找到该元素")
    #     #     self.logger.error("没有找到该元素")
    #     # except TimeoutError as error:
    #     #     print("等待页面超时")
    #     except Exception as error:
    #         self.logger.error(error)
    #         print(error)
    #
    #
    #     mingxichaxun_h2.click()
    #     word_element_5 = '//*[@id="pane-day"]/button'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_5)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")

    # 运维工单
    # def test_orderManage(self):
    #
    #     # 切换到运维工单
    #     yunweigongdan_h1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[4]/div/span')
    #     gongzuotai_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[4]/ul/li/ul/li[1]/span')
    #     dingjianguanli_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[4]/ul/li/ul/li[2]/span')
    #     gongdanchaxun_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[4]/ul/li/ul/li[3]/span')
    #
    #     yunweigongdan_h1.click()
    #     gongzuotai_h2.click()
    #     word_element_6 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div/span/img'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_6)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     dingjianguanli_h2.click()
    #     word_element_7 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/span'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_7)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     gongdanchaxun_h2.click()
    #     word_element_8 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/table/thead/tr/th[2]/div'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_8)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")


    # 电能质量
    # def test_eleQuality(self):
    #
    #     # 切换到电能质量
    #     diannengzhiliang_h1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[5]/div/span')
    #     gailan_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[5]/ul/li/ul/li[1]/span')
    #     dianyapiancha_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[5]/ul/li/ul/li[2]/span')
    #     gongleyinshu_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[5]/ul/li/ul/li[3]/span')
    #     sanxiangdianliu_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[5]/ul/li/ul/li[4]/span')
    #     xiebodianliu_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[5]/ul/li/ul/li[5]/span')
    #     xiebodianya_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[5]/ul/li/ul/li[6]/span')
    #
    #     diannengzhiliang_h1.click()
    #     gailan_h2.click()
    #     word_element_9 = '//*[@id="my-canvas-left2"]'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_9)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     dianyapiancha_h2.click()
    #     word_element_10 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li[1]/span[2]'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_10)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     gongleyinshu_h2.click()
    #     word_element_11 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li/span[2]'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_11)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     sanxiangdianliu_h2.click()
    #     word_element_12 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li[1]/span[2]'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_12)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     xiebodianliu_h2.click()
    #     word_element_13 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li[3]'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_13)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     xiebodianya_h2.click()
    #     word_element_14 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li[3]'
    #     try:
    #             WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_14)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")

    # 报表管理
    # def test_report(self):
    #
    #
    #     # 切换到报表管理
    #     baobiao_h1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[6]/div/span')
    #     ribao_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[6]/ul/li/ul/li[1]/span')
    #     yuebao_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[6]/ul/li/ul/li[2]/span')
    #
    #     baobiao_h1.click()
    #     ribao_h2.click()
    #     word_element_15 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[1]/div[1]/button/span'
    #     try:
    #             WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_15)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     yuebao_h2.click()
    #     word_element_16 = '//*[@id="itableLastMonthShowFlag"]/div[2]/table/thead/tr[1]/th[2]'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_16)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #          print("等待页面超时")

    # 权限管理
    # def test_manage(self):
    #
    #
    #     # 切换到权限管理
    #     quanxian_h1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[7]/div/span')
    #     zhanghao_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[7]/ul/li/ul/li[1]/span')
    #     zuzhi_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[7]/ul/li/ul/li[2]/span')
    #     role_h2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/ul/li[7]/ul/li/ul/li[3]/span')
    #
    #     quanxian_h1.click()
    #     zhanghao_h2.click()
    #     word_element_17 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_17)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     zuzhi_h2.click()
    #     word_element_18 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_18)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")
    #
    #     role_h2.click()
    #     word_element_19 = '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/span'
    #     try:
    #         WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH, word_element_19)))
    #     except e.InvalidSelectorException as error:
    #         print("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #         self.logger.error("元素定位表达式 logo 不正确，请修正：{}".format(word_element_1))
    #     except e.NoSuchElementException as error:
    #         print("没有找到该元素")
    #         self.logger.error("没有找到该元素")
    #     except TimeoutError as error:
    #         print("等待页面超时")





