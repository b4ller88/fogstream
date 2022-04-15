import _io


def goods_info(file_name: str) -> dict:
    '''Gets info about goods from file.

    :param file_name:
    :return: dict: Goods info in dictionary
    '''

    minimum, maximum = 9999, 0
    num_of_goods = 0
    price_sum = 0
    expensive_goods = set()

    result = {}

    with open(file_name, 'r', encoding='utf-8') as work_file:
        for product in work_file:
            new_product = product.split(':')
            price = int(new_product[1])
            if price < minimum:
                minimum = price
            elif price > maximum:
                maximum = price
            num_of_goods += 1
            price_sum += price
            if price > 100:
                expensive_goods.add(new_product[0])

    result['min_price'] = minimum
    result['max_price'] = maximum
    result['mean_price'] = round(price_sum / num_of_goods, 2)
    result['goods_count'] = num_of_goods
    result['expensive_goods'] = expensive_goods

    return result


def nice_print(info_dict: dict):
    print(f'Минимальная цена: {info_dict["min_price"]}\nМаксимальная цена: {info_dict["min_price"]}\n'
          f'Средняя цена: {info_dict["mean_price"]}\nКоличество продуктов: {info_dict["goods_count"]}\n\n'
          f'Список самых дорогих товаров:')
    for i in info_dict["expensive_goods"]:
        print(f'- {i}')


nice_print(goods_info('goods.txt'))