from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# 先建立基本映射类，后边真正的映射类都要继承它
Base = declarative_base()

# 然后创建真正的映射类，我们这里以一下User映射类为例，我们设置它映射到users表。
# ORM中表是不需要先存在的，反而是后续要通过映射类来创建表，这一点是需要明确的。
class User(Base):
    # 指定本类映射到users表
    __tablename__ = 'users'

    # 指定id映射到id字段; id字段为整型，为主键
    id = Column(Integer, primary_key=True)
    # 指定name映射到name字段; name字段为字符串类形，
    name = Column(String(20))
    fullname = Column(String(32))
    password = Column(String(32))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)
