#! python3

import os,shutil

os.makedirs('.\\copy')
for foldername, subfolders, filenames in os.walk('.\\'):
  for filename in filenames:
    if filename.endswith('.txt'):
      shutil.copy(os.path.join(foldername, filename), '.\\copy')
