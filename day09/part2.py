input_lines = open(0).read().splitlines()

class Coord:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2

class Rectangle:
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

red_tile_coords = []
shape_x_max = 0
for input_line in input_lines:
  x = int(input_line.split(",")[0])
  y = int(input_line.split(",")[1])
  red_tile_coords.append(Coord(x, y))
  if x > shape_x_max:
    shape_x_max = x

vertical_lines = []
horizontal_lines = []
for i in range(0, len(red_tile_coords)):
  first_red_tile_coord = red_tile_coords[i]
  second_red_tile_coord = red_tile_coords[(i + 1) % len(red_tile_coords)]
  if first_red_tile_coord.x == second_red_tile_coord.x:
    vertical_lines.append(Line(first_red_tile_coord.x, first_red_tile_coord.y, second_red_tile_coord.x, second_red_tile_coord.y))
  else:
    horizontal_lines.append(Line(first_red_tile_coord.x, first_red_tile_coord.y, second_red_tile_coord.x, second_red_tile_coord.y))
vertical_lines.sort(key = lambda line : line.x1)
horizontal_lines.sort(key = lambda line : line.y1)

def vertical_line_is_inside_rectangle(vertical_line, rectangle):
  if vertical_line.x1 > rectangle.x and vertical_line.x1 < rectangle.x + rectangle.width - 1 and (
       (vertical_line.y1 > rectangle.y and vertical_line.y1 < rectangle.y + rectangle.height - 1) or
       (vertical_line.y2 > rectangle.y and vertical_line.y2 < rectangle.y + rectangle.height - 1) or
       (min(vertical_line.y1, vertical_line.y2) <= rectangle.y and max(vertical_line.y1, vertical_line.y2) >= rectangle.y + rectangle.height - 1)
     ):
    return True
  return False

def horizontal_line_is_inside_rectangle(horizontal_line, rectangle):
  if horizontal_line.y1 > rectangle.y and horizontal_line.y1 < rectangle.y + rectangle.width - 1 and (
       (horizontal_line.x1 > rectangle.x and horizontal_line.x1 < rectangle.x + rectangle.width - 1) or
       (horizontal_line.x2 > rectangle.x and horizontal_line.x2 < rectangle.x + rectangle.width - 1) or
       (min(horizontal_line.x1, horizontal_line.x2) <= rectangle.x and max(horizontal_line.x1, horizontal_line.x2) >= rectangle.x + rectangle.width - 1)
     ):
    return True
  return False

def horizontal_line_intersects_vertical_line(horizontal_line, rectangle):
  vertical_lines_intersected = []
  for vertical_line in vertical_lines:
    if horizontal_line.y1 >= min(vertical_line.y1, vertical_line.y2) and \
       horizontal_line.y1 <= max(vertical_line.y1, vertical_line.y2) and \
       vertical_line.x1 >= min(horizontal_line.x1, horizontal_line.x2) and \
       vertical_line.x1 <= max(horizontal_line.x1, horizontal_line.x2):
      if vertical_line.y1 == horizontal_line.y1 or vertical_line.y2 == horizontal_line.y1:
        if vertical_line_is_inside_rectangle(vertical_line, rectangle):
          vertical_lines_intersected.append(vertical_line)
        else:
          continue
      else:
        vertical_lines_intersected.append(vertical_line)
 
  return False if len(vertical_lines_intersected) == 0 else True

def vertical_line_intersects_horizontal_line(vertical_line, rectangle):
  horizontal_lines_intersected = []
  for horizontal_line in horizontal_lines:
    if vertical_line.x1 >= min(horizontal_line.x1, horizontal_line.x2) and \
       vertical_line.x1 <= max(horizontal_line.x1, horizontal_line.x2) and \
       horizontal_line.y1 >= min(vertical_line.y1, vertical_line.y2) and \
       horizontal_line.y1 <= max(vertical_line.y1, vertical_line.y2):
      if horizontal_line.x1 == vertical_line.x1 or horizontal_line.x2 == vertical_line.x1:
        if horizontal_line_is_inside_rectangle(horizontal_line, rectangle):
          horizontal_lines_intersected.append(horizontal_line)
        else:
          continue
      else:
        horizontal_lines_intersected.append(horizontal_line)
  
  return False if len(horizontal_lines_intersected) == 0 else True

def rectangle_is_inside_shape(rectangle):
  left_side = Line(rectangle.x, rectangle.y + 1, rectangle.x, rectangle.y + rectangle.height - 2)
  top_side = Line(rectangle.x + 1, rectangle.y, rectangle.x + rectangle.width - 2, rectangle.y)
  bottom_side = Line(rectangle.x + 1, rectangle.y + rectangle.height - 1, rectangle.x + rectangle.width - 2, rectangle.y + rectangle.height - 1)
  right_side = Line(rectangle.x + rectangle.width - 1, rectangle.y + 1, rectangle.x + rectangle.width - 1, rectangle.y + rectangle.height - 2)

  if vertical_line_intersects_horizontal_line(left_side, rectangle) or vertical_line_intersects_horizontal_line(right_side, rectangle) or \
     horizontal_line_intersects_vertical_line(top_side, rectangle) or horizontal_line_intersects_vertical_line(bottom_side, rectangle):
    return False
  return True

highest_area = -1
for i in range(0, len(red_tile_coords)):
  for j in range(i + 1, len(red_tile_coords)):
    if i == j:
      continue
    first_coord = Coord(int(red_tile_coords[i].x), int(red_tile_coords[i].y))
    second_coord = Coord(int(red_tile_coords[j].x), int(red_tile_coords[j].y))
    rectangle = Rectangle(min(first_coord.x, second_coord.x), min(first_coord.y, second_coord.y), abs(first_coord.x - second_coord.x) + 1, abs(first_coord.y - second_coord.y) + 1)

    area = rectangle.width * rectangle.height
    if rectangle_is_inside_shape(rectangle) and area > highest_area:
      highest_area = area

print(highest_area)