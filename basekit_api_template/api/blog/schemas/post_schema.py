from basekit_api_template.api.blog.models.post import Post
from basekit_core_lib.config.helpers import ma
from flask_marshmallow.fields import fields

class PostSchema(ma.Schema):    
    class Meta:
        model = Post
        fields = ('id', 'title', 'description')