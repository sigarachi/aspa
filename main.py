import random
import math
import matplotlib.pyplot as plt

def generate_polygon(num_vertices, max_x, max_y):
  """Генерирует случайный многоугольник с заданным количеством вершин."""
  vertices = []
  for _ in range(num_vertices):
    x = random.uniform(0, max_x)
    y = random.uniform(0, max_y)
    vertices.append((x, y))
  return vertices

def generate_point(polygon, max_x, max_y, r):
  """Генерирует случайную точку вне многоугольника."""
  while True:
    x = random.uniform(0, max_x)
    y = random.uniform(0, max_y)
    if not is_point_inside_polygon((x, y), polygon):
      return (x, y)

def is_point_inside_polygon(point, polygon):
  """Проверяет, находится ли точка внутри многоугольника."""
  x, y = point
  n = len(polygon)
  inside = False
  for i in range(n):
    j = (i + 1) % n
    xi, yi = polygon[i]
    xj, yj = polygon[j]
    if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
      inside = not inside
  return inside

def distance_to_polygon(point, polygon, r):
  """Вычисляет расстояние от точки до ближайшей стороны многоугольника."""
  min_distance = float('inf')
  closest_line = None
  for i in range(len(polygon)):
    j = (i + 1) % len(polygon)
    x1, y1 = polygon[i]
    x2, y2 = polygon[j]
    distance = calculate_distance_point_to_line(point, (x1, y1), (x2, y2))
    if distance < min_distance:
      min_distance = distance
      closest_line = ((x1, y1), (x2, y2))
  return min_distance - r, closest_line

def calculate_distance_point_to_line(point, line_start, line_end):
  """Вычисляет расстояние от точки до прямой."""
  x, y = point
  x1, y1 = line_start
  x2, y2 = line_end
  denominator = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / denominator

def main():
  # Параметры
  max_x = 100
  max_y = 100
  num_vertices = 5
  r = 10

  # Генерация многоугольника
  polygon = generate_polygon(num_vertices, max_x, max_y)

  # Генерация точки вне многоугольника
  point = generate_point(polygon, max_x, max_y, r)

  # Вычисление расстояния до ближайшей стороны многоугольника
  distance, closest_line = distance_to_polygon(point, polygon, r)

  # Вывод результатов
  print("Точка:", point)
  print("Многоугольник:", polygon)
  print("Расстояние от точки до ближайшей стороны многоугольника:", distance)

  if distance < 0:
    print("Точка находится внутри окружности с радиусом", r, "относительно многоугольника.")
  else:
    print("Точка находится вне окружности с радиусом", r, "относительно многоугольника.")

  # Рисуем график
  plt.figure(figsize=(8, 6))
  plt.title("Многоугольник, точка и расстояние")

  # Рисуем многоугольник
  x, y = zip(*polygon)
  plt.plot(x, y, "b-", label="Многоугольник")
  plt.fill(x, y, "lightblue", alpha=0.5)

  # Рисуем точку
  plt.scatter(point[0], point[1], s=50, c="red", label="Точка")

  # Рисуем линию от точки до ближайшей стороны
  if closest_line:
    x1, y1 = closest_line[0]
    x2, y2 = closest_line[1]
    plt.plot([point[0], x1], [point[1], y1], "r--", label="Расстояние")

  # Настраиваем график
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.xlim(0, max_x)
  plt.ylim(0, max_y)
  plt.grid(True)
  plt.legend()

  # Отображаем график
  plt.show()

if __name__ == "__main__":
  main()