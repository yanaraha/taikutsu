#! python3

import random
guess = ''
while guess not in (0, 1):
  print('コインの表裏を当ててください。1(表)か0(裏)を入力してください:')
  guess = int(input())
toss = random.randint(0, 1) #0は裏、1は表
if toss == guess:
  print('当たり')
else:
  print('はずれ')
  guess = int(input())
  if toss == guess:
    print('当たり')
  else:
    print('終わり')