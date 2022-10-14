from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    3/0
    return redirect(url_for('question._list'))
