lines = open(0).read().splitlines()

current = 50
zero_count = 0

for line in lines:
  dir = line[0]
  val = int(line[1:])
  current = current + val if dir == 'R' else current - val
  current = current % 100
  if current == 0:
    zero_count += 1

print(zero_count)