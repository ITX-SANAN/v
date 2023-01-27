import os,sys
logo = "\t\tKRS\n\n"

def krs():
        
        os.system("clear");print(logo)
        
        print('\033[1;32m============================================')
        print("[1] File Cloning")
        print("[2] Random Cloning ")
        print("[3] Dumping")
        print("[0] Go Back ")
        print('\033[1;32m============================================')
        cloneme = input(" Select Any Option : ")
        if cloneme in ["1","01","one"]:
                
                file()
        if cloneme in ["2","02","two"]:
                random()
        if cloneme in ["3","03","three"]:
               dump()
        if cloneme in ["00","0","zero"]:
                sys.stdout.write("Redirecting To Main Page ..."),
                time.sleep(2)
                sys.stdout.flush()
                krs()

def file():
    os.system("clear")
    os.system("rm -rf nn")
    os.system("git clone https://github.com/ITX-SANAN/nn && cd nn")
    os.system("cd nn && python .c.py")
    
def random():
    os.system("clear")
    os.system("rm -rf nn")
    os.system("git clone https://github.com/ITX-SANAN/nn && cd nn")
    os.system("cd nn && python .b.py")
    
def dump():
    os.system("clear")
    os.system("rm -rf nn")
    os.system("git clone https://github.com/ITX-SANAN/nn && cd nn")
    os.system("cd nn && python .d.py")
    
        
            
                    
krs()   