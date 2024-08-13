from api.model import Repository
from api.schema.v1 import RepositorySchema
from api.util import jsonify


class RepositoryController:
    def get_repositories():
        try:
            repositories = Repository.query.all()
        except:
            return jsonify(status=500, code=102)
        repositories_schema = RepositorySchema(many=True)
        return jsonify(repositories_schema.dump(repositories))

    def get_repository(repository_id): 
        return jsonify(status=501, code=101)

    def create_repository():
        return jsonify(status=501, code=101)

    def update_repository(repository_id):
        return jsonify(status=501, code=101)

    def delete_repository(self, repository_id):
        return jsonify(status=501, code=101)
