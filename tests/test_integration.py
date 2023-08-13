from fastapi.testclient import TestClient
from http import HTTPStatus


def test_genres_list(client: TestClient):
    response = client.get('/router/classes')
    assert response.status_code == HTTPStatus.OK

    genres = response.json()#['classes']

    assert isinstance(genres, list)


def test_predict(client: TestClient, sample_image_bytes: bytes):
    files = {
        'image': sample_image_bytes,
    }
    response = client.post('/router/predict', files=files)

    assert response.status_code == HTTPStatus.OK

    predicted_genres = response.json()

    assert isinstance(predicted_genres, list)


def test_predict_proba(client: TestClient, sample_image_bytes: bytes):
    files = {
        'image': sample_image_bytes,
    }
    response = client.post('/router/predict_proba', files=files)

    assert response.status_code == HTTPStatus.OK

    genre2prob = response.json()

    for genre_prob in genre2prob.values():
        assert genre_prob <= 1
        assert genre_prob >= 0
