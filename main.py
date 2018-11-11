from tqdm import tqdm
import requests
import os


def download(src, url):
    file_size = int(requests.head(url).headers['Content-Length'])
    dir = os.path.split(src)[0]
    if not os.path.exists(dir):
        os.makedirs(dir)

    if os.path.exists(src):
        first_byte = os.path.getsize(src)
    else:
        first_byte = 0
    if first_byte >= file_size:
        print('该文件已存在！')
        return file_size

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        '70.0.3538.67 Safari/537.36',
        'Range': 'bytes=%s-%s' % (first_byte, file_size),
    }
    pbar = tqdm(total=file_size, initial=first_byte, unit='B', unit_scale=True, desc=src.split('/')[-1])
    resp = requests.get(url, headers=header, stream=True)

    with open(src, 'ab') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                pbar.update(1024)

    pbar.close()
    return file_size


if __name__ == '__main__':
    url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-694734.jpg'
    src = 'images/beauty.jpg'
    download(src, url)
