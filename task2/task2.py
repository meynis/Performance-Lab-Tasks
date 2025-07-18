import sys
import math

def read_circle_data(filename):
    """Читает данные окружности из файла"""
    with open(filename, 'r') as f:
        center_x, center_y = map(float, f.readline().split())
        radius = float(f.readline().strip())
    return center_x, center_y, radius

def read_points_data(filename):
    """Читает координаты точек из файла"""
    points = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

def point_position(px, py, cx, cy, radius):
    """
    Определяет положение точки относительно окружности
    0 - на окружности
    1 - внутри
    2 - снаружи
    """
    distance_squared = (px - cx) ** 2 + (py - cy) ** 2
    radius_squared = radius ** 2
    
    if abs(distance_squared - radius_squared) < 1e-9:
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python task2.py <circle_file> <points_file>")
        sys.exit(1)
    
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    cx, cy, radius = read_circle_data(circle_file)
    
    points = read_points_data(points_file)
    
    for px, py in points:
        position = point_position(px, py, cx, cy, radius)
        print(position)