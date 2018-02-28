import os
from configparser import ConfigParser
class Config(object):
    def __init__(self):
        self.conf = ConfigParser()
        if "control.cfg" in os.environ and os.path.isfile(os.environ["control.cfg"]):
            self.conf.read(os.environ["control.cfg"])
        else:
            # path 为control.cfg的绝对地址，默认和当前文件目录下
            path = os.path.realpath(__file__).replace('config.py','control.cfg')
            print(path)
            self.conf.read(path)

    def get_cfg(self, section, name):
        return self.conf.get(section, name)

    def set_cfg(self, section, option, value):
        self.conf.set(section, option, value)
