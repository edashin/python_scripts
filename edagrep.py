#!/usr/bin/env python
# coding: UTF-8

import sys
import binascii
import re

pt =re.compile(r'TIME: [A-Z][a-z][a-z]')
co = []
cc = open(sys.argv[1],'rb').read()

for a in pt.finditer(cc):
	ti = a.start() + 30
	ch = a.start() - 160
	timeinfo = cc[a.start():ti]
	comminfo = cc[ch:a.start()]
	co.append(comminfo)

	for line in co:
		baito = binascii.hexlify(line)
		if "2020202020202020" in baito:
			baito = baito.replace("2020202020202020","20")
		if "0d0a" in baito:
			baito = baito.replace("0d0a","20")
		if "820d" in baito:
			baito = baito.replace("820d","2e2e")
		emd = binascii.a2b_hex(baito)
		pagefile = timeinfo.strip() +";"+ emd.strip()
print pagefile