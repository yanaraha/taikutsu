#! python3
#Usage:
#python mcb.pyw save <keyword> クリップボードをキーワードに紐づけて保存
#python mcb.pyw delete <keyword> 指定されたキーワードを削除
#python mcb.pyw delete all すべてのキーワードを削除
#python mcb.pyw <keyword> キーワードに紐づけられたテキストをクリップボードにコピー
#python mcb.pyw list 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

#TODO:クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
  mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1].lower == 'delete':
  if sys.argv[2].lower == 'all':
    mcb_shelf.clear()
  else:
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
  #キーワード一覧と内容の読み込み
  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcb_shelf.keys())))
  elif sys.argv[1] in mcb_shelf:
    pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
