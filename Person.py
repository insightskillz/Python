class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete Attribute")

class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name
    @name.setter
    def name(self, value):
        print('Setting nsme to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)
    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)
        
