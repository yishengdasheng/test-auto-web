# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/26 17:51
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  testsuite
#   function：执行用例

import unittest
from common import HTMLTestRunnerNew
from common import contants
import datetime
from testcases.testSmokeCase import TestSmokeCases
from testcases.test_login import TestLogin
from testcases.test_operationMonitor import TestOperationMonitor
from testcases.test_manage import TestManage

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestLogin))

report = contants.report
test_time = datetime.date.today()

with open(report, "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title=str(test_time) + "web自动化测试报告", tester="YOYO")
    runner.run(suite)
