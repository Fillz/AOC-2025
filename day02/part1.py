lines = open(0).read().splitlines()[0].split(",")

def is_repeating(input):
  if len(input) % 2 == 1:
    return False
  left = input[0 : int(len(input) / 2)]
  right = input[int(len(input) / 2): len(input)]
  return left == right

res = 0
for line in lines:
  start, end = line.split("-")
  for i in range(int(start), int(end) + 1):
    if is_repeating(str(i)):
      res += i

print(res)