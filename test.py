#test for main script

import time
from netcat.sender import Netcat
import sys

target = str(sys.argv[1])

x = Netcat()
var = str(raw_input())
print var

#send cmd
x.netcat(target=target, port=9999, buf=var)
		
