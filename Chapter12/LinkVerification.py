import requests, bs4, os

os.makedirs('/home/isocyanate/Downloads/link_verify',exist_ok=True)
res=requests.get('https://automatetheboringstuff.com/')
print(res.raise_for_status)

soup=bs4.BeautifulSoup(res.text,'html.parser')

aElem=soup.select('a')
hrefs=[]

for i in aElem:
    hrefs.append(i.get('href'))

print(hrefs)
for j in hrefs:
    try:
        res=requests.get(j)
        if res.status_code != requests.codes.ok:
            print(f'There was a problem downloading {j} page')

        else:
            savinglink = open(os.path.join('/home/isocyanate/Downloads/link_verify', os.path.basename(j+'.html')),'wb')
            print(f'Downloading {j}')
            for k in res.iter_content(100000):
                savinglink.write(k)
            savinglink.close()
            
    except requests.exceptions.MissingSchema:
        if'/2e/chapter' in str(j):
            j='https://automatetheboringstuff.com'+j
            savinglink = open(os.path.join('/home/isocyanate/Downloads/link_verify', os.path.basename(j+'.html')),'wb')
            print(f'Downloading {j}')
            for l in res.iter_content(100000):
                savinglink.write(l)
            savinglink.close()
        else:
            print('Invalid url')