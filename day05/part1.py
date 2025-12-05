lines = open(0).read().splitlines()

class Range:
  def __init__(self, start, end):
    self.start = start
    self.end = end

ranges = []
ingredients = []

i = 0
while i < len(lines):
  if lines[i] == "":
    i += 1
    break
  start, end = lines[i].split("-")
  ranges.append(Range(int(start), int(end)))
  i += 1
while i < len(lines):
  ingredients.append(int(lines[i]))
  i += 1

def is_fresh(ingredient):
  for range in ranges:
    if ingredient >= range.start and ingredient <= range.end:
      return True
  return False

count = 0
for ingredient in ingredients:
  if is_fresh(ingredient):
    count += 1

print(count)