import timm
import torch as th
import typing as tp
import numpy as np
import cv2


MAX_UINT8 = 255


def preprocess_image(image: np.ndarray, target_image_size: tp.Tuple[int, int]) -> th.Tensor:
    """Препроцессинг имаджнетом.

    :param image: RGB изображение;
    :param target_image_size: целевой размер изображения;
    :return: батч с одним изображением.
    """
    image = image.astype(np.float32)
    image = cv2.resize(image, target_image_size) / MAX_UINT8
    image = np.transpose(image, (2, 0, 1))
    image -= np.array([0.485, 0.456, 0.406])[:, None, None]
    image /= np.array([0.229, 0.224, 0.225])[:, None, None]
    return th.from_numpy(image)[None]


class Model:
    """
    Класс для сохранения и получения объектов
    """

    def __init__(self, config: dict):
        self.path = config['path']
        self.device = config['device']
        self.class_names = np.array(config['class_names'])
        self.model_kwargs = config['model_kwargs']
        self.threshold = config['threshold']
        state_dict = th.load(
            self.path, map_location=th.device(self.device),
        )
        self.model = timm.create_model(
            num_classes=len(self.class_names),
            **self.model_kwargs,
        )
        self.model.load_state_dict(state_dict)
        self.model.eval()

    def predict(self, image) -> tp.List[str]:
        img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
        batch = preprocess_image(img, (MAX_UINT8, MAX_UINT8))
        with th.no_grad():
            prediction = (
                self.model(batch).
                sigmoid().
                squeeze().
                detach().
                cpu().
                numpy()
            )
        return self.class_names[self.threshold < prediction].tolist()

    def predict_proba(self, image) -> tp.List[str]:
        img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
        batch = preprocess_image(img, (MAX_UINT8, MAX_UINT8))
        with th.no_grad():
            prediction = (
                self.
                model(batch).
                sigmoid().
                squeeze().
                detach().
                cpu().
                tolist()
            )
        return dict(zip(self.class_names, prediction))

    def get_classes(self) -> tp.List[str]:
        return self.class_names.tolist()
