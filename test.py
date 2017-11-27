#test for main script

import time
from netcat.sender import Netcat
import sys

target = str(sys.argv[1])

x = Netcat()

var = "./chuck playwav.ck"
#send cmd
x.netcat(target=target, port=9999, buf=var)
#sent it infinitely?? or interpretted it infinitely??
