from collections import OrderedDict

class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise  TypeErro('Expected ', + str(self._expected_type))
        instance.__dict__[self._name] = value



class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.apped(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)
    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()

    
