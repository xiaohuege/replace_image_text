import zhconv
from text import replace_special_words

def to_simplified(word):
  '''繁体文字转简体文字'''
  to = zhconv.convert(word, 'zh-hans')
  return replace_special_words(to)