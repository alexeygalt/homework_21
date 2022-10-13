from base_store import BaseStore
from exceptions import TooManyDifferentProducts


class Store(BaseStore):
    def __init__(self, items: dict[str, int], capacity=20):
        super().__init__(items, capacity)

    def add(self, name: str, value: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(name, value)
