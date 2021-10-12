# -*- coding: utf-8 -*-

import simple_draw as sd

sd.background_color = (0, 0, 0)
sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# point = sd.get_point(300, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, width=2)

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, point_snowflake, step, color):
    radius = 20
    color = sd.random_color()
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color)
        sd.snowflake(center=point_snowflake, color=color, factor_a=0.6, factor_b=0.35, factor_c=60)

# point = sd.get_point(500, 100)

# Нарисовать 10 пузырьков в ряд

# for x in range(100, 1001, 100):
#     point = sd.get_point(x, 300)
#     bubble_one(point=point, step=8)




# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 301, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble_one(point=point, step=8)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    point_snowflake = sd.random_point()
    bubble(point=point, point_snowflake=point_snowflake, step=4, color=sd.random_color())

sd.pause()
