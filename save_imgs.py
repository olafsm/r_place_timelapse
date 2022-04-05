import requests
import shutil
import time

with open("urls.txt") as f:
    urls = f.readlines()

for (i, url) in enumerate(urls):
    res = requests.get(url.strip(), stream=True)
    if res.status_code == 200:
        with open("./img/img{}.png".format(i), 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',i)
    else:
        print('Image Couldn\'t be retrieved')
    time.sleep(0.05)
print("{}".format(len(urls)))