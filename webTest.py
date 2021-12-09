from urllib import request
from bs4 import BeautifulSoup
import requests

url = "http://openapi-lib.sen.go.kr/openapi/service/lib/openApi?serviceKey=0Yid8kPxBKOwFYM8goFzmvf6h9Ot3a1H5Iszap8TengJuLyK4A2HOCxWD8XSJ5ulIvFq06/deAnPd/27aYo3IQ==&pageNo=2&numOfRows=5&manageCd=MB&title=1"

data = request.urlopen(url).read().decode('utf-8', 'replace')
soup = BeautifulSoup(data, 'html.parser')

print(soup)
