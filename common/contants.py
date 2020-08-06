# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/6 10:54
#   email : youyou.xu@enesource.com
#   project_name :  test-auto-web
#   file_name :  contants
#   function： 设置各个文件的路径变量

import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

conf_file = os.path.join(base_dir, "config")
conf = os.path.join(conf_file, "conf.ini")

test_object_file = os.path.join(base_dir, "object repository")
test_data_file = os.path.join(base_dir, "test data")

report_dir = os.path.join(base_dir, "test report")