########################################################
## This Must be run as Admin if you are on Windows 10 ##
########################################################
import os;
from datetime import datetime;
from subprocess import call;

# Define some constant vars for building
UNITY_INSTALL_LOCATION  = "C:/Program Files/Unity_2018.1.1f1/Editor/Unity.exe";
PROJECT_PATH            = "C:\Program Files (x86)\Jenkins\workspace\AurumKingsBuild\AurumKings";
BUILD_TARGET_WINDOWS_64 = "-buildWindows64Player";
BUILD_TARGET_LINUX_64   = "-buildLinux64Player ";
BUILD_TARGET_OSX        = "-buildOSXPlayer ";
BASE_BUILD_PATH         = r'C:/Builds/AurumKings/' + datetime.now().strftime("%m-%d-%Y %H.%M %p") + "/";
LINUX_64_BUILD_PATH     = BASE_BUILD_PATH + 'Linux_x64/';
WINDOWS_BUILD_PATH      = BASE_BUILD_PATH + 'Windows/';
MAC_BULID_PATH          = BASE_BUILD_PATH + 'OSX/';

## Build the game suing a new subprocess and the defined variables
def buildGame(buildTarget, outputPath, executeableName):

    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    call([
        UNITY_INSTALL_LOCATION,
        "-batchmode" ,
        "-quit",
        "-logFile",
        outputPath + "_BUILD_LOG.txt",
        "-nographics",
        "-projectPath",
        PROJECT_PATH,
        buildTarget,
        outputPath + executeableName
        ]);


#####################################################
# Call the build functions and bulid the game

buildGame(BUILD_TARGET_WINDOWS_64, WINDOWS_BUILD_PATH, "AurumKings.exe");

buildGame(BUILD_TARGET_LINUX_64, LINUX_64_BUILD_PATH, "AurumKings.x86_64");
