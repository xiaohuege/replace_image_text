import json
from youdao import translate
from os import path
from font import to_simplified

def save_json(res):
  jsonPath = path.realpath('./data/1.json')
  file = open(jsonPath, 'w+')
  file.write(json.dumps(res))
  file.close()

def get_json():
  jsonPath = path.realpath('./data/1.json')
  file = open(jsonPath, 'r')
  res = json.loads(file.read())
  file.close()
  return res

# 坐标转换
def split_bounding(str):
  arr = str.split(',')
  return { 'left_top': arr[0:2], 'right_top': arr[2:4], 'right_bottom': arr[4:6], 'left_bottom': arr[6:8]}

def bootatrap(imgPath):
  # res = translate(imgPath)
  res = get_json()
  if res is None or res.get('errorCode') != '0':
    print('接口请求失败')
    return
  result = res.get('Result')
  # 文字区块方向
  # orientation = result.get('orientation')
  regions = result.get('regions')
  # 去除所有文字
  words = []
  for reg in regions:
    lines = reg.get('lines')
    for line in lines:
      words = words + line.get('words')
  # 保存所有繁体字
  tradit_words = []
  for w in words:
    word = w.get('word')
    boundingBox = w.get('boundingBox')
    # 转换成简体字
    new_word = to_simplified(word)
    # 如果转换之后和原始值不同，则认为是繁体字
    if word != new_word:
      tradit_words.append({ 'word': word, 'to': new_word, 'boundingBox': split_bounding(boundingBox) })

  # 识别文字颜色以及所在区域的背景色
  print(tradit_words)

if __name__ == '__main__':
  imgPath = path.realpath('./data/1.jpeg')
  bootatrap(imgPath)