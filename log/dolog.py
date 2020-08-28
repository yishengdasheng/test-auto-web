# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/8/6 14:24
#   email : youyou.xu@enesource.com
#   project_name :  test-auto-web
#   file_name :  dolog
#   function： 
import logging
from config.read_conf import ReadConf
import datetime
from common import contants

time = datetime.date.today()

conf = ReadConf(contants.conf)
name = conf.getvalue("LOG", "name").upper()
in_level = conf.getvalue("LOG", "in_level").upper()
out_level = conf.getvalue("LOG", "out_level").upper()
out_file_level = conf.getvalue("LOG", "out_file_level").upper()
file_path = contants.base_dir + conf.getvalue("LOG", "file_path") + name + str(time) + '.txt'
log_format = conf.getvalue("LOG", "log_format")


class DoLog:
    @staticmethod
    def mylog(level, msg):
        my_logger = logging.getLogger(name)
        my_logger.setLevel(in_level)
        formatter = logging.Formatter(log_format)
        fh = logging.FileHandler(file_path, mode='a', encoding='utf-8')
        fh.setLevel(out_file_level)
        fh.setFormatter(formatter)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
                my_logger.info(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.mylog("DEBUG", msg)

    def info(self, msg):
        self.mylog("INFO", msg)

    def error(self, msg):
        self.mylog("ERROR", msg)

    def warning(self, msg):
        self.mylog("WARNING", msg)

    def critical(self, msg):
        self.mylog("CRITICAL", msg)


if __name__ == "__main__":
    my_logger = DoLog()
    my_logger.debug("%s test日志信息" % time)