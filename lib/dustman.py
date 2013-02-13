import subprocess

class Dustman():
	def WipeFileList(self, lst):
		for item in lst:
			self.WipeFile(str(item[0]))

	def WipeFile(self, fil):
		subprocess.call("srm -f -l -v " + fil, shell = True)