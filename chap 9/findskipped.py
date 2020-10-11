#! python3

import os,re

#接頭辞と正規表現指定
prefix = 'spam'
pattern = re.compile(prefix + r"""(\d*?)
                                  (\..*?)$""", re.VERBOSE)

#フォルダの中のファイル名一覧取得し連番のパターン抽出
filenames = os.listdir('.\seqfiles')
filenames.sort()
mo = pattern.search(''.join(filenames))
length = len(mo.group(1))
num = 1

#ファイル名の連番が1づつ上がっているか確認し、違っていればなかったファイルを作成する
for filename in filenames:
  mo =  pattern.search(filename)
  while int(mo.group(1)) != num:
    new_filename = prefix + str(num).zfill(3) + mo.group(2)
    new_path = os.path.join(os.path.abspath('.\seqfiles'), new_filename)
    new_file = open(new_path, 'w')
    new_file.close()
    print(prefix + str(num).zfill(3) + mo.group(2) + '作った')
    num = num + 1
  num = num + 1
      