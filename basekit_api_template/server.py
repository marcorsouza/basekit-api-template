import inspect
import os
from flask import Blueprint, Flask
from flask_jwt_extended import JWTManager
from basekit_api_template.core_lib.route_loader import load_routes
from basekit_core_lib.config.helpers import db, ma, config
from basekit_api_template.core_lib.swagger_config import swagger_init_app
from basekit_core_lib.api.middlewares.auth_middleware import authenticate
from basekit_api_template.core_lib.app_container import AppContainer

container = AppContainer()  

class Server:
    def __init__(self, app: Flask) -> None:
        self.app = app
        self.blue_print = Blueprint('api', __name__, url_prefix='/api')           
        self.config =config
        self.app.config.from_object(self.config)
        
        self.app.secret_key = self.config.SECRET_KEY
        self.app.config['JWT_SECRET_KEY'] = self.config.SECRET_KEY # Defina sua chave secreta
        JWTManager(self.app)
                     
        self.configure_routes()
        self.app.register_blueprint(self.blue_print)
        
        db.init_app(self.app)
        ma.init_app(self.app)
        swagger_init_app(self.app)
        
        self.configure_autenticate_routes()
        
        super().__init__()
        
    def configure_routes(self):            
        load_routes(self.blue_print, container)
        
    def configure_autenticate_routes(self,):
        for route in self.app.url_map.iter_rules():
            if route.rule.startswith('/api/') and not route.rule.startswith('/api/auth/') and not 'recovery_password' in route.rule:
                self.app.view_functions[route.endpoint] = authenticate(self.app.view_functions[route.endpoint])
            
    def run(self, ):
        self.app.run(
            port=self.config.PORT,
            debug=self.config.DEBUG,
            host=self.config.HOST
        )