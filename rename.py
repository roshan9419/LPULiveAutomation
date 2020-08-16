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
		if os.path.exists(gName+"\\"+file):
			os.remove(file)
			continue
		if(f_ext != ''):
			try:
				shutil.move(file, gName)
			except Exception as e:
				raise e

