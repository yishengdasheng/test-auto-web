# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/6 10:49
#   email : youyou.xu@enesource.com
#   project_name :  test-auto-web
#   file_name :  read_conf
#   function： 读取配置文件里的内容

import configparser
from common import contants

conf_file = contants.conf


class ReadConf:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(conf_file, encoding="utf-8")

    def getvalue(self, section, option):
        return self.cf.get(section, option)


if __name__ == "__main__":
    print(ReadConf().getvalue("LOG", "name"))
