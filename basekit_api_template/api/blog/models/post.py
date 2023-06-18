from basekit_core_lib.config.helpers import db 

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(4000), nullable=False)
    
    def __init__(self, title, description):
        self.title = title
        self.description = description