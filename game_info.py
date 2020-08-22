from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

@dataclass
class GameData:
    image_url: str
    name: str
    link: str


class GameInformer(ABC):
    @abstractmethod
    def get_free_games(self) -> List[GameData]:
        raise NotImplementedError
