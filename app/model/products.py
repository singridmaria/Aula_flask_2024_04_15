from app import db

class Products(db.model):
    __tablename__ = 'products'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Columns(db.Integer, primary_key=True)
    name = db.Columns(db.String(255))
    price = db.Columns(db.Float)