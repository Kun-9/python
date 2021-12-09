import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("인구.csv", delimiter=',')
dataArr = data[2:]

print("연도별 인구 합계")
print("-"*15)

for i in dataArr :              # 연도별 인구수 합계 출력
    print('{0:g}년: {1:g}명'.format(*i[0:1],*(i[1:2] + i[2:3])))
    

years = data[2:,0]
man = data[2:,1]
woman = data[2:,2]

xrange = np.arange(len(years))  # x축 범위
width = 0.3                     # 그래프 넓이, 간격

plt.bar(xrange + width, woman+man, width, label="woman + man")
plt.bar(xrange, man, width, label="man")
plt.bar(xrange - width, woman, width, label="woman")

plt.xticks(xrange, years)
plt.xlabel("year")
plt.ylabel("population")
plt.ylim(20000, 70000)          # y축 표시 범위
plt.legend()                    # 축 설명
plt.grid(True)
plt.show()
    
