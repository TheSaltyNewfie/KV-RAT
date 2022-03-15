import os
import sys

def retreiveLocalDirectory(directoryPath):
    return os.listdir(directoryPath)

def changeActiveDirectory(directoryPath):
    os.chdir(directoryPath)

def createFile(name, contents, writetype):
    with open(name, writetype) as file:
        file.write(contents)
        
