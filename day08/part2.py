import math

class JunctionBox:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

class Circuit:
  def __init__(self, junction_boxes = []):
    self.junction_boxes = junction_boxes

  def is_in_circuit(self, junction_box):
    for circuit_box in self.junction_boxes:
      if circuit_box.x == junction_box.x and circuit_box.y == junction_box.y and circuit_box.z == junction_box.z:
        return True
    return False
  
  def size(self):
    return len(self.junction_boxes)

def box_dist(first_box, second_box):
  return math.sqrt((second_box.x - first_box.x) ** 2 + (second_box.y - first_box.y) ** 2 + (second_box.z - first_box.z) ** 2)

def merge_circuits(first_circuit, second_circuit):
  return Circuit(first_circuit.junction_boxes + second_circuit.junction_boxes)


lines = open(0).read().splitlines()
junction_boxes = []
circuits = []

for line in lines:
  x, y, z = [int(x) for x in line.split(",")]
  junction_boxes.append(JunctionBox(x, y, z))

for junction_box in junction_boxes:
  circuits.append(Circuit([junction_box]))

junction_box_pairs = []

for i in range(0, len(junction_boxes)):
  for j in range(i + 1, len(junction_boxes)):
    first_box = junction_boxes[i]
    second_box = junction_boxes[j]
    if first_box == second_box:
      continue
    junction_box_pairs.append({"first_box": first_box, "second_box": second_box, "dist": box_dist(first_box, second_box)})

junction_box_pairs.sort(key = lambda dist : dist["dist"])

for i in range(0, len(junction_box_pairs)):
  junction_box_pair = junction_box_pairs[i]
  first_box = junction_box_pair["first_box"]
  second_box = junction_box_pair["second_box"]

  first_circuit = None
  second_circuit = None
  for circuit in circuits:
    if circuit.is_in_circuit(first_box):
      first_circuit = circuit
    if circuit.is_in_circuit(second_box):
      second_circuit = circuit
  if first_circuit == second_circuit:
    continue
  merged = merge_circuits(first_circuit, second_circuit)
  circuits.remove(first_circuit)
  circuits.remove(second_circuit)
  circuits.append(merged)
  if(len(circuits) == 1):
    print(first_box.x * second_box.x)
    break