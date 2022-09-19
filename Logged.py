class LoggedMappingMixin:
    '''
 Add logging to get/set/delete operations for debugging.
 '''
    __slots__ = ()

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' _str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    '''
 Only allow a key to be set once.
 '''
    __slot__ =()
    def __seitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key, value)


clsss StringKeysKeysMappingMixin:
    '''
 Restrict keys to strings only
 '''
    __slot__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('key must be strings')
        return super().__setitem__(key, value)

    
        
