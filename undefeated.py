#!/usr/bin/env python3


from ev3dev.ev3 import *
from time import sleep

speed=80
Err = 0
clL = ColorSensor("in1")
assert clL.connected, "Подключите датчик цвета EV3 in1"
clR = ColorSensor("in4")
assert clR.connected, "Подключите датчик цвета EV3 in4"
# Переводим датчик в режим измерения освещенности
# в этом режиме датчик выдает освещенность 0..100%
clL.mode='COL-REFLECT'
clR.mode='COL-REFLECT'
ts = TouchSensor("in2")
assert ts.connected, "Подключите датчик касания в любой порт"
# проверка, подключен ли датчик
# программа завершится с сообщением, если датчик не подключен

motorLeft = LargeMotor('outD')
assert motorLeft.connected, 'Connect Left motor in  port D'
motorRight = LargeMotor('outC')
assert motorRight.connected, 'Connect Right motor in  port C'



Err=(clL.value()-clR.value())

while not ts.value():
   sleep(0.1)

colorWhiteR=clR.value()
print(colorWhiteR)

sleep(1)

while not ts.value():
    sleep(0.1)

colorWhiteL=clL.value()
print(colorWhiteL)

Err=(clL.value()-clR.value())
print (Err)

sleep(0.1)

while True:
    delta = clL.value() - clR.value() + Err
    motorLeft.run_forever (speed_sp = speed + delta)
    motorRight.run_forever(speed_sp = speed - delta)
    sleep(0.1)

motorLeft.stop()
motorRight.stop()







