from typing import Union
from fastapi import FastAPI
import requests
import json

app = FastAPI()

def getlist(hliwa):
  url = "https://youtube-media-downloader.p.rapidapi.com/v2/search/videos"
  querystring = {"keyword":hliwa}
  headers = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  jess_dict2 = json.loads(response.text)

  return jess_dict2

def getlinkfromid(id):
  url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
  querystring = {"id":id}
  headers = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
  }
  response2 = requests.request("GET", url, headers=headers, params=querystring)
  jess_dict2 = json.loads(response2.text)
  return jess_dict2['formats'][2]['url']

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search/songs/{item_id}")
def searsh(item_id: str, q: Union[str, None] = None):
        mylist=getlist(item_id)['items']
        i=0
        finalelist=[]
        while (i<10 or i>len(mylist)):
            mine={
            "songid":mylist[i]['id'],
            "songname":mylist[i]['title'],
            "userid":mylist[i]['channel']['id'],
            "trackid":mylist[i]['id'],
            "duration":str(mylist[i]['lengthText']),
            "cover_image_url":mylist[i]['thumbnails'][0]['url'],
            "first_name":mylist[i]['channel']['name'],
            "last_name":str(mylist[i]['viewCountText'])
            }
            finalelist.append(mine)
            i=i+1
        return {"results":finalelist }


@app.get("/gotolink/{item_id}")
async def gotolink(item_id: str, q: Union[str, None] = None):
    response = RedirectResponse(url='https://redirector.googlevideo.com/videoplayback?expire=1668469041&ei=0HxyY5-ZLPCP2LYPlIG-iAo&ip=198.98.59.215&id=o-AHn0JsC6v3iZM03yojnwR9LFlRTKr_l5rU5g_yX0rnb5&itag=18&source=youtube&requiressl=yes&mh=D9&mm=31%2C29&mn=sn-ab5sznzd%2Csn-ab5l6nrs&ms=au%2Crdu&mv=m&mvi=1&pl=24&initcwndbps=93750&spc=SFxXNumFP2NhDU7yEwGDc7-aUQxs8SGs3Z1iFz4GaLaD&vprv=1&mime=video%2Fmp4&ns=ecWE6WCf72MEfufspWFhMZAJ&gir=yes&clen=14088459&ratebypass=yes&dur=199.936&lmt=1666358220522542&mt=1668446943&fvip=2&fexp=24001373%2C24007246&c=WEB&txp=4530434&n=N73YGZbZ774bAg&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAP_Y6liefYjEidUL4CEDKZqRUxdv2kHdZTjCyWucmHiRAiEArT9EbytDJMeqBKbi9gamQ2WvZR40tCm1SS0OJPesYPM%3D&sig=AOq0QJ8wRgIhAL3K6tBgeWOvBTlvJphMALBicFJheLDPZAVBwqxK6D8fAiEAmaSy2r0ONcrTzcO-Dx_jUkBy8n40E8l34K2L6RojcVY%3D&range=0-')
    return response

@app.get("/album/{item_id}")
def album(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
