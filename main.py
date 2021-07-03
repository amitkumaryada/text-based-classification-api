import os
import yaml
from flask import Flask,redirect
from apis import blueprint as api

with open(r"./configuration/config.yml") as file:
    config =yaml.load(file,Loader = yaml.FullLoader)

app = Flask(__name__)
app.register_blueprint(api,url_prefix = "/api/v1")

DEFAULT_API_VERSION = config['DEFAULT_API_VERSION']

@app.route("/")
def redirect_default_version(default_version = DEFAULT_API_VERSION):
    retrun redirect(f"/api/v{default_version}",code =302)


if __name__ =="__main__":
    app.run(debug = config['DEBUG'],host=config['HOST'],port =config['PORT'])

