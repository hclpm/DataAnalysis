import requests
from bs4 import BeautifulSoup

import json
import time

KAKAO_TOKEN = "????"

def get_price(code):
    # html 파일을 가져올 url 입력
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    # url 내의 html 파일 가져오기
    result = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    # 가져온 html 파일을 계층구조를 유지하며(beautifulsoup 기능, =파싱) 추출
    bs_obj = BeautifulSoup(result.content, "html.parser")
    # 파싱한 내용에서 태그가 "em"인 것들 중에 "class"가 no_down인 것 추출(no_down 클래스 내용 추출)
    no_down = bs_obj.find("p", {"class": "no_today"})
    # no_down클래스에서 태그가 "span"인 것들의 내용을 가져와서 text 형태 데이터만 추출
    price = (no_down.find("span")).get_text()
    return price
def get_name(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    result = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    bs_obj = BeautifulSoup(result.content, "html.parser")
    wrap_company = bs_obj.find("a", {"onclick" :"clickcr(this, 'sop.title', '', '', event);window.location.reload();"})
    cName = wrap_company.get_text()
    return cName

def sendMessageToMe(name, price):
    header = {"Authorization" : "Bearer " + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type" : "text",
        "text" : (f"[{name}] 현재 주가: {price}"),
        "link" : {
            "web_url" : "https://developers.kakao.com",
            "mobile_web_url" : "https://developers.kakao.com"
        },
        "button_title" : "바로 확인"
    }
    data = {"template_object" : json.dumps(post)}
    return requests.post(url, headers=header, data = data)

code = input("종목 코드를 입력하세요: ")
name = get_name(code)
price = get_price(code)
sendMessageToMe(name, price)
