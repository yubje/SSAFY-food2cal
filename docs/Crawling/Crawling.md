# Crawling



## Web Crawling이란?

> 웹상에 존재하는 정보들을 수집하는 작업을 말한다.



* 웹 크롤링 방법

  * 오픈 API를 활용해 받은 데이터중 필요한 데이터만 사용하는 방법
  * HTML 소스를 가져와서 원하는 정보를 사용하는 방법
  * 브라우저를 조작해 원하는 정보를 사용하는 방법

  

* 웹 크롤러의 간단한 구조

  ![crawler_architecture](Crawling.assets/crawler_architecture.png)

  * Frontier: 탐색할 URL을 Fetcher에게 넘겨 준다
  * Parser: 다른 하이퍼링크를 찾는다.
  * Fetcher:Frontier에게 URL을 받아 해당 페이지의 html 내용을 가져와서 Parser에게 넘겨준다

  [참고](https://velog.io/@mowinckel/%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-I)

  

## Python + BeautifulSoup

  > 파이썬 크롤링은 Selenium, Scrapy, BeautifulSoup 등을 일반적으로 사용하며, 프로젝트에서는 BeautifulSoup을 사용하였다. 



### 1. 네이버 크롤링

#### 1-1. 검색할 데이터 불러오기

```python
import pandas as pd

nutrition = pd.read_excel('../datasets/nutrition.xlsx', usecols='B,F')
food_names = nutrition['식품명']
```

* `read_excel()`: 엑셀 파일을 불러온다. `usecols`를 지정하면 원하는 열만 불러와 로딩 시간을 단축할 수 있다.



#### 1-2. 데이터 파싱하기

```python
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

for j in range(len(food_names)):
  keyword = food_names.iloc[j]
  crawl_num = 50
  
  url = baseUrl + quote_plus(keyword) # 한글 검색 자동 변환
  html = urlopen(url)
  soup = bs(html, "html.parser")
  img = soup.find_all(class_='_img')
  
  ...
```

* `quote_plus()`: 한글 검색을 자동 변환해준다. URL로 이동하기 위한 쿼리 문자열을 만들 때 HTML 폼값을 인용하는 데 필요한 대로 스페이스를 더하기 부호로 치환하기도 한다.  Ex) `quote_plus('/El Niño/')` =>  `'%2FEl+Ni%C3%B1o%2F'`
* `urlopen()`: url을 열어주는 함수
* `bs(html, "html.parser")`: html 파싱. `"html.parser"`를 지정해 주어야 한다.
* `.find_all(class_='_img')`: `<img>` 태그를 찾아온다.



#### 1-3. 저장 디렉토리 확인 및 지정

```python
import os

...

  for i in img:
    dir_path = '../datasets/images/'+keyword
    try:
      if not(os.path.isdir(dir_path)):
        os.makedirs(os.path.join(dir_path))
    except OSError as e:
      print('Error: Creating directory. ' + dir_path)
```

* try except 문으로 에러 처리
* `os.path.isdir(dir_path)`: 디렉토리 유무 확인
* `os.path.join(dir_path)`: 파일 경로 생성 
* `os.makedirs(os.path.join(dir_path))`: 생성된 경로에 디렉토리 생성




#### 1-4. 이미지 저장

```python
imgUrl = i['data-source']
with urlopen(imgUrl) as f:
  with open(dir_path+'/'+ keyword+str(n)+'.jpg','wb') as h: # w - write b - binary
    img = f.read()
    h.write(img)
```

* `i['data-source']` : `<img>`태그에 저장된 `data-source`, 즉 이미지 데이터를 불러온다.
* url을 열고, 지정한 규칙대로 이미지 파일을 binary형태로 작성한다. 





### 2.  ~~구글 크롤링(구버전)~~

