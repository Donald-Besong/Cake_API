from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
#********** begin sawgger****************************
from flask_swagger_ui import get_swaggerui_blueprint
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "Api_from_Donald"}
        )

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
    
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)
#********** end sawgger******************************


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'don'
api = Api(app)


#@app.before_first_request
#def create_tables():
#    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item, '/cake/<string:name>')
api.add_resource(ItemList, '/cakes')
api.add_resource(UserRegister, '/register')

from db import db
db.init_app(app)
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
