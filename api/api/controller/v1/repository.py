from api.model import Repository
from api.util import jsonify


class RepositoryController:
    def get_repositories():
        return jsonify(status=501, code=101)

    def get_repository(repository_id):
        return jsonify(status=501, code=101)

    def create_repository():
        return jsonify(status=501, code=101)

    def update_repository(repository_id):
        return jsonify(status=501, code=101)

    def delete_repository(self, repository_id):
        return jsonify(status=501, code=101)
