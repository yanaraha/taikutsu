#! python3
import re

def restrip(moji, del_str = 's'):
  """ mae_regex_str = r'^' + '\\' + del_str + r'+'
  ato_regex_str = '\\' + del_str + r'+' + r'$'
  mae_regex = re.compile(mae_regex_str)
  ato_regex = re.compile(ato_regex_str)
  return ato_regex.sub('', mae_regex.sub('', moji)) """
  regex_str = r'^' + '\\' + del_str + r'+' + r'(.*?)' + '\\' + del_str + r'+' + r'$'
  return re.sub(regex_str, r'\1', moji)

print('文字列を入力してください:')
moji = input()
print('削除対象を入力してください、指定しない場合はEnterキー')
del_str = input()
if del_str == '':
  restr = restrip(moji)
else:
  restr = restrip(moji, del_str)
print(restr)