from mig_app import app, db
from models import Foo

@app.route('/')
def index():
    return "this is the index"

@app.route('/query')
def query_all():
    result = Foo.query.filter_by(id=1).first()
    return result.fooname
