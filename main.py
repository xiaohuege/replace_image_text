#-*- coding: UTF-8 -*-
import json
from youdao import translate
from os import path
from font import to_simplified
from image import rebuild_image
from PIL import Image

# 缓存文件路径
cachePath = path.realpath('./data/bak.json')

# 将有道文字识别结果缓存到json，减少接口调用次数
def save_json(res):
  global cachePath
  file = open(cachePath, 'w+')
  file.write(json.dumps(res))
  file.close()

def get_json():
  global cachePath
  file = open(cachePath, 'r')
  res = json.loads(file.read())
  file.close()
  return res

# 坐标转换
def split_bounding(str):
  arr = str.split(',')
  return { 'left_top': arr[0:2], 'right_top': arr[2:4], 'right_bottom': arr[4:6], 'left_bottom': arr[6:8]}

def bootatrap(imgPath):
  res = translate(imgPath)
  # res = get_json()
  save_json(res)
  if res is None or res.get('errorCode') != '0':
    print('接口请求失败')
    return
  result = res.get('Result')
  # 文字区块方向
  # orientation = result.get('orientation')
  regions = result.get('regions')
  # 取出所有文字--按行
  words = []
  for reg in regions:
    lines = reg.get('lines')
    words = words + lines
  # 保存所有繁体字
  tradit_words = []
  for w in words:
    word = w.get('text')
    boundingBox = w.get('boundingBox')
    # 转换成简体字
    new_word = to_simplified(word)
    # 如果转换之后和原始值不同，则认为是繁体字
    tradit_words.append({ 'word': word, 'to': new_word, 'boundingBox': split_bounding(boundingBox) })

  image = Image.open(imgPath)
  rebuild_image(image, tradit_words)
  image.save(imgPath.replace('/data/', '/output/'))

if __name__ == '__main__':
  imgPath = path.realpath('./data/7.jpeg')
  bootatrap(imgPath)