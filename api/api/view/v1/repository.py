from flask_restful import Resource

from api.controller.v1 import RepositoryController


class RepositoryResource(Resource):
    def get(self, repository_id=None):
        # GET /api/v1/respositories --> list of repositories.
        # GET /api/v1/respositories/<repository_id> --> get one repository.
        if repository_id is None:
            return RepositoryController.get_repositories()
        else:
            return RepositoryController.get_repository(repository_id)

    def post(self):
        # POST /api/v1/respositories --> Create one repository.
        # POST /api/v1/respositories/<repository_id> --> Not allowed.
        return RepositoryController.create_repository()

    def patch(self, repository_id):
        # PATCH /api/v1/respositories --> Not allowed.
        # PATCH /api/v1/respositories/<repository_id> --> Update the repository.
        return RepositoryController.update_repository(repository_id)

    def delete(self, repository_id):
        # DELETE /api/v1/respositories --> Not allowed.
        # DELETE /api/v1/respositories/<repository_id> --> Update the repository.
        return RepositoryController.delete_repository(repository_id)
