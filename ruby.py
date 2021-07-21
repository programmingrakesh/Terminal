import os
import subprocess
from typing import ByteString

#os.chdir(r"C:\Users\ADMIN\Desktop\cmd") for windows
os.chdir(r"/mnt/c/Users/ADMIN/Desktop/cmd")
PATH = os.getcwd()


while True:
    x = input(f"{PATH}$ ")
    if "ls" in x:
        sl = os.listdir(PATH)
        print(sl)
    elif "exit" in x:
        break

    elif "cd" in x:
        x = x.split(" ")
        x = x[1]
        if ".." in x:
            #PATH = PATH.split("\\") for windows
            PATH = PATH.split("/") #for linux users
            l = PATH[-1]
            PATH = os.getcwd()
            #PATH = PATH.replace(f"\\{l}", "") sor windows
            PATH = PATH.replace(f"/{l}", "")
            os.chdir(PATH)
        else:
            cmd = f"{PATH}/{x}"
            PATH = cmd
            os.chdir(PATH)
    elif "help" in x:
        print("<ls> to list the directory.")
        print("<cd /DIRECTORY NAME/> to change directory.")
        print("<cd ..> to return to Home directory.")
        print("<cat <FILENAME>> to see the content.")
        print("<bs> to oprn WSL in Windows computer.")
        print("<run <FILENAME.py>> to run the python file.")
        print("<rm <FILENAME>> to Remove a file.")
        print("type <pip <Package name>> to install the package.")
        print("type<exit> to close the program.")        

    elif "cat" in x:
        x = x.split(' ')
        x = x[-1]
        with open(x, 'r') as f:
            b = f.read()
            f.close()
            print(b)

    elif "rm" in x:
        x = x.split(" ")
        x = x[1]
        print(x, "the File Have been Deleted")
        os.remove(x)

    elif "bs" in x:
        os.system("bash")

    elif "run" in x:
        x = x.split(" ")
        x = x[1]
        with open(x, 'r') as f:
            b = f.read()
            f.close()
            exec(b)
 
    elif "pip" in x:
        x = x.split(" ")
        x = x[1]
        os.system(f"pip install {x}")
    
    else:
        print('something Went wrong')
