import copy
lines = open(0).read().splitlines()

class Device:
  def __init__(self, name):
    self.outputs = []
    self.name = name

devices = dict()
for line in lines:
  device_name = line.split(":")[0]
  devices[device_name] = Device(device_name)
devices["out"] = Device("out")
for line in lines:
  device = devices[line.split(":")[0]]
  other_devices_names = line.split(": ")[1].split(" ")
  for other_device_name in other_devices_names:
    device.outputs.append(devices[other_device_name])

paths_found_to_out_from_device = dict()

def get_paths_to_out(current_device, visited_devices):
  if current_device.name == "out":
    if visited_devices.get("dac") and visited_devices.get("fft"):
      return 1
    else:
      return 0
  
  visited_devices[current_device.name] = True
  important_devices_in_visited = []
  if visited_devices.get("dac"):
    important_devices_in_visited.append("dac")
  if visited_devices.get("fft"):
    important_devices_in_visited.append("fft")

  paths_to_out = 0
  for output_device in current_device.outputs:
    current_state_tuple = tuple(important_devices_in_visited + [output_device.name])
    if paths_found_to_out_from_device.get(current_state_tuple) != None:
      paths_to_out += paths_found_to_out_from_device[current_state_tuple]
      continue

    paths_found = get_paths_to_out(output_device, copy.deepcopy(visited_devices))
    paths_found_to_out_from_device[current_state_tuple] = paths_found
    paths_to_out += paths_found

  return paths_to_out

print(get_paths_to_out(devices["svr"], dict()))