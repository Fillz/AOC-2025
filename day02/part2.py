lines = open(0).read().splitlines()[0].split(",")

def is_repeating_digits(input, repeating_length):
  if len(input) % repeating_length != 0:
    return False
  i = 0
  while i <= len(input) - repeating_length * 2:
    left = input[i : i + repeating_length]
    right = input[i + repeating_length : i + repeating_length * 2]
    if left != right:
      return False
    i += repeating_length
  return True

def is_repeating(input):
  for i in range(1, int(len(input)/2) + 1):
    if is_repeating_digits(input, i):
      return True
  return False

res = 0
for line in lines:
  start, end = line.split("-")
  for i in range(int(start), int(end) + 1):
    if is_repeating(str(i)):
      res += i

print(res)