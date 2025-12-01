lines = open(0).read().splitlines()

current = 50
zero_count = 0

for line in lines:
  dir = line[0]
  val = int(line[1:])

  if dir == 'R' and current + val > 99:
    zero_count += int((current + val) / 100)
  if dir == 'L' and current - val < 1:
    zero_count += int(abs(current - val) / 100) + 1
    if current == 0:
      zero_count -= 1

  current = current + val if dir == 'R' else current - val
  current = current % 100

print(zero_count)