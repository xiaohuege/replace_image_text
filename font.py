import zhconv

def to_simplified(word):
  '''繁体文字转简体文字'''
  return zhconv.convert(word, 'zh-hans')