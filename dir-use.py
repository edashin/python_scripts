#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#check folder size recursively.

import os
import sys

dr = sys.argv[1]
print(dr)

dic1={}
for root,dirs,files in os.walk("c:\\forensictools"):
    for dire in dirs:
        dire = os.path.join(root,dire)
        ss = os.path.getsize(dire)
        dic1[dire] = ss

for a,b in sorted(dic1.items(), key=lambda x: x[1]):
    print(a,b)


