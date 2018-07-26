## Must be run as Admin on Windows 10

import os;
from datetime import datetime;
from subprocess import call;

currentTime = datetime.now().strftime("%m-%d-%Y %H.%M %p");
buildPath = r'C:/Builds/AurumKings/' + currentTime;

windowsPath = buildPath + '/Windows/';

if not os.path.exists(windowsPath):
    os.makedirs(windowsPath)

############################ 64-Bit Windows ######################
call(["C:/Program Files/Unity_2018.1.1f1/Editor/Unity.exe",
    "-batchmode" ,
    "-quit",
    "-logFile",
    windowsPath + "/log.txt",
    "-nographics",
    "-projectPath",
    "C:\Program Files (x86)\Jenkins\workspace\AurumKingsBuild\AurumKings",
    "-buildWindows64Player",
    windowsPath + "/AurumKings.exe"]);
