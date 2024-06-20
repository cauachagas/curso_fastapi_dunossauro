from http import HTTPStatus

from curso_fastapi_dunossauro.app import app
from fastapi.testclient import TestClient


def test_root_deve_retornar_ok_e_ola_mundo():
    """
    Esta função testa se o endpoint raiz retorna um código de status "OK" e
    uma resposta JSON com a mensagem "Olá Mundo!".
    """

    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}
