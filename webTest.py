from urllib import request
from bs4 import BeautifulSoup


url = "http://openapi-lib.sen.go.kr"

data = request.urlopen(url)
soup = BeautifulSoup(data, 'html.parser')

for loc in soup.select('location') :
    print("도시 : ", loc.select_one('city').string, end = ", ")
    print("날씨 : ", loc.select_one('wf').string, end = ", ")
    print("최저기온 : ", loc.select_one('tmn').string, end = ", ")
    print("최고기온 : ", loc.select_one('tmx').string)

print()