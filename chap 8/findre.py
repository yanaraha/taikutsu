#! python3

import re, sys, os

while True:
  if len(sys.argv) < 2:
    print('引数指定')
  else:
    break

pattern = re.compile(sys.argv[1])

for name in os.listdir(os.getcwd()):
  if os.path.isfile(name) == False:
    break
  file = open(name, 'r', encoding='utf-8')
  for line in file:
    mo = pattern.search(line)
    if mo is not None:
      print(name + ':' + line)

  
  
