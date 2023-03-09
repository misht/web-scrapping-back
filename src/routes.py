from flask import Blueprint
from src.controllers.user import UserController

user_bp = Blueprint('user', __name__)
user_controller = UserController()

@user_bp.route('/users')
def get_users():
    return user_controller.get_users()