#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

speed = 360
cl = ColorSensor('in4')
assert cl.connected
cl.mode='COL-REFLECT'

us = UltrasonicSensor('in3')
assert us.connected
us.mode='US-DIST-CM'

motorLeft = LargeMotor('outD') #создаём левый мотор
assert motorLeft.connected, 'Connect left motor in  port D'
motorRight = LargeMotor('outC') #создаём правый мотор
assert motorRight.connected, 'Connect right motor in  port C'

ts = TouchSensor('in2')
colorGray = 0
barrierDistance = 50
barrierCount = 0

while not ts.value():
    sleep(0.1)

Sound.beep().wait()
    
colorBlack = cl.value()    #получаем значение черного
print(colorBlack)
    
while not ts.value():       #крутимся в цикле пока не будт нажата какая-либо кнопка на блоке
    sleep(0.1)

Sound.beep().wait()
    
colorWhite = cl.value()     #получаем значение белого
print(colorWhite)
    
colorGray = (colorWhite + colorBlack)/2 
print(colorGray)

motorLeft.run_forever(speed_sp = -speed/2) #поворачивает
motorRight.run_forever(speed_sp = speed/2)

while True:
    distance = us.value()/10 #переводим см в мм
    print(distance) #выдает измерения дистанции
    sleep(0.1)

    if distance < barrierDistance: #если дистанция меньше барьер дистанс, то
        motorLeft.run_forever(speed_sp = speed) #задали скорость -900.900
        motorRight.run_forever(speed_sp = speed) #едет вперед

        while True:
            if colorGray > cl.value():

                motorLeft.stop() #останавливаем моторы
                motorRight.stop()
                sleep(0.1) #небольшая задержка

                motorLeft.run_forever(speed_sp = -speed) #задали скорость -900.900
                motorRight.run_forever(speed_sp = -speed) #едет обратно
                sleep(4)

                motorLeft.run_forever(speed_sp = -speed/2) #поворачивает
                motorRight.run_forever(speed_sp = speed/2)

        barrierCount +=1
        if barrierCount > 4:
            break

motorLeft.stop()
motorRight.stop()

            
