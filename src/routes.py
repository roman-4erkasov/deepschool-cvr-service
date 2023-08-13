from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from src.services import Model
from fastapi import File

from src.router import router
from src.containers import AppContainer
import typing as tp


@router.get('/health_check')
@inject
def health_check():
    return {'status': 'OK'}


@router.post('/predict')
@inject
def predict(
    image: bytes = File(),
    service: Model = Depends(Provide[AppContainer.model]),
) -> tp.List[str]:
    return service.predict(image)


@router.post('/predict_proba')
@inject
def predict_proba(
    image: bytes = File(),
    service: Model = Depends(Provide[AppContainer.model]),
) -> tp.Dict[str, str]:
    return service.predict_proba(image)


@router.get('/classes')
@inject
def get_classes(
    service: Model = Depends(Provide[AppContainer.model]),
) -> tp.List[str]:
    return service.get_classes()
