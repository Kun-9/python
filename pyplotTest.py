from os import access
import matplotlib.pyplot as plt
import numpy as np
import csv


f = open('csvTest.csv','r')
data = csv.reader(f)

data = np.genfromtxt('csvTest.csv', delimiter=',')


year = np.array([])
acc = np.array([])
die = np.array([])
hurt = np.array([])
for row in data:
    year = np.append(year, row[0:1])
    acc = np.append(acc, row[1:2])    
    die = np.append(die, row[2:3])    
    hurt = np.append(hurt, row[3:4])    
print(year)
print(acc)
print(die)
print(hurt)

f.close()

plt.figure(figsize=(40, 12))

xlen = np.arange(len(year))/2

width = 0.3

plt.bar(xlen, acc, width)
# plt.bar(xlen, die, width)
# plt.bar(xlen, hurt, width)

# plt.xticks(year, xlen)

plt.show()

