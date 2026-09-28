import pytest

from orders_api.app import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_crear_pedido(client):
    r = client.post("/pedidos", json={"producto": "widget", "cantidad": 3})
    assert r.status_code == 201
    assert r.get_json()["producto"] == "widget"


def test_obtener_pedido_inexistente(client):
    r = client.get("/pedidos/9999")
    assert r.status_code == 404
