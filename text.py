#-*- coding: UTF-8 -*-
SPECIAL_WORDS = {
  '肾藏': '肾脏',
  '瞻固醇': '胆固醇',
  '内臓': '内脏',
  '补锈质': '补钙质',
  '锈.钱.孟': '钙.镁.锰.锌',
  '邮子油': '椰子油',
  '棕惘油': '棕榈油',
  '葡萄油': '葡萄籽油',
  'TS缇爱丝': 'TS爱丝',
  '黏著力': '粘着力',
  '黏附': '粘附',
  '到斗二指肠': '到十二指肠'
}

# 繁体组词替换
def replace_special_words(words):
  res = words
  for (k,v) in SPECIAL_WORDS.items():
    res = res.replace(k, v)
  return res

# 是否中文
def is_chn(text):
  if text is None:
    return False
  return '\u4e00' <= text <= '\u9fa5'