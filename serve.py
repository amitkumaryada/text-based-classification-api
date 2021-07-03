from waitress import serve
from main import app,config
serve(app,host = config['HOST'],port =config['PROT'])