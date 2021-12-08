import serial
import numpy as np
import time as tm

def move(a, p_x, p_y, b_x, b_y):
    b_pos = (b_x, b_y)
    pos = (p_x, p_y)
        
    a[b_pos] = " "
    a[pos] = "o"
    
    print(a)    # 배열 출력
    print("b", b_x,b_y)
    print("p", p_x, p_y)
    print("xyz", x, y, z)
    tm.sleep(0.1)

sr = serial.Serial('/dev/cu.usbserial-1130', 9600, timeout = 1)
print("통신 시작")

a = np.full((10,10), " ")
a[:, 0] = "*"
a[:, -1] = "*"
a[:1] = "*"
a[-1:] = "*"

x = 500 
y = 500
z = 500

class p:
    global x 
    global y

class b:
    global x
    global x


while True :
    line = sr.readline().decode("utf-8")
    x,y,z = line.split()
    # print(x, y, z)
    
    if(not(950 > int(x) > 50 and 950 > int(y) > 50)):
        b_x = p_x
        b_y = p_y

    if(int(x) < 50):     # left
        if (p_y > 1):
            
            p_y -= 1
        
            move(a, p_x, p_y, b_x, b_y)
        
    elif(int(x) > 950):     # right
        if (p_y < 8):
            
            p_y += 1
            
            move(a, p_x, p_y, b_x, b_y)
                    
    elif(int(y) > 950):     # up
        if (p_x > 1):
            
            p_x -= 1
            
            move(a, p_x, p_y, b_x, b_y)
    elif(int(y) < 50):     # down
        if (p_x < 8):
            
            p_x += 1
        
            move(a, p_x, p_y, b_x, b_y)
    elif(int(z) == 0):
        a[p_x, p_y] = " "
        p_y = 5
        p_x = 5
        a[p_x, p_y] = "o"
        
        print(a)
        print("b", b_x, b_y)
        print("p", p_x, p_y)
        print("xyz", x, y, z)
        tm.sleep(0.1)
        
        
    
            
        