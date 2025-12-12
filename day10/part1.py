lines = open(0).read().splitlines()

class Button:
  def __init__(self, light_triggers):
    self.light_triggers = light_triggers

class Machine:
  def __init__(self, sought_lights, buttons):
    self.sought_lights = sought_lights
    self.buttons = buttons

machines = []
for line in lines:
  lights = line.split("]")[0][1:]
  buttons_string = line.split("] ")[1].split(" {")[0]
  buttons = []
  for button_string in buttons_string.split(" "):
    buttons.append(Button([ int(x) for x in button_string[1:-1].split(",")]))
  machines.append(Machine(lights, buttons))

class ButtonSequence:
  def __init__(self, current_lights, pressed_buttons_list):
    self.current_lights = current_lights
    self.pressed_buttons_list = pressed_buttons_list

def replace_char_in_string(string, index, char):
  char_list = list(string)
  char_list[index] = char
  return "".join(char_list)

def press_button(button, current_lights):
  new_current_lights = current_lights
  for i in button.light_triggers:
    if new_current_lights[i] == '#':
      new_current_lights = replace_char_in_string(new_current_lights, i, '.')
    else:
      new_current_lights = replace_char_in_string(new_current_lights, i, '#')
  return new_current_lights
  
def process_sequences(button_sequences, sought_lights, buttons):
  already_processed_button_sequences = dict()
  while True:
    button_sequence = button_sequences.pop(0)
    if button_sequence.current_lights == sought_lights:
      return sum(button_sequence.pressed_buttons_list)
    
    for i in range(0, len(buttons)):      
      button = buttons[i]
      current_lights = press_button(button, button_sequence.current_lights)
      new_pressed_buttons_list = button_sequence.pressed_buttons_list.copy()
      new_pressed_buttons_list[i] += 1
      if already_processed_button_sequences.get(tuple(new_pressed_buttons_list)):
        continue
      button_sequences.append(ButtonSequence(current_lights, new_pressed_buttons_list))
      already_processed_button_sequences[tuple(new_pressed_buttons_list)] = True

res = 0
for machine in machines:
  current_lights = machine.sought_lights.replace("#", ".")
  buttons = machine.buttons
  initial_pressed_buttons_list = [0 for i in buttons]
  button_sequences = [ButtonSequence(current_lights, initial_pressed_buttons_list)]
  button_presses = process_sequences(button_sequences, machine.sought_lights, buttons)
  res += button_presses
print(res)