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

folderls = cmdline("adb shell ls /sdcard")

applist = str(folderls).split("\\n")
applist[0]=applist[0][applist[0].find("'")+1:]
applist.pop(-1)


for i in applist:
    if i.find(".")!=-1:
        applist.remove(i)

total=len(applist)

def printlist():
    print("Available folder in Internal Storage")
    print()

    y=1
    for i in applist:
        print(str(y)+" : "+i)
        y=y+1

print("\n\nCopy type :- \n")
print("For all copy all folder press 1, custom selection press 2 :- ")

temp = int(input("Enter your choice :- "))

sel = []

if temp==1:
    for i in range(total):
        sel.append(i)
elif temp==2:
    print("Enter the folder number which ever you want to copy (e.g. :- 1,5,9,..)\n") 

    printlist()
    
    while True:
        temp1 = int(input("Enter number of folder (-1 to stop) :- "))
        if temp1 <= -1:
            break
        else:
            if (temp1-1) in sel:
                continue
            else:
                sel.append(temp1-1)
    
try:
    path =  os.getcwd() + "/Copied"
    os.mkdir(path)
except:
    pass

os.chdir(path)
print(os.getcwd())

original = path
sel.sort()

for i in sel:
    cmdline("adb pull /sdcard/"+applist[i])


