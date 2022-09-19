class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getAttr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)
    def __setAttr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)


class Spam:
    def __init__(self, x):
        self.x = x
        def bar(self, y):
            print('Spam.bar:', self.x,y)
            
