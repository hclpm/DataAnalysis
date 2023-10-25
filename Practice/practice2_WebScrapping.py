import requests
from bs4 import BeautifulSoup

# 입력한 url의 데이터 확보
url = "https://m.stock.naver.com/worldstock/stock/AAPL.O/total"
result = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
# 추출한 html 데이터를 파싱(모듈(html5lib, html.parser, lxml)을 사용하여 html 계층 구조를 반영함)

html_parsed = BeautifulSoup(result.content, "html.parser")
scrap1 = html_parsed.find("body", {"class": "international"})
scrap2 = scrap1.find("div", {"id": "root"})

print(scrap2.prettify())      # 보기 좋게 출력해주는 함수

# /html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/strong