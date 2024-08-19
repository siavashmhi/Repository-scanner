from flask import request

from api.model import Repository
from api.object import db
from api.schema.v1 import RepositorySchema
from api.util import jsonify, now


class RepositoryController:
    def get_repositories():
        """
        get repositories collection from database,
        and create repositories schema.
        """
        try:
            repositories = Repository.query.all()
        except:
            return jsonify(status=500, code=102)

        try:
            repositories_schema = RepositorySchema(many=True)
        except:
            return jsonify(status=500, code=103)
        return jsonify(repositories_schema.dump(repositories))

    def get_repository(repository_id):
        """
        get one repository with repository_id,
        and create repository schema.
        """
        try:
            # repository = Repository.query.get(repository_id) ## this is deprecated.
            repository = db.session.get(Repository, repository_id)
        except:
            return jsonify(status=500, code=102)
        if repository is None:
            return jsonify(status=404, code=105)

        try:
            repository_schema = RepositorySchema()
        except:
            return jsonify(status=500, code=103)

        return jsonify(repository_schema.dump(repository))

    def create_repository():
        """
        first one create repository schema,
        and after that get user request for create new repository.
        """
        try:
            repository_schema = RepositorySchema(only=["url"])
        except:
            return jsonify(status=500, code=103)

        try:
            request_data = repository_schema.load(request.get_json())
        except:
            return jsonify(status=500, code=104)

        repository = Repository(
            owner="TBC",
            url=request_data["url"],
        )
        db.session.add(repository)

        try:
            # insert data to databse
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)

        try:
            repository_schema = RepositorySchema()
        except:
            return jsonify(status=500, code=103)

        return jsonify(repository_schema.dump(repository), status=201)

    def update_repository(repository_id):
        """
        get one repository with repository_id,
        and after that update status and last_update_at item.
        """
        try:
            repository = Repository.query.get(repository_id)
        except:
            return jsonify(status=500, code=102)
        if repository is None:
            return jsonify(status=500, code=105)

        try:
            repository_schema = RepositorySchema(only=["status"])
        except:
            return jsonify(status=500, code=103)

        try:
            request_data = repository_schema.load(request.get_json())
        except:
            return jsonify(status=500, code=104)
        repository.status = request_data["status"]
        repository.last_update_at = now()
        try:
            # insert data to databse
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)

        try:
            repository_schema = RepositorySchema()
        except:
            return jsonify(status=500, code=103)
        return jsonify(repository_schema.dump(repository))

    def delete_repository(repository_id):
        """
        get one repository with repository_id,
        and delete that repository if status of repository not in status_codes list.
        """

        status_codes = ["ACCEPTED", "PROCESSING"]

        try:
            repository = Repository.query.get(repository_id)
        except:
            return jsonify(status=500, code=102)
        if repository is None:
            return jsonify(status=500, code=105)
        if repository.status in status_codes:
            return jsonify(status=412, code=106)

        db.session.delete(repository)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        return jsonify()
