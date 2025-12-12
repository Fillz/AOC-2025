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

def get_paths_to_out(current_device):
  if current_device.name == "out":
    return 1
  
  paths_to_out = 0
  for output_device in current_device.outputs:
    paths_to_out += get_paths_to_out(output_device)
  return paths_to_out

print(get_paths_to_out(devices["you"]))