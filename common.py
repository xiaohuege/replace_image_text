import requests
import json

def post(url, data, headers):
  '''发起post请求'''
  res =  requests.post(url, data=data, headers=headers)
  if res is not None and res.content:
    return json.loads(res.content)