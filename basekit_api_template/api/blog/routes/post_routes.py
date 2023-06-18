from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from basekit_api_template.api.blog.controllers import PostController
from dependency_injector.wiring import inject, Provide
from basekit_core_lib.api.middlewares.auth_middleware import authorize, Authorize
from basekit_api_template.core_lib.app_container import AppContainer
from basekit_core_lib.api.middlewares.exception_middleware import handle_exceptions

post_routes = Blueprint('post_routes', __name__,url_prefix='blog')

@post_routes.route('/posts', methods=['GET'])
@jwt_required()
@inject
@authorize(tag_name='POSTS', authorize=Authorize.READ)
@swag_from({
    'tags': ['Posts'],
    'summary': 'Obter todos Posts',
    'responses': {
        '200': {
            'description': 'Lista de Posts',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'title': {'type': 'string'},
                                'tag_name': {'type': 'string'},
                            }
                        }
                    },
                    'success': {'type': 'boolean'}
                }
            }
        }
    }
})
@handle_exceptions
def get_all_post(controller: PostController = Provide[AppContainer.post_controller]):
    return controller.get_all()

@post_routes.route('/posts/<int:id>', methods=['GET'])
@jwt_required()
@inject
@authorize(tag_name='POSTS', authorize=Authorize.READ)
@swag_from({
    'tags': ['Posts'],
    'summary': 'Obter Post',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do Post'
        }
    ],
    'responses': {
        '200': {
            'description': 'Obter Post',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'object',
                        'properties': {
                                'id': {'type': 'integer'},
                                'name': {'type': 'string'},
                                'tag_name': {'type': 'string'},
                            }
                    },
                    'success': {'type': 'boolean'}
                }
            }
        }
    }
})
@handle_exceptions
def get_post(controller: PostController = Provide[AppContainer.post_controller], id= None):
    return controller.get_by_id(id)

@post_routes.route('/posts', methods=['POST'])
@jwt_required()
@inject
@authorize(tag_name='POSTS', authorize=Authorize.CREATE)
@swag_from({
    'tags': ['Posts'],
    'summary': 'Criar nova Post',
    'parameters': [
        {
            'name': 'post',
            'in': 'body',
            'required': True,
            'description': 'post data',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Nome do Post'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Post criada com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'object',
                        'properties': {
                                'id': {'type': 'integer'},
                                'title': {'type': 'string'},
                                'description': {'type': 'string'}
                            }
                    },
                    'success': {'type': 'boolean'}
                }
            }
        }
    }
})
@handle_exceptions
def create_post(controller: PostController = Provide[AppContainer.post_controller]):
    return controller.create()

@post_routes.route('/posts/<int:id>', methods=['PUT'])
@jwt_required()
@inject
@authorize(tag_name='POSTS', authorize=Authorize.UPDATE)
@swag_from({
    'tags': ['Posts'],
    'summary': 'Atualizar Post',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do Post'
        },
        {
            'name': 'post',
            'in': 'body',
            'required': True,
            'description': 'post data',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Nome do Post'
                    }
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Post atualizada com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'object',
                        'properties': {
                                'id': {'type': 'integer'},
                                'title': {'type': 'string'},
                                'description': {'type': 'string'}
                            }
                    },
                    'success': {'type': 'boolean'}
                }
            }
        }
    }
})
@handle_exceptions
def update_post(controller: PostController = Provide[AppContainer.post_controller], id= None):
    return controller.update(id)

@post_routes.route('/posts/<int:id>', methods=['DELETE'])
@jwt_required()
@inject
@authorize(tag_name='POSTS', authorize=Authorize.DELETE)
@swag_from({
    'tags': ['Posts'],
    'summary': 'Excluir Post',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do Post'
        }
    ],
    'responses': {
        '200': {
            'description': 'Excluir Post',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'object',
                        'properties': {
                                'message': {'type': 'string'},
                            }
                    },
                    'success': {'type': 'boolean'}
                }
            }
        }
    }
})
@handle_exceptions
def delete_post(controller: PostController = Provide[AppContainer.post_controller], id= None):
    return controller.delete(id)
