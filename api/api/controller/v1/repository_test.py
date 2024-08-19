import pytest

from api.util import uuidgen
from api.view.v1 import api_bp

API_URL_PREFIX = api_bp.url_prefix
API_REQUEST_HEADERS = {"Content-Type": "application/json"}


@pytest.mark.order(1000)
def test_get_repositories_apiv1(client):
    response = client.get(
        f"{API_URL_PREFIX}/repositories",
        headers=API_REQUEST_HEADERS,
    )
    result = response.get_json()
    assert response.status_code == 200
    assert result["status"]["code"] == 100
    assert result["status"]["message"] == "ok"
    assert len(result["output"]) == 1


@pytest.mark.parametrize(
    ["repository_id", "status", "code"],
    (["random", 404, 105], ["storage:test", 200, 100]),
)
@pytest.mark.order(1000)
def test_get_repository_apiv1(storage, client, repository_id, status, code):
    if repository_id == "random":
        repository_id = uuidgen()
    if repository_id.startswith("storage:") is True:
        repository_id = storage.get(repository_id.split(":")[1])
    response = client.get(
        f"{API_URL_PREFIX}/repositories/{repository_id}",
        headers=API_REQUEST_HEADERS,
    )
    result = response.get_json()
    assert response.status_code == status
    assert result["status"]["code"] == code
