import json
from youdao import translate
from os import path

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


def bootatrap():
  imgPath = path.realpath('./data/1.jpeg')
  # res = translate(imgPath)
  res = get_json()
  print(res)

if __name__ == '__main__':
  bootatrap()