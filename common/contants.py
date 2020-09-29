# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/6 10:54
#   email : youyou.xu@enesource.com
#   project_name :  test-auto-web
#   file_name :  contants
#   function： 设置各个文件的路径变量

import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件的目录
conf_file = os.path.join(base_dir, "config")
conf = os.path.join(conf_file, "conf.ini")
locator = os.path.join(conf_file, "locator.ini")
datas = os.path.join(conf_file, "data.ini")

# pages = os.path.join(base_dir, "pages")
# test_data_file = os.path.join(base_dir, "test_data")

report_dir = os.path.join(base_dir, "test_report")
report = os.path.join(report_dir, "report.html")
screenshot_dir = os.path.join(base_dir, "screenshot")
