import pytest

from .jsonify import jsonify


@pytest.mark.order(1)
def test_jsonify(app):
    app.debug = False
    with app.app_context():
        result = jsonify()
    assert "message" not in result[0]["status"]
    app.debug = True
    with app.app_context():
        result = jsonify()
    assert type(result) is tuple
    assert len(result) == 3
    assert type(result[0]) is dict
    assert type(result[1]) is int
    assert type(result[2]) is dict
    assert "output" in result[0]
    assert "status" in result[0]
    assert "metadata" in result[0]
    assert "code" in result[0]["status"]
    assert "message" in result[0]["status"]
    assert result[0]["status"]["code"] == 100
    assert result[0]["status"]["message"] == "ok"
    assert result[1] == 200
    assert result[2] == {}
