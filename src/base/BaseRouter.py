class BaseRouter():    
    def __new__(self, endpoint, endpoint_name=None, handler_function=None, methods=['GET']):
        self.endpoint = endpoint
        self.methods = methods
        self.endpoint_name = endpoint_name
        self.handler_function = handler_function

        return {
            "endpoint": self.endpoint,
            "endpoint_name": self.endpoint_name,
            "handler": self.handler_function,
            "methods": self.methods
        }