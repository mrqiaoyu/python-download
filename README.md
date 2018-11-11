# download
##[功能描述]
* 通过连接下载视频，音乐和文件
* 显示下载进度条和时间信息
* 可以暂停和继续下载

##[开发环境]
* python 3.7
* tqdm 4.28.1

##[使用说明]
1. 安装进度条的包

    `pip install tqdm==4.28.1`

2.填入下载文件的连接和保存位置 
 ``` 
    if __name__ == '__main__':
        url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-694734.jpg'
        src = 'images/beauty.jpg'
        download(src, url)
``` 
   
3.运行程序
 
 `python main.py`
##[联系方式]
email: qiaoyu721@gmail.com