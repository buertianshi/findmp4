import os,winshell

from win32com.client import Dispatch

target = "F:\\steam\\steamapps\\workshop\\content\\431960"
save = "F:\\steam\\steamapps\\workshop\\content\\431960\\allMp4"
dirs = os.walk(target)
for root,dirs,files in os.walk(target):
    for filename in files:
        if ".mp4" in filename:
            targetL = root+"\\"+filename
            path = save+"\\"+filename.split('.')[0]+".lnk"
            work_dir=root

            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = targetL
            shortcut.WorkingDirectory = work_dir
            shortcut.save()