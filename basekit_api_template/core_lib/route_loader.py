import glob
import importlib
import os
from basekit_api_template.core_lib.app_container import AppContainer
from basekit_core_lib.config.helpers import config
from basekit_core_lib.utils.file_utils import get_attribute, get_files, get_filename, get_import_module

def load_routes(app, app_container : AppContainer = None):
    
    if app_container is None:
        app_container = AppContainer()
        
    app_folder = config.APPLICATION_FOLDER
    api_folder = config.API_FOLDER
    
    
    list_modules = []    
    
    for file in get_files(api_folder, '_routes.py', True):
        filename, extension = get_filename(file)
        module_base = file.replace('\\','.')
        module_name = module_base[:-3]        
        module = get_import_module(f'{app_folder}.{module_name}')
        blueprint = get_attribute(module, filename)
        list_modules.append(module)
        app.register_blueprint(blueprint) # registra o blueprint da rota no blueprint api  
                           
    if len(list_modules) > 0:
        app_container.wire(modules=list_modules) # carrega o modulo que será injetado