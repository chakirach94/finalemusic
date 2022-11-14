from typing import Union
from fastapi import FastAPI
import requests
import json
from fastapi.responses import RedirectResponse, HTMLResponse


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
   link=getlinkfromid(item_id)
   if "googlevideo" in link:
        response = RedirectResponse(url=link,status_code=303)
   else:
        response = RedirectResponse(url="https://rr1---sn-p5h-gc5y.googlevideo.com/videoplayback?expire=1668471517&ei=fYZyY_7DDpyG6dsPw-K7uA0&ip=23.88.39.196&id=o-AD8vcXH_gPOXVARf1Bb8UkKzphZ5FWjeoiOke5DlR9Xq&itag=22&source=youtube&requiressl=yes&vprv=1&svpuc=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=179.513&lmt=1647228121272336&fexp=24001373,24007246&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Csvpuc%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAL3-mAgxcBhQI1vbCXrqzfzglkAK84hhO5ui68IWJ4-GAiBKOXWW5Tyz150ttixdXpUKn-C1ALVFpZ0mFRzLmdYgnw%3D%3D&redirect_counter=1&rm=sn-4g5ekr7l&req_id=66244d2638ba3ee&cms_redirect=yes&cmsv=e&ipbypass=yes&mh=wI&mip=160.177.1.229&mm=31&mn=sn-p5h-gc5y&ms=au&mt=1668449340&mv=m&mvi=1&pl=22&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgFtr7eZkeby9-Ekr3itgncfEN2sKDJXo04d-9MNCuSe8CIGLCSd3hQZUiWV2NBuFFb6OBpw7KRNwb_ROpe5LkMU7Z",status_code=303)
   return response

@app.get("/album/{item_id}")
def album(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
