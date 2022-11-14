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


@app.get("/artist/{item_id}")
def artist(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/album/{item_id}")
def album(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
