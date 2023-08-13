from copy import deepcopy

import numpy as np

from src.containers import AppContainer


def test_predicts_not_fail(app_container: AppContainer, sample_image_np: np.ndarray):
    model = app_container.model()
    model.predict(sample_image_np)
    model.predict_proba(sample_image_np)


def test_prob_less_or_equal_to_one(app_container: AppContainer, sample_image_np: np.ndarray):
    model = app_container.model()
    genre2prob = model.predict_proba(sample_image_np)
    for prob in genre2prob.values():
        assert prob <= 1
        assert prob >= 0


def test_predict_dont_mutate_initial_image(app_container: AppContainer, sample_image_np: np.ndarray):
    initial_image = deepcopy(sample_image_np)
    model = app_container.model()
    # breakpoint()
    model.predict(sample_image_np)
    assert np.allclose(initial_image, sample_image_np)
