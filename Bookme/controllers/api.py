from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required
from flask.ext.restful import Api, Resource

from Bookme import cache
from Bookme.forms import LoginForm
from Bookme.models import User

api = Blueprint('api', __name__)
apis = Api(api)

class ReadListAPI(Resource):
    def get(self):
        return {'ta' : 'da'}

    def post(self):
        pass

class ReadAPI(Resource):
    def get(self, id):
        return {'ta' : 'da'}

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint = 'tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint = 'task')
