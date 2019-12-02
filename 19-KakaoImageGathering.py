#!/usr/bin/env python
# coding: utf-8

# ## 카카오 Open Api를 연동한 이미지 수집

# In[9]:


import requests
import json               # 파이썬 기본 모듈
import urllib             # 파이썬 기본 모듈(인코딩용)
import os
import datetime as dt
import pandas as pd       
from pandas import DataFrame


# In[10]:


# 발급받은 API Key
api_key = "30a761afcc79bb6ade8491698aa45b78"


# In[11]:


# 검색어
q ="Emily Ratajkowski"


# In[12]:


# 접근할 페이지번호(1~50)
page = 1


# In[13]:


# 가져올 데이터 수(1~80)
size = 80


# In[14]:


# 검색주소 샘플 --> 카카오 개발자가이드의 예시에 있음 : https://developers.kakao.com/docs/restapi/search#이미지-검색
url_tpl = "https://dapi.kakao.com/v2/search/image"


# # 인터넷 주소에는 한글이나 공백이 포함될 수 없기 때문에 검색어에 대해 인코딩 처리를 수행해야 한다.
# (아래에는 다음에서 파이썬으로 검색한 이미지의 예) - 즉 윤아로 검색하려면 '윤아'를 인코딩해줘야 함
# 
# (아래의 주소는 실제 다음에서 파이썬을 검색했을때의 예이다. 그런데 API로 검색해오려면 카카오 가이드에 따라서 가져와야 한다)
# 
# (카카오 API에서 검색한 결과는 다음에서 가져온 결과와 같을 것이다)
# 
# <파이썬>
# 
# https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 
# https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=파이썬
# 
# 
# <윤아>
# 
# https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%9C%A4%EC%95%84
# 
# https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=윤아

# In[15]:


# 이미지가 저장될 폴더의 이름 만들기
datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")
dirname = "%s_%s" % (q, datetime)
dirname


# In[16]:


# 폴더 생성하기
if not os.path.exists(dirname):
    os.mkdir(dirname)


# In[17]:


# 접속 세션 만들기
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"

session = requests.Session()

# 인증키를 header에 포함시켜야 함 "kakaoAK" 뒤에 공백 추가 주의
session.headers.update({'User-agent':user_agent, 'referer':None, 'Authorization': 'KakaoAK ' + api_key})


# In[18]:


# 인터넷 주소에는 !~~~
params = {"page":page, "size":size, "query":q}
query = urllib.parse.urlencode(params)


# In[19]:


# 최종 접속 주소
api_url = url_tpl + "?" + query
api_url


# In[20]:


# API에 접근하여 데이터 가져오기
r = session.get(api_url)

if r.status_code != 200:
    print("[%d Error] $s" % (r.status_code, r.reason))
    quit()
    
# 가져온 결과를 딕셔너리로 변환
r.encoding = "utf-8"
image_dict = json.loads(r.text)
image_dict


# In[21]:


# 딕셔너리 중에서 검색 결과에 해당하는 documents에 대한 부분을 DataFrame으로 변환
image_df = DataFrame(image_dict['documents'])
image_df


# In[22]:


# 저장되는 이미지 파일의 수를 카운트 하기 위한 변수
count = 0

# 이미지 주소에 대해서만 반복
for image_url in image_df['image_url']:
    # 카운트 증가
    count += 1
    
    # 파일이 저장될 경로 생성
    path = "%s/%04d.jpg" % (dirname,count)
    
    print( "[%s] >> %s" % (path, image_url))
    
    # 이미지 주소를 다운로드를 위해 stream 모드로 가져온다
    r = session.get(image_url, stream=True)
    
    # 에러 발생시 저장이 불가능하므로 건너뛰고 반복의 조건식으로 이동
    if r.status_code != 200:
        print("########> 저장실패")
        continue # 중간에 실패한 것이 생겨도 계속 가져오기 위해
    
    # 추출한 데이터를 저장
    # -> 'w' : 텍스트 쓰기 모드, 'wb' : 바이너리(이진값)
    with open(path, 'wb') as f:
        f.write(r.raw.read())
        print("------------> 저장성공")


# In[23]:


# 아래의 것은 secession 만 빼고 한버에 가져오기 위한 코딩이다
# 저장되는 이미지 파일의 수를 카운트 하기 위한 변수
count = 0

for p in range(1,4): #3*80 = 240장개 가져옮 
    # 인터넷 주소에는 한글이나 공백이 포함될 수 없기 때문에 검색어에 대해 인코딩 처리를 수행해야 한다
    params = {"page":p, "size":size, "query":q}
    query = urllib.parse.urlencode(params)

    # 최종 접속 주소
    api_url = url_tpl + "?" + query
    api_url

    # API에 접근하여 데이터 가져오기
    r = session.get(api_url)

    if r.status_code != 200:
        print("[%d Error] $s" % (r.status_code, r.reason))
        quit()

    # 가져온 결과를 딕셔너리로 변환
    r.encoding = "utf-8"
    image_dict = json.loads(r.text)
    image_dict

    # 딕셔너리 중에서 검색 결과에 해당하는 documents에 대한 부분을 DataFrame으로 변환
    image_df = DataFrame(image_dict['documents'])
    image_df




    # 이미지 주소에 대해서만 반복
    for image_url in image_df['image_url']:
        # 카운트 증가
        count += 1

        # 파일이 저장될 경로 생성
        path = "%s/%04d.jpg" % (dirname,count)

        print( "[%s] >> %s" % (path, image_url))

        # 이미지 주소를 다운로드를 위해 stream 모드로 가져온다
        r = session.get(image_url, stream=True)

        # 에러 발생시 저장이 불가능하므로 건너뛰고 반복의 조건식으로 이동
        if r.status_code != 200:
            print("########> 저장실패")
            continue # 중간에 실패한 것이 생겨도 계속 가져오기 위해

        # 추출한 데이터를 저장
        # -> 'w' : 텍스트 쓰기 모드, 'wb' : 바이너리(이진값)
        with open(path, 'wb') as f:
            f.write(r.raw.read())
            print("------------> 저장성공")


# In[ ]:




