from www.base.orm import Model, StringField, IntegerField,FloatField
class User(Model):
    __table__ = 'user'
    id = IntegerField(primary_key=True,name = "id")
    name = StringField(name = "name")
    email = StringField(name = "email")
    passwd = StringField(name = "passwd")
    last_modified = FloatField(name = "last_modified")

