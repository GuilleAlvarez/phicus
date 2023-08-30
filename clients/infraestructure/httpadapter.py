from flask import Flask, jsonify
from clients.domain.iappclientinterface import IAppClientInterface
from src.tictactoe.table.domain.tables import Tables
from utils.domain.singletonmeta import SingletonMeta


class HttpAdapter(IAppClientInterface,metaclass=SingletonMeta):

    def __init__(self, handler: dict) -> None:
        self.handler = handler

    def run(self):
        """
        Aqui se podria inicializar Flask, FastAPI o cualquier otro framework
        """
        app = Flask(__name__)
        self.import_routes(app)
        app.run()
        
    
    def import_routes(self, app):
        @app.route('/new_game', methods=['GET'])
        def http_endpoint():
            table:Tables = self.handler.get("new_game")()
            return jsonify({"id": table.get_id()}), 201