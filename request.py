from abstract_storage import Storage
from exceptions import InvalidRequest, InvalidStorageName


class Request:
    def __init__(self, request: str, storages: dict[str, Storage]):
        formatted_request = request.lower().split(' ')
        if len(formatted_request) != 7:
            raise InvalidRequest

        self.quantity = int(formatted_request[1])
        self.product = formatted_request[2]
        self.departure = formatted_request[4]
        self.destination = formatted_request[6]

        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName

# Доставить 3 печеньки из склад в магазин