[신버전 보러가기](#3.-구글-크롤링(신버전)) (ctrl + 클릭)



```python
# 필요한 라이브러리
$ pip install pandas
$ pip install git+https://github.com/Joeclinton1/google-images-download.git
```

* 현재 공식문서 버전 라이브러리는 다운로드가 막힌 상태, 이를 한 외국인이 공식 레포를 포크떠서 해결한 깃이 있어 이것으로 다운받아 사용한다.



* 이와 같은 과정으로 크롤링을 실행한다.

![image-20200910091002925](C:\Users\multicampus\Desktop\특화프로젝트\s03p22a411\docs\Crawling\Crawling.assets\image-20200910091002925.png)

1. 사용할 사람이 자기에게 맞는 쿼리를 짜서 검색

2. Raw HTML을 텍스트 형식으로 받아옴
3. 구글이 사용하는 검색된 이미지 클래스명을 갖는 img 태그의 src, data-src 뒤에 링크를 긁어온다. (이 부분에서 구글이 이미지 클래스명을 일치하지 않게 흩어 놓아서 정상적으로 검색되지 않는 경우가 존재한다.)
4. 긁어서 모은 url을 이용해 이미지 다운로드!



#### 2.1 검색할 데이터 불러오기

```python
data = pd.read_excel('../datasets/nutrition.xlsx', usecols='F')
df_sample = data.loc[:, '식품명']
```

* `read_excel()`: 엑셀을 불러오는 함수로 pandas 라이브러리에서 xlrd라는 라이브러리에 의존성을 갖고 있다. 사용하기 위해 xlrd 라이브러리를 다운받아야 한다.
* `.loc`: 첫번째 인자는 행의 범위, 두번째 인자는 열의 범위를 지정하는 것으로 read_excel()의 리턴값이 ()로 싸여있기에 리스트 형식으로 바꾼다.



#### 2.2 클래스 선언 및 arguments 정보 입력

```python
response = google_images_download.googleimagesdownload()
arguments = {"keywords": i, "limit": 50, "print_urls": True}
```

* keywords: 검색할 키워드
* limit: 검색할 이미지 개수
* print_urls: 다운로드 받기전에 콘솔창에 url 주소를 출력해줄지 여부



* `google_images_download.googleimagesdownload() `

```python
# Downloading entire Web Document (Raw Page Content)
    def download_page(self,url):
        version = (3, 0)
        cur_version = sys.version_info
        if cur_version >= version:  # If the Current Version of Python is 3.0 or above
            try:
                headers = {}
                headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                req = urllib.request.Request(url, headers=headers)
                resp = urllib.request.urlopen(req)
                respData = str(resp.read())
                return respData
            except Exception as e:
                print("Could not open URL. Please check your internet connection and/or ssl settings \n"
                      "If you are using proxy, make sure your proxy settings is configured correctly")
                sys.exit()
            # except:
			# Python 버전 3.0 미만인 경우
```



#### 2.3 이미지 다운로드 시작

```python
paths = response.download(arguments)
```

* github 원본 주소에 따르면 코드 지속성을 위해 arguments를 따로 입력해서 넣어주었다고 서술되어 있다. arguments를 따로 입력해서 홈페이지의 리빌딩이나 리팩터링에 따라 변할 수 있는 클래스명에 바꿀 수 있게 한 것으로 보임.

* `response.download(arguments)`

  url 존재 여부, 다운로드 성공 여부에 따라 try, except로 예외 처리가 되어 있다. 에러가 났을 경우 어떤 에러가 나서 이미지를 받는데 실패했는지 콘솔로 찍어줌

  

### 3. 구글 크롤링(신버전)

* 구버전 이슈

  구글 검색결과의 이미지 탭은 20~30개 정도의 결과를 주는데 이미지 결과를 50개 이상 받아보기 위해서 무한 스크롤 이벤트를 발생시켜야할 필요가 있었다.

* 해결 방안

  1. selenium의 webdriver를 이용해 자동화 테스트를 시켜서 검색한 뒤 이미지 탭 클릭
  2. 무한 스크롤 이벤트를 발생시키기 위해 페이지 로드를 기다리면서 여러번 반복한다.
  3. HTML 파일을 String 형식으로 저장한 뒤 기존과 같은 방법으로 추출

```python
# 설치해야하는 라이브러리
$ pip install pandas selenium bs4 xlrd
```



#### 3-0. 사용하는 라이브러리

```python
# 내장함수
from urllib.request import urlopen
# HTML문서에서 원하는 태그 수집하기 위한 모듈
from bs4 import BeautifulSoup
# 엑셀 읽어오기 위한 모듈
import pandas as pd
# 디렉토리 생성, 확인 모듈
import os
# 무한 스크롤 이벤트 만들어주기 위한 모듈
from selenium import webdriver # 브라우저를 띄우기 위해서 필요
from selenium.webdriver.common.keys import Keys # 키이벤트를 주기 위해 필요
import time # 스크롤 텀을 주기 위해 필요
```



#### 3-1. 엑셀 데이터 읽어오기

```python
# 엑셀 읽어오기 위한 모듈
import pandas as pd
data = pd.read_excel('../datasets/nutrition.xlsx', usecols='F')
df_sample = data.loc[:, '식품명']

# 반복문으로 모든 식품명 검색하기
for i in df_sample:
    # 양 끝 공백 제거
    i = i.strip()
    crawling(i)
```



#### 3-2. 구글 이미지 검색 결과 가져오기 (1)

* 주의사항

  webdriver.Chrome안에 있는 경로는 webdriver가 실행할 크롬 버전을 다운받아서 저장해 둔 곳이다.

  https://chromedriver.chromium.org/downloads 이 링크에서 다운받을 수 있으며

  크롬 브라우저의 경우, 주소에 `chrome://version/`를 쳐서 현재 사용하는 버전을 확인할 수 있다.

```python
# 검색하기 위해 사용할 주소
url_info = "https://www.google.co.kr/search?"

# crawling 함수
def crawling(keyword):
    print(keyword, len(keyword))
    # 사용한 구글 url 예시: https://www.google.co.kr/search?q=%EB%B2%A4&tbm=isch
    # 로컬에 저장할 디렉토리 주소
    dir_path = '../datasets/images/' + keyword

    # driver 실행 과정
    driver = webdriver.Chrome('/Users/dev/chromedriver')     # 크롬 브라우저 선택
    driver.implicitly_wait(10)                               # 페이지 로드를 기다림
    driver.get(url_info)                                     # 입력한 경로의 사이트를 띄운다.(구글)
    driver.find_element_by_name("q").send_keys(keyword)      # 검색창에 검색어 입력
    driver.find_element_by_name("q").send_keys(Keys.RETURN)  # 검색창에서 엔터 누르기
    driver.implicitly_wait(10)                               # 페이지 로드를 기다림
    # driver.find_element_by_class_name("qs").click()		# 이슈-1 발생
    # (이슈-1) 검색결과 옆에 탭이 이미지가 아니라 지도가 나오는 경우가 있어서 아랫줄로 바꿈
    driver.find_element_by_link_text("이미지").click()		  # a 태그안에 이미지라고 써진 탭을 클릭
    body = driver.find_element_by_css_selector('body')  # send_keys()메서드 사용을 위해 body 가져오기
    for i in range(12):
        body.send_keys(Keys.PAGE_DOWN)  # 페이지 다운 키 누르기
        time.sleep(0.2)                 # 페이지 로드 대기시간
    html_result = driver.page_source    # html을 문자열로 저장
    driver.close()  # 크롬드라이버 닫기
    
    
	# 인스턴스 생성
    bs_object = BeautifulSoup(html_result, "html.parser")
    # img 태그들을 전부 모아 반환, limit 인자에 원하는 개수 입력(모았을 때 51개가 되면 넣지 않고 반환해서 50개)
    img_data = bs_object.find_all("img", limit=51)
    
	# (3-3)으로 이동 -> for문
```



#### 3-3. 구글 이미지 검색 결과 가져오기 (2)

```python
    # 뽑아서 모아온 이미지 태그들 반복문
    for i in enumerate(img_data[1:]):
        # img 태그의 src안에 있는 url을 읽어온다.
        try:
            t = urlopen(i[1].attrs['src']).read()
        # src가 없거나, 정상적인 url이 아닌경우, 페이지가 없어서 이미지가 없는 경우 등 다양한 에러가 발생
        except Exception as ex:
            print('에러 발생', ex)
            continue

        # 파일명 지정
        filename = str(keyword).lstrip() + str(i[0]+1)+'.jpg'

        # 파일 확인 조건문
        try:
            if not (os.path.isdir(dir_path)):
                os.makedirs(os.path.join(dir_path))
        except OSError as e:
            print('Error: Creating directory. ' + dir_path)

        # 이미지 파일 작성
        with open(dir_path + '/' + filename,"wb") as f:
            f.write(t)
        print("Img Save Success: " + filename)
```

