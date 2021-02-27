import os, sys
from datetime import datetime
import os.path
from time import sleep  
import filecmp
from shutil import copy2


#path of file used
home_folder = r"c:\DTheft"
tmp_file = r"C:\Temp\log.txt"
checker = r"C:\Temp\check.txt"
driver = r"C:\Temp\driver.txt"


# random folder
now = datetime.now()
dt_string = now.strftime("%m-%d-%y %H-%M-%S")
makefolder = home_folder+"\\"+dt_string+"\\"



#creat infinity loop to keep program running over

while True :

    # check directory 

    if not os.path.exists(home_folder) :
        os.mkdir(home_folder) 


    # earasing file 
    def reborn():
        """ function for delete file if exist on machine"""

        if os.path.exists(driver) :
            os.remove(driver)
        if os.path.exists(tmp_file) :
            os.remove(tmp_file)
        if os.path.exists(checker) :
            os.remove(checker)
    reborn()

    # Creat rapport drivers
    def get_driver_info() :
        """ creat a file 'information about your driver machine' to check if USB contected"""

        string_drive = "wmic logicaldisk get caption, drivetype >"
        full_path = string_drive+driver
        os.system(full_path)
    get_driver_info()


    # Read rapport drivers and check USB Drive
    def file_drive():
        """ function read Driver info file and check if USB connected, if True creat a file with USB information"""

        file_drive = open(r"C:\Temp\driver.txt", "r")

        for i in file_drive :
            if "2" in i :

                
                indixing = i.find("2")
                degital = int(indixing)
                drive = i[:degital]
                lecteur = drive[1]
                # creat a log file content all information about USB          
                path_dir = "dir /W "+lecteur+": >"+tmp_file
                full_path_dir = str(path_dir)
                cmd = "cmd /C" +full_path_dir
                os.system(cmd)

            
    file_drive()


    # Creat Rapport comparision
    def path_directory(): 
        """ function search in Dthief directory the log file and comapre content with log file of USB connected  to create a result comparition file"""

        if os.path.exists(tmp_file) :

            for dirpath, dirnames, filenames in os.walk(home_folder):
                for filenames in [f for f in filenames if f.endswith("log.txt")]:
                    log = os.path.join(dirpath, filenames)
                    

                    comp = filecmp.cmp(log, tmp_file)
                    string_comp = str(comp)
                    f = open(r"C:\Temp\check.txt", "a")
                    f.write(string_comp+"\n")
                    f.close
            else :
                f3 = open(r"C:\Temp\check.txt", "a")
                f3.write("False")
                f3.close
    path_directory()



    def rapport_drivers():

        if os.path.exists(checker) :
            
            with open(r"C:\Temp\check.txt") as f1 :
        
                line = [i.strip() for i in f1.readlines()]
                print(line)
                if "True" in line :
                    return
                elif "True" not in line:
                    os.mkdir(makefolder)
                    copy2(tmp_file, makefolder)

        elif not os.path.exists(checker):
            pass 

        

                    



                    
    
        


    rapport_drivers()

