import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StrucTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) !=len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)


class Stock(StrucTuple):
    _fields = ['name', 'shares', 'price']

class Point(StrucTuple):
    _fields = ['x', 'y']
    
