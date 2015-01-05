__author__ = 'vijayadurga'

import RPi.GPIO as GPIO
import time
#using rpi board pin numbering
GPIO.setmode(GPIO.BOARD)
#setting up boardpins as out
#for rpi rev 2 gpio (3,5,7,8,10,12,11,13,15,16,18,19,21,22,23,24,26)

HH = [3,5,7,8,10]
MM = [11,12,13,15,16,18]
SS = [19,21,22,23,24,26]


def computeTime():
    """computes binary value of time"""
    bhrs = bin(int(time.strftime('%H'))).lstrip('0b')
    bmins = bin(int(time.strftime('%M'))).lstrip('0b')
    bsecs = bin(int(time.strftime('%S'))).lstrip('0b')

    hrs = [i for i in bhrs]
    hrs = ['0']*(5-len(hrs))+hrs

    mins = [i for i in bmins]
    mins = ['0']*(6-len(mins))+mins

    secs = [i for i in bsecs]
    secs = ['0']*(6-len(secs))+secs

    return hrs,mins,secs
    
def glowLED():
    """GPIO operation,configures all the gpios as outs"""
    for i in HH+MM+SS: #set all relevant pins as OUT pins:
        GPIO.setup(i,GPIO.OUT)
    #entering an infinite loop for the clock to run always
    while True:
        hh,mm,ss = computeTime()
        # lit the hh led rows on pins 3,5,7,8,10
        for h in zip(hh,HH): # i = (hh[0],3)/(hh[1],5)/(hh[2],7)/(hh[3],8)/(hh[4],10)
            if h[0]== '1':#if hrs bit is ON, switch on the corresponding led
                GPIO.output(h[1],True)
            elif h[0] == '0':
                GPIO.output(h[1],False)
        
        # lit the mm led rows on pins 11,12,13,15,16,18
        for m in zip(mm,MM):# i = (mm[0],11)/(mm[1],12)/(mm[2],13)/(mm[3],15)/(mm[4],16)/(mm[5],18)
            if m[0] == '1':
                GPIO.output(m[1],True)
            elif m[0] == '0':
                GPIO.output(m[1],False)
            
        # lit the ss led rows on pins 19,21,22,23,24,26
        for s in zip(ss,SS):#s (ss[0],19),(ss[1],21),(ss[2],22),(ss[3],23),(ss[4],24),(ss[5],26)
            if s[0] == '1':
                GPIO.output(s[1],True)
            elif s[0] == '0':
                GPIO.output(s[1],False)
            print s
    GPIO.cleanup()

glowLED()
