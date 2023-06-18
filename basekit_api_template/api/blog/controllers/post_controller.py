from flask import request
from basekit_core_lib.api.middlewares.logger_middleware import log_decorator
from basekit_core_lib.api.controllers.base_controller import BaseController
from basekit_api_template.api.blog.services.post_service import PostService

class PostController(BaseController):
    def __init__(self, service:PostService):
        super().__init__(service)