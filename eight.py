import math


def calculate_area(shape, radius=None, length=None, width=None, base=None, height=None):
  """
    Calculates the area of different shapes based on the 'shape' argument.
    """
  shape = shape.lower()

  if shape == "circle" and radius is not None:
    return math.pi * (radius**2)

  elif shape == "rectangle" and length is not None and width is not None:
    return length * width

  elif shape == "triangle" and base is not None and height is not None:
    return 0.5 * base * height

  else:
    return "Invalid shape or missing dimensions!"


# --- Testing the polymorphic function ---

# 1. Circle (Requires: radius)
circle_area = calculate_area("circle", radius=5)
print(f"circle Area: {circle_area:.2f}")

# 2. Rectangle (Requires: length, width)
rectangle_area = calculate_area("rectangle", length=10, width=4)
print(f"Rectangle Area: {rectangle_area}")

# 3. Triangle (Requires: base, height)
triangle_area = calculate_area("triangle", base=..., height=...)
