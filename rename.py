import os
import shutil

def renameFiles(gName):
	# os.chdir("Downloads")
	if ":" in gName:
		gName = "Friends"
	if os.path.exists(gName)==False:
		os.mkdir(gName)
	for file in os.listdir():
		f_name, f_ext = os.path.splitext(file)
		if(f_ext != ''):
			shutil.move(file, gName)
			# while True:
			# 	try:
			# 		shutil.move(file, gName)
			# 		break
			# 	except Exception as e:
			# 		sleep(0.5)
			# 		continue



def showFiles():
	os.chdir("Downloads")
	for file in os.listdir():
		f_name, f_ext = os.path.splitext(file)
		print(f_name, f_ext)

