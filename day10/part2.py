import sympy as sp
import math
from itertools import product
from multiprocessing import Pool
from functools import partial

class Button:
  def __init__(self, joltage_triggers):
    self.joltage_triggers = joltage_triggers

class Machine:
  def __init__(self, buttons, sought_joltages):
    self.buttons = buttons
    self.sought_joltages = sought_joltages


def calculate_buttons_pressed(values, sorted_symbols, solution):
  subs = dict(zip(sorted_symbols, values))
  pressed_buttons = [expr.subs(subs) for expr in list(solution)[0]]
  if all(x.q == 1 and x >= 0 for x in pressed_buttons):
    return sum(int(x) for x in pressed_buttons)
  return math.inf

if __name__ == '__main__':
  lines = open(0).read().splitlines()
  machines = []
  for line in lines:
    sought_joltages = [int(x) for x in line.split("{")[1][:-1].split(",")]
    buttons_string = line.split("] ")[1].split(" {")[0]
    buttons = []
    for button_string in buttons_string.split(" "):
      buttons.append(Button([ int(x) for x in button_string[1:-1].split(",")]))
    machines.append(Machine(buttons, sought_joltages))

  total = 0
  with Pool() as p:
    for machine in machines:
      variables_amount = len(machine.buttons)
      variables = sp.symbols(f'x0:{variables_amount}')
      equations_left_side = []
      equations_right_side = machine.sought_joltages
      for i in range(0, len(machine.sought_joltages)):
        equations_left_side.append([])
        for button in machine.buttons:
          if i in button.joltage_triggers:
            equations_left_side[-1].append(1)
          else:
            equations_left_side[-1].append(0)

      solution = sp.linsolve((sp.Matrix(equations_left_side), sp.Matrix(equations_right_side)), variables)
      sorted_symbols = sorted(list(solution.free_symbols), key=lambda s: s.name)

      if len(sorted_symbols) == 1:
        combinations_to_check_per_variable = 1000
      elif len(sorted_symbols) == 2:  
        combinations_to_check_per_variable = 50
      else:
        combinations_to_check_per_variable = 20
      
      values = product(range(combinations_to_check_per_variable), repeat=len(sorted_symbols))
      worker = partial(calculate_buttons_pressed, sorted_symbols=sorted_symbols, solution=solution)
      if combinations_to_check_per_variable > 1:
        total += min(p.imap_unordered(worker, values))
      else:
        total += min(map(worker, values))
  print(total)