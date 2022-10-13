from abstract_storage import Storage
from request import Request


class Courier:
    def __init__(self, request: Request, storages: dict[str, Storage]):
        self.request = request
        if self.request.departure in storages:
            self.__from = storages[self.request.departure]

        if self.request.destination in storages:
            self.__to = storages[self.request.destination]

    def move(self):
        self.__from.remove(name=self.request.product, value=self.request.quantity)
        print(f'Курьер забрал {self.request.quantity} {self.request.product} из {self.request.departure}')
        self.__to.add(name=self.request.product, value=self.request.quantity)
        print(f'Курьер доставил {self.request.quantity} {self.request.product} в {self.request.destination}')
