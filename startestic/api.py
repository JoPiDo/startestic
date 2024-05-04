
from flask import jsonify, request, send_file
import os

from star import Star


class Api:
    def __init__(self, app, galaxy):
        self.app = app
        self.galaxy = galaxy
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def get_hello():
            return jsonify({"message": "Hello Galaxy!"})

        @self.app.route('/api/get_picture', methods=['GET'])
        def get_picture():
            path = os.path.join("pictures", "galaxy.png")
            self.galaxy.create_picture(path)
            return send_file(path, mimetype='image/png')

        @self.app.route('/api/star/<int:star_id>', methods=['GET'])
        def get_star(id):
            star = self.galaxy.stars[int(id)]
            return jsonify(star.to_dict())

        @self.app.route('/api/star', methods=['POST'])
        def add_star():
            star_data = request.get_json()
            x_coord = star_data.get('x')
            y_coord = star_data.get('y')

            if x_coord is None or y_coord is None:
                return jsonify({'error': 'X or Y coordinate is missing from the data'}), 400

            star = self.galaxy.add_star(x_coord, y_coord)
            return jsonify(star.to_dict())

        @self.app.route('/api/star/<int:star_id>', methods=['PUT'])
        def update_star(star_id):
            star_data = request.get_json()
            id_ = star_data.get('id_')
            x_coord = star_data.get('x')
            y_coord = star_data.get('y')

            if any(i == None for i in (id_, x_coord, y_coord, id_)):
                return jsonify({'error': 'ID, X and/or Y coordinate is missing from the data'}), 400

            star = self.galaxy.get_star(id_)
            if star == None:
                return jsonify({'error': 'Star not found'}), 404
            
            star.update(x, y)
            return jsonify({'message': 'Star updated successfully'}), 200
