from flask import Blueprint

bp_user = Blueprint('user', __name__)


@bp_user.route('/')
def index():
    return ' '