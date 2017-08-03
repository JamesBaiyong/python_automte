#coding=utf-8
#下载XKCD上的极客漫画

import os,requests,bs4

url = 'https://xkcd.com'
if not os.path.exists('./xkcd'):
	os.mkdir('xkcd')
while not url.endswith('#'):
	#Download the page.
	print  'Downloading page %s...'%url
	res=requests.get(url)
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,'lxml')

	# Find THE URL of the comic image.
	comicElem=soup.select('#comic img')
	if comicElem ==[]:
		print 'Not find comic image'
	else:
		comicUrl ='http:'+comicElem[0].get('src')
		print 'Downloading image page %s'%comicUrl
		res = requests.get(comicUrl)
		res.raise_for_status()

	#Download the image.Save the image to ./xkcd
	imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	#Get the Prev button's URL
	prevLink = soup.select('a[rel="prev"]')[0].get('href')

	url='https://xkcd.com'+prevLink
print 'Done.'