#!/usr/bin/python3

#	This program  reads acceleration data in units of G
#
#	http://ozzmaker.com/
#   [*] This program is a modified version of berryIMU.py provided
#   by ozzmaker and found on the berryIMU git repo
#
#    Copyright (C) 2016  Mark Williams
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Library General Public
#    License as published by the Free Software Foundation; either
#    version 2 of the License, or (at your option) any later version.
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    Library General Public License for more details.
#    You should have received a copy of the GNU Library General Public
#    License along with this library; if not, write to the Free
#    Software Foundation, Inc., 59 Temple Place - Suite 330, Boston,
#    MA 02111-1307, USA

import smbus
from LSM9DS0 import *
import time
from netcat.sender import Netcat
import sys

bus = smbus.SMBus(1)


def writeACC(register, value):
    bus.write_byte_data(ACC_ADDRESS, register, value)
    return -1


def readACCx():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_X_L_A)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_X_H_A)
    acc_combined = (acc_l | acc_h << 8)

    return acc_combined if acc_combined < 32768 else acc_combined - 65536


def readACCy():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Y_L_A)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Y_H_A)
    acc_combined = (acc_l | acc_h << 8)

    return acc_combined if acc_combined < 32768 else acc_combined - 65536


def readACCz():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Z_L_A)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Z_H_A)
    acc_combined = (acc_l | acc_h << 8)

    return acc_combined if acc_combined < 32768 else acc_combined - 65536


# initialise the accelerometer
writeACC(CTRL_REG1_XM, 0b01100111)  # z,y,x axis enabled, continuos update,  100Hz data rate
writeACC(CTRL_REG2_XM, 0b00011000)  # +/- 8G full scale

target = str(sys.argv[1])
loop = True
while loop:
    # Read the accelerometer,gyroscope and magnetometer values
    # Establish NC connection
    # When spike occurs send command to run wav file
    x = Netcat()
    # x.netcat(target='target', port=9999)
    # change netcat func to use variable as obj were sending
    try:
        ACCx = (readACCx() * 0.244) / 1000
        ACCy = (readACCy() * 0.244) / 1000
        ACCz = (readACCz() * 0.244) / 1000


        if ACCx >= 2 or ACCy >= 2 or ACCz >= 2:
            var = "./src/chuck playwav.ck"
            #send cmd
            x.netcat(target=target, port=9990, buf=var)
            time.sleep(1)

    except KeyboardInterrupt:
        var = 'quit'
        x.netcat(target=target, port=9990, buf=var)
        print('We exited the session')
        sys.exit(0)
    # print("##### X = %f G  #####" % ((ACCx * 0.244) / 1000)),
    # print(" Y =   %fG  #####" % ((ACCy * 0.244) / 1000)),
    # print(" Z =  %fG  #####" % ((ACCz * 0.244) / 1000))

    # slow program down a bit, makes the output more readable
    #time.sleep(0.03)
