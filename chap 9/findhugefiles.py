#! python3

import os

for foldername, subfolders, filenames in os.walk('.'):
  min_size = 1000
  for filename in filenames:
    path = os.path.join(foldername, filename)
    if os.path.getsize(path) > min_size:
      print(os.path.abspath(path) + ' : ' + str(os.path.getsize(path)) + 'byte')