import os.path # noqa: WPS301

import cv2
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from omegaconf import OmegaConf


from src.containers import AppContainer
from src import routes
from app import set_routers

TESTS_DIR = os.path.dirname(__file__)
PATH_IMG = os.path.join(TESTS_DIR, 'images', 'train_39146.jpg')

@pytest.fixture(scope='session')
def sample_image_bytes():
    f = open(os.path.join(PATH_IMG),'rb')  # noqa: WPS515
    try:
        yield f.read()
    finally:
        f.close()


@pytest.fixture
def sample_image_np():
    img = cv2.imread(PATH_IMG)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_str = cv2.imencode('.jpg', img)[1]
    return img_str


@pytest.fixture(scope='session')
def app_config():
    return OmegaConf.load(os.path.join(TESTS_DIR, 'test_config.yml'))


@pytest.fixture
def app_container(app_config):
    container = AppContainer()
    container.config.from_dict(app_config)
    return container


@pytest.fixture
def wired_app_container(app_config):
    container = AppContainer()
    container.config.from_dict(app_config)
    container.wire([routes])
    yield container
    container.unwire()


@pytest.fixture
def test_app(wired_app_container):
    app = FastAPI()
    set_routers(app)
    return app


@pytest.fixture
def client(test_app):
    return TestClient(test_app)
