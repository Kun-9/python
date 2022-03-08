import serial
import numpy as np
import time as tm

x = 500
y = 500
z = 500

class p:
    global x 
    global y
    global pre_x
    global pre_y
    global maxNum
    global minNum
    global X_LEN
    global Y_LEN
    def __init__(self, x, y, minNum, maxNum, X_LEN, Y_LEN):
        self.x = x
        self.y = y
        self.maxNum = maxNum
        self.minNum = minNum
        self.pre_x = self.x
        self.pre_y = self.y 
        self.X_LEN = X_LEN
        self.Y_LEN = Y_LEN
    
def creatXY() :
    arr = np.full((p.X_LEN, p.Y_LEN), " ")    
    arr[:, 0] = "*"
    arr[:, -1] = "*"
    arr[:1] = "*"
    arr[-1:] = "*"
    return arr

class move:
    def up(self):
        if(int(y) > p.maxNum):   
            if (p.x > 1):
                p.x -= 1
                return True
    def down():
        if(int(y) < p.minNum):
            if (p.x < p.X_LEN - 2):
                p.x += 1
                return True
    def left():
        if(int(x) < p.minNum):    
            if (p.y > 1):
                p.y -= 1
                return True
    def right():
        if(int(x) > p.maxNum): 
            if (p.y < p.Y_LEN - 2):
                p.y += 1
                return True
    def reset():
        if(int(z) == 0):            
            p.pre_x = p.x
            p.pre_y = p.y
            p.x = 4
            p.y = 5
            return True
    ## 좌표값으로 배열 출력##
    def print():            
        print("b", p.pre_x, p.pre_y)        # 이전 좌표 출력
        print("p", p.x, p.y)                # 현재 좌표 출력
        print("x :",x ,"y :",y ,"z :",z)    # 조이스틱 xyz값 출력
            
        arr[p.pre_x, p.pre_y] = " "
        arr[p.x, p.y] = "o"
        
        print(arr)    # 배열 출력
        tm.sleep(0.1)

############ 초기 세팅 ##############
# 초기 위치, 조이스틱 민감도, 배열(필드)크기
p = p(4, 5, 350, 650, 10, 11)

############ 필드 세팅 ##############
arr = creatXY()
move.print()

############ 통신 시작 ###############
sr = serial.Serial('/dev/cu.usbserial-1130', 9600, timeout = 1)

############ 루프 시작 ##############

while True :
    line = sr.readline().decode("utf-8")
    x,y,z = line.split()
    # print(x, y, z)
    
    if(not(p.maxNum > int(x) > p.minNum and p.maxNum > int(y) > p.minNum and int(z) != 0)):
        p.pre_x = p.x
        p.pre_y = p.y
        move.left()
        move.right()
        move.up()
        move.down()
        move.reset()
        move.print()
        
###################################