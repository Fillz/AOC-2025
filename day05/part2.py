lines = open(0).read().splitlines()

class Range:
  def __init__(self, start, end):
    self.start = start
    self.end = end

def get_amount_overlapped(range, handled_ranges):
  overlapped = 0
  for handled_range in handled_ranges:
    if range.start >= handled_range.start and range.end <= handled_range.end:
      overlapped += range.end - range.start + 1
      break
    if range.start < handled_range.start and range.end <= handled_range.end and range.end >= handled_range.start:
      overlapped += range.end - handled_range.start + 1
      range.end = handled_range.start - 1
    if range.start >= handled_range.start and range.start <= handled_range.end and range.end > handled_range.end:
      overlapped += handled_range.end - range.start + 1
      range.start = handled_range.end + 1
  return overlapped

def split_range_based_on_handled_ranges(range, handled_ranges):
  for handled_range in handled_ranges:
    if range.start < handled_range.start and range.end > handled_range.end:
      return (Range(range.start, handled_range.start), Range(handled_range.end, range.end))
  return None 

unhandled_ranges = []
i = 0
while i < len(lines):
  if lines[i] == "":
    break
  start, end = lines[i].split("-")
  unhandled_ranges.append(Range(int(start), int(end)))
  i += 1

handled_ranges = []
fresh_ingredients = 0

while len(unhandled_ranges) > 0:
  range = unhandled_ranges.pop(0)
  if len(handled_ranges) == 0:
    handled_ranges.append(range)
    fresh_ingredients += range.end - range.start + 1
    continue
  split_range = split_range_based_on_handled_ranges(range, handled_ranges)
  if split_range:
    unhandled_ranges.append(split_range[0])
    unhandled_ranges.append(split_range[1])
    continue
  fresh_ingredients += range.end - range.start + 1 - get_amount_overlapped(range, handled_ranges)
  handled_ranges.append(range)

print(fresh_ingredients)