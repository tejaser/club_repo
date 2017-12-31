from .. import db

club_category_assoc = db.Table('club_category_association', db.Model.metadata,
                               db.Column('club_id', db.Integer,
                                         db.ForeignKey('clubs.id')),
                               db.Column('club_category_id', db.Integer,
                                         db.ForeignKey('club_categories.id')))



class Club(db.model):
    __tablename__ = 'clubs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    description = db.Column(db.Text)
    is_confirmed = db.Column(db.Boolean)
    categories = db.relationship('ClubCategory', secondary=club_category_assoc, backref='clubs')


class ClubCategory(db.model):
    __tablename__ = 'club_categories'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(1000))
