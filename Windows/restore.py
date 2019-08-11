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
    cmdline("adb devices")

cmdline('adb push -p "'+os.getcwd()+'\Copied" /sdcard/')
print('adb push -p "'+os.getcwd()+'\Copied" /sdcard/')
