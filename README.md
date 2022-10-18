# fsbackup - general
This is a python written backup tool for blizzards world of warcraft.

Storyline:
I got mad two or three times, when an addon crashed and i had no backup of it. So i had to sit there and reconfigure everything.
So i decided to create this tool. It is not perfect and if you find anything we can improve or ad, just let me know.

I have written a pdf-file as description for installation (only in german).

I know, that this tool is far away from perfect. I am no professional software engineer, so if anyone wants to help me improving my cofing style, just let me know! :)

# Main Features

  - wow-directory (chose the source directory)
  - backup-target-directory (chose the target directory)
  - active (chose of the tool is active or not)
  - backupprefix (string infront of each backupfile)
  - game (chose if you want to backup retail or classic)
  - backupmode (chose if the tool should remove "files older then X days" or "remove files if the backupfile-count exceeds amount X")

## Backup Files

The following files will be included into the backup:

  - whole game path of the chosen game version
  This will look like this later:
  ![image](https://user-images.githubusercontent.com/116079190/196418837-fd8504a1-918d-49b7-a901-446e9fba7157.png)


# Usage
I have chosen to setup a planned task in Windows, which starts the tool everytime i startup my windows.
The whole configuration is done within  the config.ini file. You just need to check the set parameters, manipulate them if you want and execute the .exe file.

# Attention

Take care, i only used this tool with Windows 10. It may be possible, that there are issues with the paths and escaping i do within the code. I may change this in further versions.
