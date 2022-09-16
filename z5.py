databade_of_product = dict({"Мишка": ["Плюш", 57, 5],
                            "Мяч": ["Футбольный", 45, 8],
                            "Конструктор": ["Let's go", 80, 15],
                            "Пазл": ["Картон", 15, 20],
                            "Юла": ["Пластмасса", 10, 8],
                            "Машинка": ["Металл", 23, 50],
                            "Меч": ["Алюминий", 62, 70]
                            })
stringName = 'Магазин игрушек'
while True:
    print((stringName))
    stringMenu = ['1.Просмотр описания: название – описание',
                  '2.Просмотр цены: название – цена',
                  '3.Просмотр количества: название – количество',
                  '4.Вся информация',
                  '5.Покупка',
                  '6.До встречи']
    for i in range(len(stringMenu)):
        print((stringMenu[i]))

    answer = int(0)

    while True:
        answer = int(input("Ваш выбор: "))
        if answer < 1 or answer > 6:
            print("Неверный выбор, попробуйте ещё раз")
        else:
            break

    if answer == 1:
        index = 0
        for key in databade_of_product.keys():
            print("%20s : %-14s" % (key, databade_of_product.get(key)[index]))
    elif answer == 2:
        index = 1
        for key in databade_of_product.keys():
            print("%20s : %-3sруб" % (key, databade_of_product.get(key)[index]))
    elif answer == 3:
        index = 2
        for key in databade_of_product.keys():
            print("%20s : %-14s" % (key, databade_of_product.get(key)[index]))
    elif answer == 4:

        for key in databade_of_product.keys():
            print("{:>20} : {:>8} : {:<3}руб : {:<3}".format(key, databade_of_product.get(key)[0],
                                                           databade_of_product.get(key)[1],
                                                           databade_of_product.get(key)[2]))
    elif answer == 5:
        productName = input("Введите название товара, который нужно купить: ")
        if productName in databade_of_product.keys():

            count = int(0)
            while True:
                count = int(input("Введите количесто данного товара, которого нужно купить: "))
                if count < 0 or count > databade_of_product.get(productName)[2]:
                    print("Вы ввели отрицательное число или слишком большое, попробуйте ещё раз")
                else:
                    break

            print("Покупка завершена!")
            print("Вы купили товар %s на сумму %d руб" % (productName, databade_of_product.get(productName)[1] * count))
            old_value = databade_of_product.pop(productName)
            old_value[2] -= count
            if old_value[2] != 0:
                databade_of_product.update({productName: old_value})
        else:
            print("Данный товар не найден...")

    elif answer == 6:
        break
