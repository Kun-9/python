from urllib import request
from bs4 import BeautifulSoup


url = "http://openapi-lib.sen.go.kr"

data = request.urlopen(url)
soup = BeautifulSoup(data, 'html.parser')



print("hello")
