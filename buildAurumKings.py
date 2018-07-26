## Must be run as Admin on Windows 10

import os;
from datetime import datetime;
from subprocess import call;

currentTime = datetime.now().strftime("%m-%d-%Y %H.%M %p");
buildPath = r'C:/Builds/AurumKings/' + currentTime;

############################ 64-Bit Windows ######################
windowsPath = buildPath + '/Windows/';

if not os.path.exists(windowsPath):
    os.makedirs(windowsPath)

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


############################ 64-Bit LINUX ######################
linux64Path = buildPath + '/Linux_x64/';

if not os.path.exists(linux64Path):
    os.makedirs(linux64Path)

call(["C:/Program Files/Unity_2018.1.1f1/Editor/Unity.exe",
    "-batchmode" ,
    "-quit",
    "-logFile",
    linux64Path + "/log.txt",
    "-nographics",
    "-projectPath",
    "C:\Program Files (x86)\Jenkins\workspace\AurumKingsBuild\AurumKings",
    "-buildLinux64Player ",
    linux64Path + "/AurumKings.x86_64"]);



############################ 32-Bit LINUX ######################
linux32Path = buildPath + '/Linux_x32/';

if not os.path.exists(linux32Path):
    os.makedirs(linux32Path)

call(["C:/Program Files/Unity_2018.1.1f1/Editor/Unity.exe",
    "-batchmode" ,
    "-quit",
    "-logFile",
    linux32Path + "/log.txt",
    "-nographics",
    "-projectPath",
    "C:\Program Files (x86)\Jenkins\workspace\AurumKingsBuild\AurumKings",
    "-buildLinux64Player ",
    linux32Path + "/AurumKings.x86"]);
