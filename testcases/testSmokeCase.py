# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/7/21 10:22
#   email : youyou.xu@enesource.com
#   project_name :  test-auto-web
#   file_name :  test
#   function：测试用例
# 显性等待语法    Webbase_page.driverWait(webbase_page.driver对象, 等待时长，轮询周期).until(判断条件)
# 生成判断条件    expected_conditions.方法名((定位方式， 定位表达式))  元组格式
# 查找某元素是否存在  expected_conditions.presence_of_element_located((By.XPATH, logo))
import unittest
from config.read_conf import GetConf
import time
from selenium.common.exceptions import *
from pages.basepage import BasePage


class TestSmokeCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # option = webbase_page.driver.ChromeOptions()
        # option.add_argument("--disable-infobars")  # 关闭浏览器的提示栏
        # # 实例化chrome类，启动chrome浏览器
        # base_page.driver = webbase_page.driver.Chrome(options=option, service_args=["--verbose"])
        # base_page.driver.get(GetConf.conf("URL", "governor_url"))

        # 设置全局等待
        # base_page.driver.implicitly_wait(30)

        cls.base_page = BasePage("https://governor.enesource.com")
        cls.base_page.logger.info("================================")

        # cls.base_page.driver = base_page.driver

    @classmethod
    def tearDownClass(cls):
        cls.base_page.driver.quit()
        cls.base_page.logger.info("关闭浏览器")

    def test_1_login(self):
        user = eval(GetConf.datas("USER", "user_ok"))
        self.base_page.login(user["username"], user["password"])
        logo_locator = GetConf.locator("能源节度使", "logo")
        self.base_page.wait_eleVisible(logo_locator, wait_time=10)

        # 检查登录后首页的logo元素有没有出现
        # logo = base_page.driver.find_element_by_xpath('//p[@class="title ml30 flex-row flex-center"]')  # presence_of_element_located() 后面的值一定要是str
        try:
            self.assertTrue('能源节度使' in logo_locator)
        except AssertionError as e:
            self.base_page.logger.error("test_1_login 用例断言失败")
            raise e

    # 能源驾驶舱
    def test_2_skyView(self):
        nengyuanjiashicang_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("能源驾驶舱", "二级菜单"))
        nengyuanjiashicang_h2.click()

        word_element = GetConf.locator("能源驾驶舱", "能源消耗总量")
        # self.base_page.wait_eleVisible(word_element, wait_time=10)
        try:
            self.assertTrue("能源消耗总量" in word_element)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_2_skyView 用例断言失败")
            raise e

    # 设备告警
    def test_3_operationMonitor(self):
        shebeigaojing_h1 = self.driver.find_element_by_xpath(GetConf.locator("设备告警", "一级菜单"))
        shebeigaojing_h1.click()

        dangqiangaojing_h2 = self.driver.find_element_by_xpath(GetConf.locator("设备告警", "二级菜单_当前告警"))
        lishigaojing_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("设备告警", "二级菜单_历史告警"))

        dangqiangaojing_h2.click()
        word_element_1 = GetConf.locator("设备告警", "元素_当前未结")
        # self.base_page.wait_eleVisible(word_element_1, wait_time=10)
        try:
            self.assertTrue("当前未结" in word_element_1)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_3_operationMonitor,当前告警 用例断言失败")
            raise e

        lishigaojing_h2.click()
        word_element_2 = GetConf.locator("设备告警", "元素_查询按钮")
        # self.base_page.wait_eleVisible(word_element_2, wait_time=10)
        try:
            self.assertTrue("查询" in word_element_2)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_3_operationMonitor,历史告警 用例断言失败")
            raise e

    # 实时监测
    def test_4_currentAlarm(self):
        shishijiance_h1 = self.driver.find_element_by_xpath(GetConf.locator("实时监测", "一级菜单"))
        shishigongkuang_h2 = self.driver.find_element_by_xpath(GetConf.locator("实时监测", "二级菜单_实时工况"))
        mingxichaxun_h2 = self.driver.find_element_by_xpath(GetConf.locator("实时监测", "二级菜单_明细查询"))
        shishijiance_h1.click()
        shishigongkuang_h2.click()

        # 检查有没有出现弹窗提醒，有则点确定关掉弹窗
        time.sleep(3)
        try:
            ok = self.base_page.driver.switch_to.alert
            ok.accept()
        except (NoSuchElementException, NoAlertPresentException) as noalert:
            print(noalert)

        # 切换站点到 宜山大楼
        xiala_element = self.base_page.driver.find_element_by_xpath(GetConf.locator("实时监测", "下拉箭头"))
        xiala_element.click()
        yishandalou = self.base_page.driver.find_element_by_xpath(GetConf.locator("实时监测", "宜山大楼"))
        yishandalou.click()

        time.sleep(2)
        word_element_4 = GetConf.locator("实时监测", "接线图文字")
        try:
            self.base_page.wait_eleVisible(word_element_4, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_4_currentAlarm,实时工况 用例断言失败")
            raise e

        mingxichaxun_h2.click()
        word_element_5 = GetConf.locator("实时监测", "明细查询_查询按钮")
        try:
            self.base_page.wait_eleVisible(word_element_5, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_4_currentAlarm,明细查询 用例断言失败")
            raise e

    # 运维工单
    def test_5_orderManage(self):
        yunweigongdan_h1 = self.base_page.driver.find_element_by_xpath(GetConf.locator("运维工单", "一级菜单"))
        gongzuotai_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("运维工单", "二级菜单_工作台"))
        dingjianguanli_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("运维工单", "二级菜单_定检管理"))
        gongdanchaxun_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("运维工单", "二级菜单_工单查询"))

        yunweigongdan_h1.click()
        gongzuotai_h2.click()
        word_element_1 = GetConf.locator("运维工单", "工作台_头像")
        try:
            self.base_page.wait_eleVisible(word_element_1, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_5_orderManage,工作台 用例断言失败")
            raise e

        dingjianguanli_h2.click()
        word_element_2 = GetConf.locator("运维工单", "元素_定检管理_新增计划")
        try:
            self.base_page.wait_eleVisible(word_element_2, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_5_orderManage,定检管理 用例断言失败")
            raise e

        gongdanchaxun_h2.click()
        word_element_3 = GetConf.locator("运维工单", "元素_工单查询_工单编号")
        try:
            self.assertTrue("工单编号" in word_element_3)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_5_orderManage,工单查询 用例断言失败")
            raise e

    # 电能质量
    def test_6_eleQuality(self):
        diannengzhiliang_h1 = self.base_page.driver.find_element_by_xpath(GetConf.locator("电能质量", "一级菜单"))
        gailan_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("电能质量", "二级菜单_电能质量概览"))
        dianyapiancha_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("电能质量", "二级菜单_电压偏差"))
        gongleyinshu_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("电能质量", "二级菜单_功率因数"))
        sanxiangdianliu_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("电能质量", "二级菜单_三相电流不平衡"))
        xiebodianliu_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("电能质量", "二级菜单_谐波电流"))
        xiebodianya_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("电能质量", "二级菜单_谐波电压"))

        # 概览页面
        diannengzhiliang_h1.click()
        gailan_h2.click()
        word_element_1 = GetConf.locator("电能质量", "元素_指标")
        try:
            self.base_page.wait_eleVisible(word_element_1, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_6_eleQuality,电能质量概览 用例断言失败")
            raise e

        # 电压偏差页面
        dianyapiancha_h2.click()
        word_element_2 = GetConf.locator("电能质量", "元素_电压合格率")
        try:
            self.base_page.wait_eleVisible(word_element_2, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_6_eleQuality,电压偏差 用例断言失败")
            raise e

        # 功率因数页面
        gongleyinshu_h2.click()
        word_element_3 = GetConf.locator("电能质量", "元素_功率因素")
        try:
            self.base_page.wait_eleVisible(word_element_3, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_6_eleQuality,功率因数 用例断言失败")
            raise e

        # 三相电流不平衡页面
        sanxiangdianliu_h2.click()
        word_element_4 = GetConf.locator("电能质量", "元素_最大不平衡率")
        try:
            self.base_page.wait_eleVisible(word_element_4, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_6_eleQuality,三相电流不平衡 用例断言失败")
            raise e

        # 谐波电流页面
        xiebodianliu_h2.click()
        word_element_5 = GetConf.locator("电能质量", "元素_最大A相电流总畸变率")
        try:
            self.base_page.wait_eleVisible(word_element_5, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_6_eleQuality,谐波电流 用例断言失败")
            raise e

        # 谐波电压页面
        xiebodianya_h2.click()
        word_element_6 = GetConf.locator("电能质量", "元素_最大A相电压总畸变率")
        try:
            self.base_page.wait_eleVisible(word_element_6, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_6_eleQuality,谐波电压 用例断言失败")
            raise e

    # 报表管理
    def test_7_report(self):
        baobiao_h1 = self.base_page.driver.find_element_by_xpath(GetConf.locator("报表管理", "一级菜单"))
        ribao_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("报表管理", "二级菜单_日报"))
        yuebao_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("报表管理", "二级菜单_月报"))

        # 日报
        baobiao_h1.click()
        ribao_h2.click()
        word_element_1 = GetConf.locator("报表管理", "元素_表头")
        try:
            self.base_page.wait_eleVisible(word_element_1, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_7_report,日报 用例断言失败")
            raise e

        # 月报
        yuebao_h2.click()
        word_element_2 = GetConf.locator("报表管理", "元素_表格")
        try:
            self.base_page.wait_eleVisible(word_element_2, wait_time=10)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_7_report,月报 用例断言失败")
            raise e

    # 权限管理
    def test_8_manage(self):
        quanxian_h1 = self.base_page.driver.find_element_by_xpath(GetConf.locator("权限管理", "一级菜单"))
        zhanghao_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("权限管理", "二级菜单_账号管理"))
        zuzhi_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("权限管理", "二级菜单_组织管理"))
        role_h2 = self.base_page.driver.find_element_by_xpath(GetConf.locator("权限管理", "二级菜单_角色管理"))

        # 账号管理
        quanxian_h1.click()
        zhanghao_h2.click()
        word_element_1 = GetConf.locator("权限管理", "元素_新建账号")
        try:
            # self.base_page.wait_eleVisible(word_element_1, wait_time=10)
            self.assertTrue("新建账号" in word_element_1)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_8_manage,账号管理 用例断言失败")
            raise e

        # 组织管理
        zuzhi_h2.click()
        word_element_2 = GetConf.locator("权限管理", "元素_成员管理")
        try:
            # self.base_page.wait_eleVisible(word_element_2, wait_time=10)
            self.assertTrue("成员管理" in word_element_2)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_8_manage,组织管理 用例断言失败")
            raise e

        # 角色管理
        role_h2.click()
        word_element_3 = GetConf.locator("权限管理", "元素_创建角色")
        try:
            # self.base_page.wait_eleVisible(word_element_3, wait_time=10)
            self.assertTrue("创建角色" in word_element_3)
            self.base_page.logger.info("用例成功执行")
        except AssertionError as e:
            self.base_page.logger.error("test_8_manage,角色管理 用例断言失败")
            raise e


if __name__ == "__main__":
    unittest.main()



