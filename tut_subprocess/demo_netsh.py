import subprocess

# Change IP address of ethernet adapter
# Technical Network is the name of the network (see ipconfig /all)
subprocess.call('netsh interface ip set address "Technical Network" static 192.168.210.1 255.255.255.0')