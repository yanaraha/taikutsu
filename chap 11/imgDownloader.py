#! python3

import requests, bs4, os, sys

os.makedirs('test', exist_ok=True)

res = requests.get(sys.argv[1])
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

img_elem = soup.select('.alignnone')
if img_elem == []:
  print('なかった')
else:
  print('開始')
  for i in range(len(img_elem)):
    img_url = img_elem[i].get('data-src')
    if img_url == None:
      continue
    res = requests.get(img_url)
    res.raise_for_status()
    img_file = open(os.path.join('test', os.path.basename(img_url)), 'wb')
    for chunk in res.iter_content(100000):
      img_file.write(chunk)
    img_file.close()
print('完了')
