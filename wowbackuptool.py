## INFO ######
# version: 1.5
# Created by: Florian Schuetze, WETHUGER
# Created 20220609
# config-file needs to be in: C:\wowbackuptool
#
#
# Change History:
# 20220609: Creation
# 20220627: Implementing Backupfunction-Cleanup per age or per Count, added Backup of the whole _retail_ or _classic_ folders
# 20220701: Implementing Status Output while Copying Files
# 20220711: Cleaning Code Structure, implementing functions
##############

# Module importieren
import configparser
import os
import datetime
import time
import shutil
import logging
from time import sleep
from xml.etree.ElementTree import tostring
from distutils.dir_util import copy_tree
from shutil import copytree,copy2
import zipfile

# Konfiguration einlesen
config = configparser.ConfigParser()
config.read('C:\wowbackuptool\config.ini')

# Variablen bauen
active = config['conf']['active']
wowdir = (config['conf']['WowDir']).replace('\\','/')
backupprefix = config['conf']['backupprefix']
backupdir = (config['conf']['backupdir']).replace('\\','/')
gameversion = config['conf']['game']
backupfolder = backupprefix + '-' +datetime.datetime.now().strftime("%d-%b-%Y-%H%M%S")
backupfolderfull = backupdir + '/' + backupfolder
addonfolder = wowdir + '/' +'_'+ gameversion +'_'+ '/' + 'Interface' 
wtf = wowdir + '/' +'_'+ gameversion +'_'+ '/' + 'WTF'
cache = wowdir + '/' +'_'+ gameversion +'_'+ '/' + 'cache'
backupcount = config['conf']['backupcount']
backupage = config['conf']['backupage']
backupmode = config['conf']['backupmode']


# Sicherungsordner anlegen und ausgeben
def MakeBackupDirectory():
    print('Creating Destination Folder...')
    os.mkdir(backupfolderfull)
    print('Folder: ' + backupdir + '\\' + backupfolder + ' created!')
# Daten aus Original kopieren
def CopyOriginals():
    print('Copying Files...')
    source = wowdir + '/' +'_'+ gameversion +'_'
    destination = backupfolderfull + '/retail'
    def copy2_verbose(src, dst):
        print('Copying {0}'.format(src))
        copy2(src,dst)
    copytree(source, destination, copy_function=copy2_verbose)
# Zipfile schnueren
def ZipBackup():
    print('Creating Zip-File...')
    zf = zipfile.ZipFile(backupfolderfull+".zip", "w")
    for dirname, subdirs, files in os.walk(backupfolderfull):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
    shutil.rmtree(backupfolderfull)
    print('Zip-File created: '+backupfolderfull+'.zip')
    print('Cleaning...')
    sleep(3)
    print(os.walk(backupdir))
# Alte Backups löschen
def CleanOldFiles():
    # Cleanmode Count
    if backupmode == 'count':
        for filename in sorted(os.listdir(backupdir))[:-int(backupcount)]:
            filename_relPath = os.path.join(backupdir,filename)
            os.remove(filename_relPath)

    # Cleanmode Age
    if backupmode == 'age':
        now = time.time()
        for f in os.listdir(backupdir):
            f = os.path.join(backupdir,f)
            if os.stat(f).st_mtime < now -7 * 86400:
                if os.path.isfile(f):
                    os.remove(f)

    print('Done!')

### Funktionsaufrufe ###
MakeBackupDirectory()
CopyOriginals()
ZipBackup()
CleanOldFiles()