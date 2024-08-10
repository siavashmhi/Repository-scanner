from api.object import db
from api.util import now, uuidgen


class Repository(db.Model):
    __tablename__ = "repositories"

    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    owner = db.Column(db.String(256), index=True, nullable=False)
    url = db.Column(db.String(256), index=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=now)
    last_update_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(32), nullable=False, default="NEW")

    def __repr__(self):
        return f"<Repository id='{self.id}' owner='{self.owner}' url='{self.url}'>"
