from config import APP_KEY, APP_SECRET, YOUDAO_URL
from common import post
import base64
import uuid
import time
import hashlib

def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def translate(imgPath):
  file = open(imgPath, 'rb')
  content = base64.b64encode(file.read()).decode('utf-8')
  file.close()

  data = {}
  data['img'] = content
  data['detectType'] = '10012'
  data['imageType'] = '1'
  data['langType'] = 'zh-CHT'
  data['docType'] = 'json'
  data['signType'] = 'v3'
  curtime = str(int(time.time()))
  data['curtime'] = curtime
  salt = str(uuid.uuid1())
  signStr = APP_KEY + truncate(content) + salt + curtime + APP_SECRET
  sign = encrypt(signStr)
  data['appKey'] = APP_KEY
  data['salt'] = salt
  data['sign'] = sign

  headers = {'Content-Type': 'application/x-www-form-urlencoded'}
  return post(YOUDAO_URL, data, headers)
