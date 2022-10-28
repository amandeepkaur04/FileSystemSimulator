# Python File System Simulator

## Requirements
1. Python 3.7 installed, (Tested on versions 3.7 and 3.8)

## Description

### Data structure used

Uses Tree data structure to store the directory and file names.
Class Tree has name (name of directory), 
directories (list of directories under current directory, 
where each directory is object of Tree class), 
files (list of file names in the directory), 
and root (parent directory of current directory)

### Commands supported

1. **ls**: list files and directories of current directory. At this point only ls with no arguments is supported.
2. **cd**: change directory. Here operation ".." means one directory back. Usage: cd path. If path is None, it moves to root directory. Also, if path is given, it assumes that absolute correct path should be given, otherwise it generates invalid path error. For example, from directory home/test command "cd .." works, command "cd" works, but command "cd ../.." doesn't work.  
3. **touch**: Although touch command has additional purposes than creating a file, but in this simulator, assumption is that touch command creates an empty file. Usage touch filename. At this point only alphanumeric filename is supported along with character "." for adding file extension. For example test12, TEST.txt, 123.doc are supported. #12, abc% etc are not supported.
4. **mkdir**: Make a new directory. At this point only alphanumeric directory name is supported. For example, test, test123, new, NEW are supported but test.test, test$ etc. are not.
5. **q**: Exit the filesystem.
### Usage

To run the simulator, simply run the program. By default, a root directory named "Home" is created.
