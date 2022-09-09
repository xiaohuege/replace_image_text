from PIL import ImageDraw,ImageFont
from color import hex_to_rgb,rgb_to_hex,is_color_alike
from text import is_chn

WORD_SPACE = 10

# 重新生成图片
def rebuild_image(image, tradit_words):
  # 识别文字颜色以及所在区域的背景色
  for word in tradit_words:
    boundingBox = word.get('boundingBox')
    words = word.get('word')
    to = word.get('to')

    # 截取文字区域
    box = get_range_box(boundingBox)
    print(words, to, box)
    image_crop = image.crop(box)
    # 获取文字颜色、背景颜色、字体大小
    color, bg_color, font_size = get_font_and_color(image_crop, to)
    # 重置背景
    width,height = image_crop.size
    start_x = box[0]
    start_y = box[1]
    for i in range(width):
      for j in range(height):
        xy = (start_x + i, start_y + j)
        image.putpixel(xy, bg_color)

    # 填充文字
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('RuiZiChaoPaiYanWeiSongJian-Shan-ChangGui.ttf', size=font_size)
    draw_text(draw, box[0], box[1], font_size, to, color, font)

# 绘制文字
def draw_text(draw, start_x, start_y, font_size, text, color, font):
  prev_x = start_x
  for i in range(len(text)):
    w = 0
    if is_chn(text[i]):
      w += font_size
      w += WORD_SPACE
    else:
      w += int(font_size * 0.6)
    draw.text((prev_x, start_y), text[i], fill=color, font=font)
    prev_x += w


# 获取文字区域
def get_range_box(boundingBox):
  left_top = boundingBox.get('left_top')
  right_bottom = boundingBox.get('right_bottom')
  box = (int(left_top[0]), int(left_top[1]), int(right_bottom[0]), int(right_bottom[1]))
  return box

# 获取文字字体大小、颜色以及背景色
def get_font_and_color(image_crop, to):
  width,height = image_crop.size
  data = list(image_crop.getdata())
  colors = get_colors(data, width, height)
  color, bg_color = get_font_and_bg_color(colors)
  font_width = width/len(to)
  font_size = int(font_width)
  return (color, bg_color, font_size)

# 获取图片中的色值
def get_colors(data, width, height):
  res = {}
  for i in range(height):
    for j in range(width):
      rgb = data[i * width + j]
      color = rgb_to_hex(rgb)
      if color not in res:
        res[color] = 0
      res[color] += 1
  return res

def cmp(nums):
  return nums[1]

# 获取字体和背景颜色
# 占比最高的为背景色，第二的为字体颜色
def get_font_and_bg_color(colors):
  data = list(colors.items())
  data.sort(key=cmp, reverse=True)
  # 取前100条
  top_data = data[:100]
  count = len(top_data)
  idx = 0
  valid_idx = 1
  valid_list = [top_data[idx]]
  while idx < count and valid_idx < count:
    c1 = top_data[idx]
    c2 = top_data[valid_idx]
    if is_color_alike(c1[0], c2[0]):
      tmp_count = len(valid_list)
      tmp_color, tmp_num = valid_list[-1]
      valid_list[tmp_count - 1] = (tmp_color, tmp_num + c2[1])
      valid_idx += 1
    else:
      idx = valid_idx
      valid_list.append(top_data[idx])

  color = (0,0,0)
  bg_color = hex_to_rgb(valid_list[0][0])
  if bg_color[0] == color[0] and bg_color[1] == color[1] and bg_color[2] == color[2]:
    color = (255 - bg_color[0], 255 - bg_color[1], 255 - bg_color[2])
  return (color, bg_color)

