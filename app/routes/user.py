from flask import Blueprint


bp_user = Blueprint('user', __name__)


@bp_user.route('/')
def reg_user():
    new_user = User('valera666', '123', 'a@1', '3', True, )
    return 'user created'
