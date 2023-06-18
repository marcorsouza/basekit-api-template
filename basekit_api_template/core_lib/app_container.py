from dependency_injector import containers, providers
from basekit_api_template.api.blog.services.post_service import PostService
from basekit_api_template.api.blog.controllers import PostController

class AppContainer(containers.DeclarativeContainer):    
    post_service = providers.Singleton(PostService)    
    post_controller = providers.Singleton(PostController, service = post_service) 
    