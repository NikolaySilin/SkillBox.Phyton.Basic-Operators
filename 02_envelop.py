# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9

# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6   # - влезла
# paper_x, paper_y = 3, 4   # - влезла
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

approach = "Бумага влезла в конверт"
does_not_approach = "Бумага не поместилась в конверт"

if envelop_x > paper_x:
    if envelop_y > paper_y:
        print(approach)
    elif envelop_y < paper_y:
        print(does_not_approach)
elif envelop_x < paper_x:
    print(does_not_approach)

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2    # - Не влез
# brick_x, brick_y, brick_z = 11, 2, 10    # - Не влез
# brick_x, brick_y, brick_z = 10, 11, 2    # - Не влез
# brick_x, brick_y, brick_z = 10, 2, 11    # - Не влез
# brick_x, brick_y, brick_z = 2, 10, 11    # - Не влез
# brick_x, brick_y, brick_z = 2, 11, 10    # - Не влез
# brick_x, brick_y, brick_z = 3, 5, 6    # - Влез
# brick_x, brick_y, brick_z = 3, 6, 5    # - Влез
# brick_x, brick_y, brick_z = 6, 3, 5    # - Влез
# brick_x, brick_y, brick_z = 6, 5, 3    # - Влез
# brick_x, brick_y, brick_z = 5, 6, 3    # - Влез
# brick_x, brick_y, brick_z = 5, 3, 6    # - Влез
# brick_x, brick_y, brick_z = 11, 3, 6    # - Влез
# brick_x, brick_y, brick_z = 11, 6, 3    # - Влез
# brick_x, brick_y, brick_z = 6, 11, 3    # - Влез
# brick_x, brick_y, brick_z = 6, 3, 11    # - Влез
# brick_x, brick_y, brick_z = 3, 6, 11    # - Влез
brick_x, brick_y, brick_z = 3, 11, 6    # - Влез
# (просто раскоментировать нужную строку и проверить свой код)

approach_brick = "Кирпич влез в отверстие"
does_not_approach_brick = "Кирпич не влез в отверстие"

if hole_x > brick_x:
    if hole_y > brick_y:
        print(approach_brick)
    elif hole_y > brick_z:
        print(approach_brick)
    else:
        print(does_not_approach_brick)
elif hole_x < brick_x:
    if hole_y > brick_y:
        if hole_y > brick_z:
           print(approach_brick)
        else:
            print(does_not_approach_brick)
    else:
        print(does_not_approach_brick)

