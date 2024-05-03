import cv2
import numpy as np

# Задаем размеры изображения
width, height = 500, 500

arc = np.zeros((500, 500, 3), dtype='uint8')

# Задаем начальное и конечное значение яркости
start_intensity = 0
end_intensity = 255

# Создаем градиент с помощью линейной интерполяции
for i in range(width):
    intensity = int(start_intensity + (end_intensity - start_intensity) * i / width)
    arc[:, i] = intensity

cv2.circle(arc, (200, 200), 150, (255, 255, 255), 3)

major_axis = 23
minor_axis = 24
major_axis_big = round(major_axis * 2.1)
minor_axis_big = round(minor_axis * 2.1)


# Параметры эллипса
center1 = (200, 200)
axes1 = (major_axis, minor_axis)
center2 = (200, 200)
axes2 = (major_axis_big, minor_axis_big)
angle = 0
start_angle = 0
end_angle = 180

# Рисуем дуги эллипса
cv2.ellipse(arc, center1, axes1, angle, start_angle, end_angle, (65, 252, 3), 3)
cv2.ellipse(arc, center2, axes2, angle, start_angle, end_angle, (65, 252, 3), 3)

# Вычисляем координаты конечных точек малой дуги
start_point1 = (
    int(center1[0] + axes1[0] * np.cos(np.radians(start_angle))),
    int(center1[1] - axes1[1] * np.sin(np.radians(start_angle)))
)
end_point1 = (
    int(center1[0] + axes1[0] * np.cos(np.radians(end_angle))),
    int(center1[1] - axes1[1] * np.sin(np.radians(end_angle)))
)

# Рисуем прямые линии от конечных точек малой дуги
cv2.line(arc, start_point1, (start_point1[0], 152), (255, 0, 0), 3)
cv2.line(arc, end_point1, (end_point1[0], 152),(255, 0, 0), 3)

# Вычисляем координаты конечных точек большой дуги
start_point2 = (
    int(center2[0] + axes2[0] * np.cos(np.radians(start_angle))),
    int(center2[1] - axes2[1] * np.sin(np.radians(start_angle)))
)
end_point2 = (
    int(center2[0] + axes2[0] * np.cos(np.radians(end_angle))),
    int(center2[1] - axes2[1] * np.sin(np.radians(end_angle)))
)

# Рисуем прямые линии от конечных точек большой дуги
cv2.line(arc, start_point2, (start_point2[0], 152), (255, 0, 0), 3)
cv2.line(arc, end_point2, (end_point2[0], 152),(255, 0, 0), 3)

# Рисуем горизонтальные линии
cv2.line(arc, (start_point2[0], 152), (start_point1[0], 152), (0, 0, 255), 3)
cv2.line(arc, (end_point2[0], 152), (end_point1[0], 152), (0, 0, 255), 3)


cv2.imshow('arc', arc)
cv2.waitKey(0)
cv2.destroyAllWindows()


