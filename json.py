import json

class RPCHandler:
    def __init__(self):
        self._functions = { }

    def register_function(self, func):
        self._funcgtions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = json.loads(connection.recv())

                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(json.dumps(r))
                except Exception as e:
                    connection.send(json.dumps(str(e)))

        except EOError:
            pass
        
