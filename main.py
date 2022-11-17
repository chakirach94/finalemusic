
from typing import Union
from fastapi import FastAPI
import requests
import json
from fastapi.responses import RedirectResponse, HTMLResponse


app = FastAPI()

def channelsearch(channel):
  url = "https://youtube-media-downloader.p.rapidapi.com/v2/search/channels"

  querystring = {"keyword":channel,"sortBy":"relevance"}

  headers = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  jess_dict2 = json.loads(response.text)
  if jess_dict2['status']==True:
      return jess_dict2
  return "false"


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

#addddd 
def getchaininformations(id):
  url = "https://youtube-media-downloader.p.rapidapi.com/v2/channel/details"

  querystring = {"channelId":id}

  headers = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  print(response.text)
  jess_dict2 = json.loads(response.text)
  if jess_dict2['status']==True:
      return jess_dict2
  return "false"

def getlinkfromid(id):
  url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
  querystring = {"id":id}
  headers = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
  }
  response2 = requests.request("GET", url, headers=headers, params=querystring)
  jess_dict2 = json.loads(response2.text)
  if jess_dict2['status']=="OK":
      return jess_dict2['formats'][2]['url']
  return "false"

def getvideosfromuser(id):
  url = "https://youtube-media-downloader.p.rapidapi.com/v2/channel/videos"
  querystring = {"channelId":id}
  headers = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  jess_dict2 = json.loads(response.text)
  if jess_dict2['status']==True:
      return jess_dict2
  return "false"

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search/songs/{item_id}")
def searsh(item_id: str, q: Union[str, None] = None):
        mylist=getlist(item_id)['items']
        i=0
        finalelist=[]
        while (i<10 and i+1<len(mylist)):
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

@app.get("/search2/songsbyuserid/{item_id}")
def searsh2(item_id: str, q: Union[str, None] = None):
  
        jess_dict2=getchaininformations(item_id)
        mylist=getvideosfromuser(item_id)
        if jess_dict2!="false" and mylist!="false" :
          i=0
          finalelist=[]
          while (i<15 and i+1<len(mylist['items'])):
              mine={
              "songid":mylist['items'][i]['id'],
              "songname":mylist['items'][i]['title'],
              "userid":str(item_id),
              "trackid":mylist['items'][i]['id'],
              "duration":str(mylist['items'][i]['lengthText']),
              "cover_image_url":mylist['items'][i]['thumbnails'][0]['url'],
              "first_name":jess_dict2['name'],
              "last_name":str(mylist['items'][i]['viewCountText'])
              }
              finalelist.append(mine)
              i=i+1
          return {"results":finalelist }
        else:
          mine={
              "songid":"none",
              "songname":"none",
              "userid":"none",
              "trackid":"none",
              "duration":"none",
              "cover_image_url":"none",
              "first_name":"none",
              "last_name":"none"
              }
          return {"results":[{"songid":"zN_GNb_QXKk","songname":"Rick Astley - Either Way (Chris Stapleton Cover)","userid":"UCuAXFkgsw1L7xaCfnd5JJOw","trackid":"zN_GNb_QXKk","duration":"2:53","cover_image_url":"https://i.ytimg.com/vi/zN_GNb_QXKk/hqdefault.jpg?sqp=-oaymwE1CKgBEF5IVfKriqkDKAgBFQAAiEIYAXABwAEG8AEB-AG2CIAC0AWKAgwIABABGEggWihlMA8=&rs=AOn4CLB6NBLu-Lm9bnygyv_GmWg3Hm5K8g","first_name":"Rick Astley","last_name":"247,817 views"},{"songid":"LLFhKaqnWwk","songname":"Rick Astley - Never Gonna Give You Up (Official Animated Video)","userid":"UCuAXFkgsw1L7xaCfnd5JJOw","trackid":"LLFhKaqnWwk","duration":"3:33","cover_image_url":"https://i.ytimg.com/vi/LLFhKaqnWwk/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBvqKlqVycRo8izPhuzpQqeE9TINA","first_name":"Rick Astley","last_name":"2,618,019 views"},{"songid":"rZlQ28OeGMI","songname":"Rick Astley – My Arms Keep Missing You (Official Audio)","userid":"UCuAXFkgsw1L7xaCfnd5JJOw","trackid":"rZlQ28OeGMI","duration":"3:15","cover_image_url":"https://i.ytimg.com/vi/rZlQ28OeGMI/hqdefault.jpg?sqp=-oaymwE1CKgBEF5IVfKriqkDKAgBFQAAiEIYAXABwAEG8AEB-AH-CYAC0AWKAgwIABABGGUgXyhCMA8=&rs=AOn4CLCkobrNepIb2MMggjtChmPmZvsYzw","first_name":"Rick Astley","last_name":"339,816 views"}]}

@app.get("/artistbyid/{item_id}")
def artistbyid(item_id: str, q: Union[str, None] = None):
        jess_dict2=getchaininformations(item_id)
        if jess_dict2!="false":
          mine={
              "id":str(item_id),
              "username":str(item_id),
              "first_name":jess_dict2['name'],
              "last_name":jess_dict2['subscriberCountText'],
              "email":jess_dict2['isVerified'],
              "city":jess_dict2['country'],
              "avatar":jess_dict2['avatar'][3]['url'],
              }
          return {"results":mine }
        else:
          m={"id":"UCuAXFkgsw1L7xaCfnd5JJOw","username":"Rick Astley","first_name":"Rick Astley","last_name":"3.49M subscribers","email":"true","city":"United Kingdom","avatar":"https://yt3.ggpht.com/BbWaWU-qyR5nfxxXclxsI8zepppYL5x1agIPGfRdXFm5fPEewDsRRWg4x6P6fdKNhj84GoUpUI4=s900-c-k-c0x00ffffff-no-rj"}
          return {"results":m }
@app.get("/search/artist/{item_id}")
def searsh(item_id: str, q: Union[str, None] = None):
  mylist=channelsearch(item_id)
  if mylist!="false":
          i=0
          finalelist=[]
          while (i<100 and i+1<len(mylist['items'])):
              if (mylist['items'][i]['isVerified']==True):
                mine={
                "avatar":mylist['items'][i]['avatar'][1]['url'],
                "first_name":mylist['items'][i]['id'],
                "last_name":mylist['items'][i]['id'],
                "username":mylist['items'][i]['id'],
                }
                finalelist.append(mine)
              i=i+1
  return {"results":finalelist }

@app.get("/gotolink/{item_id}")
async def gotolink(item_id: str, q: Union[str, None] = None):
    link=getlinkfromid(item_id)
    if link!="false":
        response = RedirectResponse(url=link,status_code=303)
    else:
        response = RedirectResponse(url="https://drive.google.com/uc?id=1ixtBSHFEMH9zyDkRNLU79hYSpA5ZHAd&export=download",status_code=303)

    return response

@app.get("/album/{item_id}")
def album(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
