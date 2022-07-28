
comando="frame3dd -h"

#--------------------------------------
from platform import system as  platsys
from os import system
prev=""
if platsys()=="Windows":prev="powershell"
system(prev+" "+comando)
