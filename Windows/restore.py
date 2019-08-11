from subprocess import PIPE, Popen
import os, sys
import glob

os.chdir("./Copied")

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

for i in range(3):
    cmdline("adb connect 192.168.1.2:5555")
    

applist = glob.glob("*/")

print("Total " + str(len(applist)) + " Folder(s) found in Copied folder folder\n\n")

y=1
for i in applist:
	print(str(y) + " : " + i)
	cmdline('adb push -p "F:\MyPyScripts\Android\Folders Copy\Windows\Copied" /sdcard/')
	print('adb push -p "F:\MyPyScripts\Android\Folders Copy\Windows\Copied" /sdcard/')
	y=y+1

