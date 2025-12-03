lines = open(0).read().splitlines()

def get_highest_number_index_in_bank_subset(bank, start_index, end_index):
  highest = 0
  highest_index = -1
  for i in range(start_index, end_index + 1):
    if int(bank[i]) > highest:
      highest = int(bank[i])
      highest_index = i
  return highest_index

def get_highest_joltage(bank, bateries_amount):
  current_batteries = ""
  i = 0
  while len(current_batteries) != bateries_amount:
    highest_number_index = get_highest_number_index_in_bank_subset(bank, i, len(bank) - bateries_amount + len(current_batteries))
    current_batteries += bank[highest_number_index]
    i = highest_number_index + 1
  return current_batteries

res_p1, res_p2 = (0, 0)
for line in lines:
  res_p1 += int(get_highest_joltage(line, 2))
  res_p2 += int(get_highest_joltage(line, 12))

print("part1: " + str(res_p1))
print("part2: " + str(res_p2))
