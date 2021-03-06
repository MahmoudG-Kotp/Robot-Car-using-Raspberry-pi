import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

#  Connection
#2. 5v of H bridge
#7.IN3
#11.IN4
#13.IN2
#15.IN1

def initilization() :
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(7 , gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def Forward(tf) :
    gpio.output(7 ,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()


def Backward(tf) :
    gpio.output(7 ,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def Right(tf) :
    gpio.output(7 ,True)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()

def Left(tf) :
    gpio.output(7 ,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def Stop(tf) :
    gpio.output(7 ,False)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def key_input(event) :
    initilization()
    key_press = event.char
    sleep_time = 0.3
    print 'key:', event.char
    
    if key_press.lower() == 'w':
      Forward(0.1)  
    elif key_press.lower() == 's':
      Backward(0.1)
    elif key_press.lower() == 'a':
      Left(0.1)
    elif key_press.lower() == 'd':
      Right(0.1)
    else :
      Stop(0.1)

command = tk.Tk()
command.bind('<KeyPress>' , key_input)
command.mainloop()
