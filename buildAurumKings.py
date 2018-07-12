## Must be run as Admin on Windows 10

import os;
from datetime import datetime;
from subprocess import call;

newPath = r'C:/Builds/AurumKings/Windows/';
newPath += datetime.now().strftime("%m-%d-%Y %H.%M %p");

print (newPath);

if not os.path.exists(newPath):
    os.makedirs(newPath)

# Run the Aurum Kings build to this folder
call(["C:/Program Files/Unity_2018.1.1f1/Editor/Unity.exe",
    "-batchmode" ,
    "-quit",
    "-logFile",
    newPath + "/log.txt",
    "-nographics",
    "-projectPath",
    "C:\Program Files (x86)\Jenkins\workspace\AurumKingsBuild\AurumKings",
    "-buildWindows64Player",
    newPath + "/AurumKings.exe"]);
