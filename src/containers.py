from dependency_injector import containers, providers
from src.services import Model


class AppContainer(containers.DeclarativeContainer):
    """
    Класс DI контейнера
    """
    config = providers.Configuration()
    model = providers.Singleton(
        Model, config.model,
    )
