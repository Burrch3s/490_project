#test for main script

import time
from netcat.sender import Netcat
import sys

target = str(sys.argv[1])
loop = True
x = Netcat()
while loop:
	var = str(raw_input())
	if var == 'quit':
		loop = False

	print var
	#send cmd
	x.netcat(target=target, port=9999, buf=var)
		
