#coding=utf-8
#多进程下载XKCD上的极客漫画

import os,requests,bs4,threading

if not os.path.exists('./xkcd'):
	os.mkdir('xkcd')

def downloadXkcd(startComic,endComic):
	for urlNumber in range(startComic,endComic):
		print 'Downloading page https://xkcd.com/%s ...'%urlNumber
		res = requests.get('https://xkcd.com/%s'%urlNumber)
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text, 'lxml')

		comicElem = soup.select('#comic img')

		if comicElem ==[]:
			print 'Not find comic image..'
		else:
			comicUrl = 'http:'+comicElem[0].get('src')
			print comicUrl
			print 'Downloading image %s...'%comicUrl
			res = requests.get(comicUrl)
			print 'dsaf'
			res.raise_for_status()

			imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()

# downloadXkcd(1,10)
dowmloadTreads = []
for i in range(1,20):
	dowmloadTread = threading.Thread(target=downloadXkcd,args=(i,i+1))
	dowmloadTreads.append(dowmloadTread)
	dowmloadTread.start()

for dowmloadTread in dowmloadTreads:
	dowmloadTread.join()
print 'Done.'
