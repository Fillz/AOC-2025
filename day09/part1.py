lines = open(0).read().splitlines()

class Coord:
  def __init__(self, x, y):
    self.x = x
    self.y = y

coords = []
for line in lines:
  coords.append(Coord(int(line.split(",")[0]), int(line.split(",")[1])))

highest_area = -1
for i in range(0, len(coords)):
  for j in range(i + 1, len(coords)):
    if i == j:
      continue
    area = (abs(coords[j].x - coords[i].x) + 1) * (abs(coords[j].y - coords[i].y) + 1)
    if area > highest_area:
      highest_area = area
print(highest_area)