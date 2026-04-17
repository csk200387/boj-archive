def get_color(c):
  if c >= 620 and c <= 780:
    return "Red"
  elif c >= 590 and c < 620:
    return "Orange"
  elif c >= 570 and c < 590:
    return "Yellow"
  elif c >= 495 and c < 570:
    return "Green"
  elif c >= 450 and c < 495:
    return "Blue"
  elif c >= 425 and c < 450:
    return "Indigo"
  else:
    return "Violet"

print(get_color(int(input())))