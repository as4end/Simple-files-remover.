import os, sys, time
from glob import glob 
from shutil import rmtree
try:
	from cprint import cprint
except:
	print("this script will be ugly cuz you don't have the cprint&pprint libraries xD")
	def bprint(txt, *args, speed=1/99, newline=True):
		print(txt)
	cprint = bprint


cprint("Enter (t) to select 'Tree mode' or continue on the current directory: ", "fow")
ans = input()
treeMode = True if ans == "t" else False
startpath, fullpaths =os.getcwd(), []
cprint("Enter extention you want to remove: ")
ex = input()
if len(ex) < 2:
	cprint("invalid extention senpai!")
	time.sleep(5)
	sys.exit()
for root, dirs, files in os.walk(startpath):
	for f in files:
		try:
			path = str(os.path.join(root, f))
			ext = str(os.path.join(root, f))[::-1].split(".")[0][::-1]
			if any([len(ext)>4, ext != ex]):continue
		except:continue
		fullpaths.append(path)
		cprint(path, "s", speed=0.0000000000000000000000000000000009, newline=True, warningOn=False)
	if not treeMode:break

if len(fullpaths) ==0:
	cprint("couldn't find this extention!")
	time.sleep(3)
	sys.exit()

#################################STATS CONDITIONS###########################################################
cprint("i found all your files, senpai!!, press a key to show stats: ", newline=True)
input()
os.system("cls")
cprint("(STATS)".center(34, "*"), newline=True)
cprint(f"the target extention: ".ljust(30, " ") + f"{ex}".rjust(4, " "), newline=True)
cprint(f"the number of files found: ".ljust(30, " ") + f"{str(len(fullpaths))}".rjust(4, " "), newline=True)
cprint("(press enter to proceed)".center(34, "*"), newline=True)
input()
#############################################################################################################

cprint("press (y) if you want to proceed and remove all: ", newline=True)
ans = input()
if ans == "y":
	for p in fullpaths:
		#path = os.path.join(os.getcwd(), i)
		cprint("removing "+os.path.basename(p), speed=0.01/99, newline=True)
		os.remove(p)



