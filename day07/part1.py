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

split_amount = 0
beam_visited = dict()

def calculate_beam(x, y):
  global split_amount
  if y == map_height or beam_visited.get((x, y)):
    return
  beam_visited[(x, y)] = True

  current = map_get(x, y)
  if current == '.':
    calculate_beam(x, y + 1)
  if current == '^':
    calculate_beam(x - 1, y)
    calculate_beam(x + 1, y)
    split_amount += 1

calculate_beam(start_x, 1)
print(split_amount)