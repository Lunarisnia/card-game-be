class FlaskAppWrapper():
    def __init__(self, app, **configs) -> None:
        self.app = app
        self.configs(**configs)

    def configs(self, **configs):
        self.app.config.update(**configs)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], **options):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, **options)