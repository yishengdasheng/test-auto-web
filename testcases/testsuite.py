# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/26 17:51
#   email : youyou.xu@enesource.com
#   project_name :  auto_webTest
#   file_name :  testsuite
#   function：执行用例

import unittest
from common import HTMLTestRunnerNew
from testcases.testcase import TestCases
from common import contants
import datetime

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCases))

report = contants.report
test_time = datetime.date.today()

with open(report, "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title=str(test_time) + "web自动化测试报告", tester="YOYO")
    runner.run(suite)