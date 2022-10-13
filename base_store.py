from abstract_storage import Storage
from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStore(Storage):
    def __init__(self, items: dict[str, int], capacity):
        super().__init__(items, capacity)

    def get_free_space(self) -> int:
        occupied_space = 0

        for value in self.items.values():
            occupied_space += value

        return self.capacity - occupied_space

    def add(self, name: str, value: int) -> None:
        if self.get_free_space() < value:
            raise NotEnoughSpace

        self.items[name] = self.items.get(name, 0) + value

    def remove(self, name: str, value: int) -> None:
        if name not in self.items or self.items[name] < value:
            raise NotEnoughProduct

        self.items[name] -= value
        if self.items[name] == 0:
            del self.items[name]

    def get_items(self) -> dict:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items)
