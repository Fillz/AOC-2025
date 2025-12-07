lines = open(0).read().splitlines()
map = []
for line in lines:
  map.append(list(line))
map_width = len(map[0])
map_height = len(map)

def map_get(x, y):
  return map[y][x]

start_x = -1
for x in range(0, map_width):
  if map_get(x, 0) == 'S':
    start_x = x
    break

timelines_below_splitter = dict()

def calculate_beam(x, y):
  if y == map_height:
    return 1
  if timelines_below_splitter.get((x, y)):
    return timelines_below_splitter[(x, y)]

  current = map_get(x, y)
  if current == '.':
    return calculate_beam(x, y + 1)
  if current == '^':
    sum = calculate_beam(x - 1, y) + calculate_beam(x + 1, y)
    timelines_below_splitter[(x, y)] = sum
    return sum

print(calculate_beam(start_x, 1))