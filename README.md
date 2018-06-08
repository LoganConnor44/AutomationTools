# Automation Tools

## Objective

* Minimize Sifting Through Directories
* Automate Simple, Repetative Tasks
* Create Simple And Memorable Commands

## Setup

* Environment Variable
	* Purpose: Call this script without having to type out its full path
	* Variable Name: AutomationTools
	* Value: python /c/path/to/where/you/place/this/file.py
	* NOTE: Milage may vary depending on your preferred shell
		* PowerShell: iex "$Env:AutomationTools commands-here"
		* Bash: $AutomationTools commands-here
* Python
	* Installed on your machine
* Vim
	* The editing file script calls Vim, but this does not work in PowerShell and I have not taken the time to find a workaround
	* This could be fixed by opening a different text editor