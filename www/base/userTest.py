__author__ = 'sdyang'

import time
from www.base.tables import User
from www.base import db


db.create_engine('root', 'mysql', 'test')

#u = User(name='sdyang', email='yangsd@tcl.com', passwd='123456', id='123',last_modified= time.time())
#u.insert()
#print(u.id)

User.find_all()