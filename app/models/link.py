class Link(db.models):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Colun(db.String, unique=True, nullable=False)
    count = db.Colun(db.Integer, nullable=False, default=3)
    status = db.Colun(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    