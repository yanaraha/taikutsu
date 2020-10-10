#! python3

import os, re

#変換対象文字列セット作成
change_list = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

#ファイルの読み込み
print('読み込むファイルのパスを入力してください')
path = input()

#ファイルの存在チェック
if os.path.exists(path) == True and os.path.isfile(path) == True:
  #ファイルを読み込み空白区切りでリスト化
  file = open(path)
  sentence = file.read()

  #変換対象文字列セットとマッチしたら文字列変換
  while True:
    mo = change_list.search(sentence)
    if mo is None:
      break
    print('Enter  {}'.format(mo.group()))
    change = input()
    sentence = sentence.replace(mo.group(), change, 1) 

  #変換後ファイル作成
  new_path = os.path.join(os.path.dirname(path), 'new_' + os.path.basename(path))
  new_file = open(new_path, 'w')
  new_file.write(sentence)
  file.close()
  new_file.close()
else:
  print('正しくない')    