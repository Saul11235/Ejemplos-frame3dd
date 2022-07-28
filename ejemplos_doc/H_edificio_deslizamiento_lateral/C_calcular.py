
comando="frame3dd -i data.3dd  -o calculos.out "

#--------------------------------------
from platform import system as  platsys
from os import system
prev=""
if platsys()=="Windows":prev="powershell"
system(prev+" "+comando)
