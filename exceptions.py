class BaseError(Exception):
    message = "Some kind of error"


class NotEnoughSpace(BaseError):
    message = 'Not enough storage space'


class NotEnoughProduct(BaseError):
    message = 'Not enough goods in stock'


class TooManyDifferentProducts(BaseError):
    message = 'Too many different products'


class InvalidRequest(BaseError):
    message = 'Request is not valid'


class InvalidStorageName(BaseError):
    message = 'StorageName is not valid'
