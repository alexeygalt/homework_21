from courier import Courier
from exceptions import BaseError
from request import Request
from shop import Shop
from store import Store

store = Store(items={
    "печеньки": 5,
    "конфеты": 5,
    "цветы": 5
})

shop = Shop(items={
    "печеньки": 2,
    "конфеты": 2,
    "цветы": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print('\nДобрый день\n')

    while True:

        # Вывод всех товаров
        for storage in storages:
            print()
            print(f"В {storage} хранится:")

            for key, value in storages[storage].get_items().items():
                print(key, value)

        # получаем пользовательский ввод
        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('stop', 'стоп'):
            break

        # создаем запрос на основе ввода
        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        # перемещаем товары
        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            courier.move()
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
