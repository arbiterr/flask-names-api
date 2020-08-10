from config import db, ma


class Newborn(db.Model):
    __tablename__ = 'newborn'
    newborn_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, index=True)
    name = db.Column(db.String(32), index=True)
    number = db.Column(db.Integer)
    position = db.Column(db.Integer)



class NewbornSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Newborn
        load_instance = True
