# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/6 10:49
#   email : youyou.xu@enesource.com
#   project_name :  test-auto-web
#   file_name :  read_conf
#   function： 读取配置文件里的内容;
#                   将读取配置文件的类的调用又封装了一次，简化其他地方调用的操作

import configparser
from common import contants


class ReadConf:
    def __init__(self, conf_file):
        self.cf = configparser.ConfigParser()
        self.cf.read(conf_file, encoding="utf-8")

    def getvalue(self, section, option):
        return self.cf.get(section, option)


class GetConf:
    # 分别读取三个配置文件里的内
    # datas      测试会用到的数据集合
    # conf      日志和测试地址的配置
    # locator  元素的定位表达式集合
    @staticmethod
    def datas(section, option):
        return ReadConf(contants.datas).getvalue(section, option)

    @staticmethod
    def conf(section, option):
        return ReadConf(contants.conf).getvalue(section, option)

    @staticmethod
    def locator(section, option):
        return ReadConf(contants.locator).getvalue(section, option)


if __name__ == "__main__":
    print(GetConf.datas("LOGIN", "user_isnull"))
