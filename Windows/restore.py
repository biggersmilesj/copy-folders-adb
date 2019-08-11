from subprocess import PIPE, Popen
import os, sys
import glob

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

for i in range(3):
    cmdline("adb connect 192.168.1.2:5555")

cmdline('adb push -p "'+os.getcwd()+'\Copied" /sdcard/')
print('adb push -p "'+os.getcwd()+'\Copied" /sdcard/')
