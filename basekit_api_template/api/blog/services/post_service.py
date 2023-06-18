from basekit_core_lib.api.services.base_service import BaseService
from basekit_api_template.api.blog.models.post import Post
from basekit_api_template.api.blog.schemas import PostSchema
from basekit_core_lib.config.helpers import db

class PostService(BaseService):
    def __init__(self) -> None:
        super().__init__(Post, PostSchema())
        
    def get_all(self):
        try:
            models = self._get_all() 
            model_data = self.model_schema.dump(models, many=True)
            return model_data
        except Exception as e:
            db.session.rollback()  # Executa o rollback para reverter a transação
            raise Exception(f"Erro ao obter todas os aplicações: {e}")

    def get_by_id(self, id):
        try:
            model = self._get_by_id(id)
            if model:
                model_data = self.model_schema.dump(model)
                return model_data
            return None
        except Exception as e:
            db.session.rollback()  # Executa o rollback para reverter a transação
            raise Exception(f"Erro ao obter post por ID {id}: {e}")
    
    def create(self, model_data):
        try:
            self.is_valid(self.model_schema, model_data)  # Valida o schema antes de criar o post
            
            model_data.pop('roles', [])  # Extrai as informações de ações
            model = self._create(model_data)
            model_data = self.model_schema.dump(model)
            return model_data
        except Exception as e:
            db.session.rollback()  # Executa o rollback para reverter a transação
            raise Exception(f"Erro ao criar aplicações: {e}")
    
    def update(self, id, model_data):
        try:         
            model_data.pop('roles', [])  # Extrai as informações de ações              
            self.is_valid(self.model_schema, model_data) # Valida o schema antes de atualizar o post
            model = Post.query.get(id)
            if model:
                self._update(model, model_data, self.model_schema)
                model_data = self.model_schema.dump(model)
                return model_data
            return None
        except Exception as e:
            db.session.rollback()  # Executa o rollback para reverter a transação
            raise Exception(f"Erro ao atualizar post com ID {id}: {e}")

    def delete(self, id):
        try:
            return self._delete(id)
        except Exception as e:
            db.session.rollback()  # Executa o rollback para reverter a transação
            raise Exception(f"Erro ao excluir post com ID {id}: {e}")
    
