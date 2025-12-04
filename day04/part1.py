map = [list(line) for line in open(0).read().splitlines()]
map_width = len(map[0])
map_height = len(map)

def is_paper(y, x):
  if x < 0 or y < 0 or x > map_width - 1 or y > map_height - 1:
    return False
  if map[y][x] == '@':
    return True
  return False

accessible = 0

for y in range(0, map_height):
  for x in range(0, map_width):
    if not is_paper(y, x):
      continue
    adjacents = 0
    for i in range(y - 1, y + 2):
      for j in range(x - 1, x + 2):
        if i == y and j == x:
          continue
        if is_paper(i, j):
          adjacents += 1
    if adjacents < 4:
      accessible += 1

print(accessible)