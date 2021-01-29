import os, sys
from datetime import datetime
import os.path
from time import sleep  
import filecmp, shutil






home_folder = r"c:\USBTheft"



now = datetime.now()
dt_string = now.strftime("%m-%d-%y %H-%M-%S")

makefolder = home_folder+"\\"+dt_string

while True :

    os.system('if exist c:\Temp\log.txt del c:\Temp\log.txt')
    os.system('if exist c:\Temp\driver.txt del c:\Temp\driver.txt ')
    os.system('if exist c:\Temp\check.txt del c:\Temp\check.txt')
    os.system("wmic logicaldisk get caption, drivetype >C:\Temp\driver.txt")

    if not os.path.exists(home_folder) :
        os.mkdir(home_folder) 

    def file_drive():

        file_drive = open(r"C:\Temp\driver.txt", "r")

        for i in file_drive :
            if "2" in i :

                indixing = i.find("2")
                degital = int(indixing)
                drive = i[:degital]
                lecteur = drive[1]
                path_dir = "dir /W "+lecteur+":"+">C:\Temp\log.txt"
                os.system(path_dir)
                
                

    file_drive()
            

    def path_directory():    

        tmp_file = r"C:\Temp\log.txt"

        for dirpath, dirnames, filenames in os.walk(home_folder):


            if "log.txt" in filenames :

                
                
                
                st_dirpath = str(dirpath)+"\log.txt"
                print(st_dirpath)

                
                comp = filecmp.cmp(st_dirpath, tmp_file)
                string_comp = str(comp)
                print(string_comp)
                
                f = open(r"C:\Temp\check.txt", "a")
                f.write(string_comp+"\n")
                

                
    path_directory()

    def check_file():

        
        cheker = open(r"C:\Temp\check.txt", "r")
        for line in cheker :
            if "True" in line :
                print("True here")

        
    check_file()





        


                
            

                        

                      
                        

        
    




