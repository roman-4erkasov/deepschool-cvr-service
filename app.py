import uvicorn
from fastapi import FastAPI
from omegaconf import OmegaConf
from src.router import router
from src import routes
from src.containers import AppContainer

# from src.containers.containers import AppContainer
# from src.routes.routers import wiki_router
# from src.routes import wiki as wiki_routes


def set_routers(app: FastAPI):
    app.include_router(
        router, prefix='/router', tags=['planet']
    )


def create_app() -> FastAPI:
    # # Инициализация DI контейнера
    container = AppContainer()
    # # Инициализация конфига
    cfg = OmegaConf.load('src/config.yml')
    # # Прокидываем конфиг в наш контейнер
    container.config.from_dict(cfg)
    # # Говорим контейнеру, в каких модулях он будет внедряться
    container.wire([routes])
    app = FastAPI()
    # цепляем роутер к нашему приложению
    set_routers(app)
    return app


app = create_app()

# @app.get("/")
# def health():
#     return {"status": "OK"}

if __name__ == '__main__':
    uvicorn.run(app, port=1234, host='0.0.0.0')
