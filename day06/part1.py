lines = open(0).read().splitlines()

number_lines = []
for i in range(0, len(lines) - 1):
  number_lines.append([int(x) for x in lines[i].split(" ") if x != ""])
operations = [x for x in lines[-1].split(" ") if x != ""]

total = 0
for i in range(0, len(number_lines[0])):
  op = operations[i]
  res = 0 if op == '+' else 1
  for j in range(0, len(number_lines)):
    if op == '+':
      res += number_lines[j][i]
    elif op == '*':
      res *= number_lines[j][i]
  total += res
print(total)