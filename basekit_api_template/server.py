import inspect
import os
from flask import Flask
from basekit_api_template.core_lib.route_loader import load_routes
from basekit_api_template.core_lib.swagger_config import swagger_init_app
from basekit_api_template.core_lib.app_container import AppContainer
from basekit_core_lib.server_base import ServerBase

container = AppContainer()  

class Server(ServerBase):
    def __init__(self, app: Flask) -> None:
        super().__init__(app)
        
    def configure_routes(self):            
        load_routes(self.blue_print, container)
        
    def swagger_init_app(self):
        swagger_init_app(self.app)