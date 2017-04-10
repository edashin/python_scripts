#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import ctypes

print("0:shutdown, 1:reboot, 2:sleep, 3:hibernation")
ii = input("number: ")
print(ii)
if ii == "0":
    os.system("shutdown -s -f -t 0")
if ii == "1":
    os.system("shutdown -r -f -t 0")
if ii == "2":
    ctypes.windll.PowrProf.SetSuspendState(0,1,0)
if ii == "3":
    ctypes.windll.PowrPlrof.SetSuspendState(1,1,0)
else:
    pass
