# fsbackup
This is a python written backup tool for blizzards world of warcraft.

Storyline:
I got mad two or three times, when an addon crashed and i had no backup of it. So i had to sit there and reconfigure everything.
So i decided to create this tool. It is not perfect and if you find anything we can improve or ad, just let me know.

I have written a pdf-file as description for installation (only in german).

# Main Features

  - wow-directory (chose the source directory)
  - backup-target-directory (chose the target directory)
  - active (chose of the tool is active or not)
  - backupprefix (string infront of each backupfile)
  - game (chose if you want to backup retail or classic)
  - backupmode (chose if the tool should remove "files older then X days" or "remove files if the backupfile-count exceeds amount X")

# Usage
I have chosen to setup a planned task in Windows, which starts the tool everytime i startup my windows.

# Attention

Take care, i only used this tool with Windows 10. It may be possible, that there are issues with the paths and escaping i do within the code. I may change this in further versions.
