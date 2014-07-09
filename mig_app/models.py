from mig_app import db

class Foo(db.Model):

    __tablename__ = 'foo'

    id = db.Column(db.Integer, primary_key=True)
    fooname = db.Column(db.String(140), unique=True)
    email = db.Column(db.String(150))

    def __init__(self, fooname):
        self.fooname = fooname

    def __repr__(self):
        return '<Foo %r>' % self.fooname
