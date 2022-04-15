from goods_info import Good, Goods

if __name__ == '__main__':
    file_name = input('Введите путь к файлу')
    goods = Goods()
    goods.get_from_file(file_name)
    print(goods)
