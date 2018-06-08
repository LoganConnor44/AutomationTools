import argparse
import datetime
import os
import shutil
import subprocess

"""
Copies all .dll, .xml, and .pdb to a given directory if they have been changed within the past hour.

@param string repoName:  This is the name of the git repo
@param string directoryPath: This is the source directory that files will be copied from
@return: None 
"""
def copyBinariesTo(repoName, directoryPath) :
	gitRepo = "C:\\Source\\Repos\\" + repoName + "\\Bin\\Module\\"
	sourceFiles = []
	now = datetime.datetime.now()
	timeRange = now - datetime.timedelta(hours = 1)

	for file in os.listdir(gitRepo) :
		fileTime = datetime.datetime.fromtimestamp(os.path.getmtime(gitRepo + file))

		if file.endswith(".dll") and fileTime > timeRange :
			sourceFiles.append(file)
		if file.endswith(".xml") and fileTime > timeRange :
			sourceFiles.append(file)
		if file.endswith(".pdb") and fileTime > timeRange :
			sourceFiles.append(file)

	for file in sourceFiles :	
		shutil.copyfile(gitRepo + file, directoryPath + file)
		print("---Copy Completed: {}---" . format(file))

	print("\n")
	print("{} Files Copied" . format(len(sourceFiles)))
	print("Source Directory: {}" . format(gitRepo))
	print("Destination Directory: {}" . format(directoryPath))

	return

"""
Starts a given exe

@param programName: A simplified version of the app name
@return: None
"""
def executeProgram(programName) :
	baseDirectory = "C:\\your\\path\\here\\"
	os.system("start " + baseDirectory + programName)
	print("Opening application-name-here From {}" . format(baseDirectory + programName))

	return

"""
Opens a given file in vim to edit

@param fileName: The name of the desire file to edit
@return: None
"""
def editFile(fileName) :
	baseDirectory = "C:\\your\\path\\here\\"
	os.system("vim " + baseDirectory + fileName)

	return

"""
Stops all tasks that have the name prefixed-name-here prefixed on it

@return: None
"""
def killAllExpertTasks() :
	killTask = "taskkill /F /im prefixed-name-here.*"
	os.system(killTask)
	print("Killing All Tasks With prefixed-name-here As A Prefix")

	return

"""
Core logic for the terminal application

@param @argparse string typeOfOperation: User defined base operation for the app
@param @argparse string optionalArgTwo: An optional argument that is used only for copy binaries git repo name
@param @argparse string optionalArgThree: An option argument that is used only for copy binaries source directory 
@return: None
"""
def mainApplication() :
	options = {
		"copy-binaries" : copyBinariesTo,
		"run" : executeProgram,
		"kill-expert" : killAllExpertTasks,
		"edit" : editFile
	}
	variableNameHere = "C:\\your\\path\\here\\"
	variableNameHere2 = "C:\\your\\path\\here\\"
	localServices = "C:\\your\\path\\here\\"
	availablePairs = {
		"app-name-here" : variableNameHere,
		"app-name-here" : variableNameHere2,
		"services" : localServices,
		"app-name-here" : "app-name-here.exe",
		"log" : "log-name-here.xml"
	}

	parser = argparse.ArgumentParser()
	parser.add_argument(
		"typeOfOperation",
		type = str
	)
	parser.add_argument(
		"optionalArgTwo",
		nargs = "?",
		type = str
	)
	parser.add_argument(
		"optionalArgThree",
		nargs = "?",
		type = str
	)
	args = parser.parse_args()

	if args.typeOfOperation not in options.keys() :
		print("{} is not an available operation. Please try again." . format(args.typeOfOperation))
		return
	if args.optionalArgTwo != None :
		if args.optionalArgTwo not in availablePairs :
			print("{} is not an optional argument. Please try again." . format(args.optionalArgTwo))
			return

	if args.optionalArgTwo == None and args.optionalArgThree == None :
		options[args.typeOfOperation]()
	elif args.optionalArgTwo != None and args.optionalArgThree == None :
		options[args.typeOfOperation](
			availablePairs[args.optionalArgTwo]
		)
	else:
		options[args.typeOfOperation](
			args.optionalArgTwo,
			availablePairs[args.optionalArgThree]
		)

	return

if __name__ == "__main__" :
	mainApplication()