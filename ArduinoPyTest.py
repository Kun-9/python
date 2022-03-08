
from tokenize import Double
import serial
import numpy as np
import time as tm


############ 통신 시작 ###############
sr = serial.Serial('/dev/cu.usbserial-130', 9600, timeout = 1)

############ 루프 시작 ##############

while True :
    line = sr.readline().decode("utf-8")
    # x,y,z = line.split()
    x = line.split()

    print(x)
    # if(len(x) > 0) :
        # if (float(x[0]) > 1.0) :
            # sr.write('c'.encode())
            
    

    
        
###################################