import urllib.parse
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from config.config import Config

databasepoolinstantiation=''

class Databasepool():
    def __init__(self):
        self.enginedict = {}
        self.sessiondict = {}
        self.basedict = {}
        self.config = Config()

    def get_session (self, section):
        """
        获取数据库连接
        :param section:
        :return:
        """
        if section not in sessiondict:
            self._set_session(section)
        session = sessiondict[section]()
        return session

    def _set_session(self,section):
        engine = self.get_engine(section)
        Session = sessionmaker(bind=engine)
        self.sessiondict[section] = Session


    def get_engine(self, section='localdb'):
        """
        获取databaseurl
        :param section:
        :param autocommit:
        :return: databaseurl
        """
        if section not in self.enginedict:
            self._set_engine(section)
        return self.enginedict[section]

    def _set_engine(self, section,autocommit=True):
        type = self.config.get_cfg(section, 'type')
        databaseurl = self.config.get_cfg('databaseurl', type)
        if type == 'sqlite':
            path = self.config.get_cfg(section, 'path')
            databaseurl = databaseurl.format(path=path)
        else:
            host = self.config.get_cfg(section, 'host')
            port = self.config.get_cfg(section, 'port')
            user = self.config.get_cfg(section, 'user')
            password = self.config.get_cfg(section, 'password')
            database = self.config.get_cfg(section, 'database')
            databaseurl = databaseurl.format(host=host, port=port, user=user, password=password, database=database)
        engine = create_engine(databaseurl)
        self.enginedict[section] = engine

    def getbase(self,section):
        if section not in self.basedict:
            self._setbase(section)
        return self.basedict[section]

    def _setbase(self,section):
        engine = self.get_engine(section)
        Base = declarative_base(bind=engine)
        self.basedict[section] = Base

    def initialize(self,section='localdb'):
        self.getbase(section)



def databasepool():
    global databasepoolinstantiation
    if not databasepoolinstantiation:
        databasepoolinstantiation = Databasepool()
    return databasepoolinstantiation





if __name__ == '__main__':
    databasepool().initialize('localdb')