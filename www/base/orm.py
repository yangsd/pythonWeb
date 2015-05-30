from www.base import db


class Field(object):
    def __init__(self,**kw):
        self.name = kw.get('name', None)
        self.column_type = kw.get('column_type', '')
        self.primary_key = kw.get('primary_key', False)

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, **kw):
        kw['column_type'] = 'varchar(255)'
        super(StringField, self).__init__(**kw)

class IntegerField(Field):
    def __init__(self, **kw):
        kw['column_type'] = 'bigint'
        super(IntegerField, self).__init__(**kw)

class FloatField(Field):
    def __init__(self, **kw):
        kw['column_type'] = 'real'
        super(FloatField, self).__init__(**kw)

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):				
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        primary_key = None
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    primary_key = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        if not '__table__' in attrs:
            attrs['__table__'] = name.lower()
        attrs['__mappings__'] = mappings
        attrs['__table__'] = attrs['__table__']
        attrs['__primary_key__'] = primary_key
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    @classmethod
    def insert(self):
        params = {}
        for k, v in self.__mappings__.iteritems():
            params[v.name] = getattr(self, k)
            #print(v.name,getattr(self, k))
        db.insert(self.__table__, **params)
        return self

    @classmethod
    def find_all(cls, *args):
        '''
        Find all and return list.
        '''
        #L = db.select('select * from `%s`' % cls.__table__)
        L = db.select('select * from user')
        print(L);
        return [cls(**d) for d in L]
	