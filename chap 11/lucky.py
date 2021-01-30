#! python3

import requests, sys, webbrowser, bs4

print('Googling...')
url = 'http://www.google.com/search?q=' + ' '.join(sys.argv[1:])
res = requests.get(url)
res.raise_for_status()
# file = open('test', 'wb')
# file.write(res.text.encode('cp932', 'ignore'))
# file.close()
#TODO:上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text, 'html5lib')
link_elems = soup.select('.kCrYT a')

#TODO:各結果をブラウザのタブで開く
num_open = min(5, len(link_elems))
for i in range(num_open):
  webbrowser.open('http://google.com' + link_elems[i].get('href'))