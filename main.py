from typing import Union
from fastapi import FastAPI
import requests
import json

app = FastAPI()

def getlist(hliwa):
  querystrings = {"q":hliwa}
  headerss = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "youtube-search-results.p.rapidapi.com"
  }
  urls = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
  responses = requests.request("GET", urls, headers=headerss, params=querystrings)
  jess_dict2 = json.loads(responses.text)
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
            if mylist[i]['type']=='video':
                mine={"songid":mylist[i]['id'],
                "songname":mylist[i]['title'],
                "userid":mylist[i]['author']['channelID'],
                "trackid":mylist[i]['id'],
                "duration":str(mylist[i]['duration']),
                "cover_image_url":mylist[i]['bestThumbnail']['url'],
                "first_name":mylist[i]['author']['name'],
                "last_name":str(mylist[i]['views'])
                }
                
                finalelist.append(mine)
            i=i+1
            print(finalelist)
        return {"results":finalelist }


@app.get("/artist/{item_id}")
def artist(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/album/{item_id}")
def album(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}