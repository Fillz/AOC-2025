parts = open(0).read().split("\n\n")

class Space:
  def __init__(self, width, height, shapes_amounts):
    self.width = width
    self.height = height
    self.shapes_amounts = shapes_amounts

def count(str):
  res = 0
  for c in list(str):
    if c == "#":
      res += 1
  return res

shape_sizes = dict()
for i in range(0, len(parts) - 1):
  amount = 0
  for row in parts[i].split("\n"):
    amount += count(row)
  shape_sizes[i] = amount

spaces = []
for row in parts[-1].split("\n"):
  spaces.append(Space(int(row.split("x")[0]), int(row.split("x")[1].split(":")[0]), [int(x) for x in row.split(": ")[1].split(" ")]))

total = 0
for space in spaces:
  space_size = space.width * space.height
  present_total_space = 0
  for i in range(0, len(space.shapes_amounts)):
    shape_amount = space.shapes_amounts[i]
    present_total_space += shape_sizes[i] * shape_amount
  if present_total_space <= space_size:
    total += 1
print(total)