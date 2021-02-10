from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

dogs = [
    {"id": 1, "breed": "pembroke-welsh-corgi", "name": "charles"},
    {"id": 2, "breed": "pug", "name": "cheese"},
    {"id": 3, "breed": "dachshund", "name": "ralph"}
]

cats = [
    {"id": 1, "breed": "ragdoll", "name": "mimi"},
    {"id": 2, "breed": "siamese", "name": "mocha"},
    {"id": 3, "breed": "russian-blue", "name": "bean"}
]


class DogList(Resource):
    def get(self):
        return dogs, 200


class Dog(Resource):
    def get(self, dog_id):
        return next(item for item in dogs if item["id"] == dog_id), 200


class CatList(Resource):
    def get(self):
        return cats, 200


class Cat(Resource):
    def get(self, cat_id):
        return next(item for item in cats if item["id"] == cat_id), 200


api.add_resource(DogList, '/dogs')
api.add_resource(Dog, '/dogs/<int:dog_id>')

api.add_resource(CatList, '/cats')
api.add_resource(Cat, '/cats/<int:cat_id>')

if __name__ == '__main__':
    app.run(debug=True)

