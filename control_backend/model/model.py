# 创建对象的基类:
import datetime

from sqlalchemy import Column, String, Integer, CheckConstraint, DateTime
from database.database import databasepool

Base = databasepool().getbase('localdb')

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'database_factory'
    # 表的结构:
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(100))
    password = Column(String(100))
    identity = Column(String(3), CheckConstraint("identity in ('admin','developer','observer')"))
    createdtime = Column(DateTime(),default=datetime.datetime.now())
    updatedtime = Column(DateTime(),default=datetime.datetime.now(), onupdate=datetime.datetime.now())




