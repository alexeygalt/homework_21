from base_store import BaseStore


class Shop(BaseStore):
    def __init__(self, items: dict[str, int], capacity=100):
        super().__init__(items, capacity)
