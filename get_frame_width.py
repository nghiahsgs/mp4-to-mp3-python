import cv2
import os
import requests
import urllib.request


def get_file_size_MB_local(file_path):
    b = os.path.getsize(file_path)
    return b/1024/1024


def get_video_resolution(file_path):
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    return min(height,width)


def download_video(url_link):
    urllib.request.urlretrieve(url_link, 'video_name.mp4') 
if __name__ =="__main__":
    # file_path = "Ink in Water Background (360p).mp4"
    # resolution = get_video_resolution(file_path)

    # file_size = get_file_size_MB_local(file_path)

    '''
    url_link = 'https://rr2---sn-8pxuuxa-i5o6k.googlevideo.com/videoplayback?expire=1642345678&ei=buDjYcfkF9CGs8IPzpG3uAY&ip=27.72.30.231&id=o-AOP6es8TMk1gWjlfIkUfGinmCVHsGat2YaNaoq105zRd&itag=18&source=youtube&requiressl=yes&mh=Df&mm=31%2C26&mn=sn-8pxuuxa-i5o6k%2Csn-oguesn6d&ms=au%2Conr&mv=m&mvi=2&pl=22&initcwndbps=1688750&vprv=1&mime=video%2Fmp4&ns=0wj_thysPv0TseSviOx7IVYG&gir=yes&clen=30511330&ratebypass=yes&dur=510.769&lmt=1642316596791459&mt=1642323701&fvip=2&fexp=24001373%2C24007246&c=WEB&txp=5530434&n=F68TfwMhz9NvaIxI3kyrn&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgLgUqdF1kHePqfU51lhdc3o6I_OWADDpF5-4MLo2_ZYoCIQC1oIKElrsPJGyj2gXuxumFTbmS7oAdisdtn_bW4TyeVw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAMGBBEeOQ2ay414meyjpg01oe5a9toMpBRIH5MAmp28kAiBq-jSRcSsKAOkjgSiQPZMOMUfNbGb63OPS7usEqIwvRQ%3D%3D'
    # download_video(url_link)
    r = requests.get(url_link, stream = True)
    # download started 
    file_name = "video_name1.mp4"
    with open(file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
    '''