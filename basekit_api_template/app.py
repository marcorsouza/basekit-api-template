from basekit_api_template.server import Server
from flask import Flask, redirect


app = Flask(__name__)        
server = Server(app)

@server.app.route('/')
def index():
    return redirect('/apidocs/')

if(__name__ == '__main__'):
    server.run()