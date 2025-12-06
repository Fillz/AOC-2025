lines = open(0).read().splitlines()
map = []
for line in lines:
  map.append(list(line))
map_width = len(map[0])
map_height = len(map)

def map_get(x, y):
  return map[y][x]

def get_number_width(from_x):
  res = 0
  for x in range(from_x + 1, map_width):
    if map_get(x, map_height - 1) != ' ':
      return res
    res += 1
  return res + 1

def calculate(x_start, number_width, op):
  res = 0 if op == '+' else 1
  for x in range(x_start + number_width - 1, x_start - 1, -1):
    number = ""
    for y in range(0, map_height - 1):
      number += map_get(x, y)
    if op == '+':
      res += int(number)
    elif op == '*':
      res *= int(number)
  return res

res = 0
x = 0
while x < map_width:
  number_width = get_number_width(x)
  op = map_get(x, map_height - 1)
  res += calculate(x, number_width, op)
  x += number_width + 1
print(res)