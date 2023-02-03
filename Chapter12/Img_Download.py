import requests, bs4, os
os.makedirs('/home/isocyanate/Downloads/flickr',exist_ok=True)
search='car'
res=requests.get('https://flickr.com/search/?text='+search)
print(res.raise_for_status)
soup=bs4.BeautifulSoup(res.text,'html.parser')

# <a class="html-attribute-value html-resource-link" target="_blank" href="//live.staticflickr.com/1062/886413370_31b96208ec_m.jpg" rel="noreferrer noopener">//live.staticflickr.com/1062/886413370_31b96208ec_m.jpg</a>
aElems=soup.select('img')
hrefs=[]
# print(aElems)

for i in aElems:
    pic=i.get('src')
    if '//live' in str(pic):
        pic='https:'+str(pic)
        hrefs.append(pic)

# print(hrefs)

for j in hrefs:
    try:
        res=requests.get(j)
        if res.status_code != requests.codes.ok:
            print(f'There was a problem downloading {j} page')
        else:
            image = open(os.path.join('flikr', os.path.basename(j+'.jpg')),'wb')
            print(f'Downloading {j}')
            for k in res.iter_content(100000):
                image.write(k)
            image.close()
    except requests.exceptions.MissingSchema:
        print("Invalid URL")


