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
    cmdline("adb devices")

applist = glob.glob("*/")

print("Total " + str(len(applist)) + " Folder(s) found in Apk folder\n\n")

y=1
for i in applist:
	print(str(y) + " : " + i)
	cmdline("adb push "+i+" /sdcard/")
	y=y+1

