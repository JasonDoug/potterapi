from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_providers():
    response = client.get("/providers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_provider():
    response = client.get("/providers/openrouter")
    assert response.status_code == 200
    assert response.json()["id"] == "openrouter"


def test_get_provider_not_found():
    response = client.get("/providers/non-existent-provider")
    assert response.status_code == 404


def test_list_capabilities():
    response = client.get("/providers/openrouter/capabilities")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_capabilities_provider_not_found():
    response = client.get("/providers/non-existent-provider/capabilities")
    assert response.status_code == 404
