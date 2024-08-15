from api.model import Repository
from api.object import ma


class RepositorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Repository

    id = ma.auto_field(dump_only=True)
    owner = ma.auto_field(dump_only=True)
    url = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)
    last_update_at = ma.auto_field(dump_only=True)
    status = ma.auto_field()
