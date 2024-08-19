import pytest

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
