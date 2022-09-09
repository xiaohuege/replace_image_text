# 16进制转RGB
def hex_to_rgb(color):
  r = int(color[0:2], 16)
  g = int(color[2:4], 16)
  b = int(color[4:6], 16)
  return (r,g,b)

# RGB转16进制
def rgb_to_hex(color):
  r,g,b = color
  res = str(hex(r))[-2:].replace('x', '0').upper()
  res += str(hex(g))[-2:].replace('x', '0').upper()
  res += str(hex(b))[-2:].replace('x', '0').upper()
  return res

RATE = 0.5

def check(n1, n2):
  return abs(n1 - n2)/255 < RATE

# 判断颜色是否接近(16进制)
def is_color_alike(c1, c2):
  r1,g1,b1 = hex_to_rgb(c1)
  r2,g2,b2 = hex_to_rgb(c2)
  res = False
  if check(r1,r2) and check(g1,g2) and check(b1,b2):
    res = True
  return res