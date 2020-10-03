#! python3

import re

#パスワードの強度を測る
def check_password(password):
  #正規表現を定義
  uppercase = re.compile(r'[A-Z]+')
  lowercase = re.compile(r'[a-z]+')
  numeral = re.compile(r'[0-9]+')

  #8文字以上であることの確認
  if len(password) < 8:
    return False
  
  #大文字を含むことの確認
  if uppercase.search(password) == None:
    return False
  #小文字を含むことの確認
  if lowercase.search(password) == None:
    return False
  #数字を含むことの確認
  if numeral.search(password) == None:
    return False

  return True

print('パスワードを入力してください:')
password = input()
if check_password(password) == True:
  print('問題なし')
else:
  print('問題あり')