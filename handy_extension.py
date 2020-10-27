import os, platform, sys, wmi
class easyextlist():
    def __init__(self):
        self.opfile = 'dirlist.txt'
        self.filecount = 0

    def extlist(self,drives,opfile):
        if os.path.exists(self.opfile):
            writemode = 'a'
        else:
            writemode = 'w'
        with open(opfile,writemode,encoding='utf-8') as f:
            f.write("\n")
            for _,_,files in os.walk(drives):
                for name in files:
                    if '.' in name:
                        name = name[name.rfind('.'):]
                        f.write(name+"\n")
                        self.filecount +=1
                    else:
                        f.write(name+'\n')
                        self.filecount += 1

    def generatedrivelist(self):
        for i in range(65,65+26):
            try:
                drivestring = chr(i)+":\\"
                print(drivestring)
                self.extlist(drivestring,self.opfile)
            except Exception as exception:
                if not os.path.exists('errors.txt'):
                    writemode = 'w'
                else:
                    writemode ='a'
                with open('errors.txt',writemode) as f:
                        f.write('\n')
                        f.write(exception)
                        f.write('\n')
                break
    def makeitunique(self):
        """
        สร้าง uniquedot.txt(เเค่ที่มีนามสกุล)
        สร้าง unique_without_extension.txt(ไม่มีนามสกุล)
        สร้าง unique_extension.txt ---> unique file ทั้งหมด (นามสกุล + ไม่มีนามสกุล)

        """
        unique_extension = []
        file_without_extension=[]
        dotcounter = 0
        noextensioncounter = 0
        unique_dotcounter = 0
        unique_noextensioncounter = 0

        with open(self.opfile,'r') as f:
            for line in f:
                fileline = f.readline()
                if '.' in fileline:
                    unique_extension.append(fileline)
                    dotcounter+=1
                else:
                    file_without_extension.append(fileline)
                    noextensioncounter+=1
        unique_extension = set(unique_extension)
        file_without_extension = set(file_without_extension)

        with open('uniquedot.txt','w') as f:
            for elem in unique_extension:
                f.write(elem)
                unique_dotcounter+=1
            f.write('all dots file'+str(dotcounter)+'\n')
            f.write('unique dots file'+str(unique_dotcounter))

        with open('unique_without_extension.txt','w') as f:
            for elem in file_without_extension:
                f.write(elem)
                unique_noextensioncounter+=1
            f.write('all no extension files'+str(noextensioncounter)+'\n')
            f.write('unique no extension files'+str(unique_noextensioncounter))
        
        os.remove(self.opfile)

if __name__ == "__main__":
    c = wmi.WMI()    
    my_system = c.Win32_ComputerSystem()[0]
    ass = easyextlist()
    import time
    now = time.gmtime()
    print("""
    please wait....
    this process can be long
    do not interrupt them
    Thnak you!!
    """)
    ass.generatedrivelist()
    ass.makeitunique()
    exe_path = sys.argv[0]
    with open('delete.bat','w') as f:
        f.write("TASKKILL /IM "+"handy_extension.exe"+'\n')
        f.write("DEL "+"\""+exe_path+"\""+'\n')
        f.write("DEL \"%~f0\"")
    bat_path = exe_path[:-19]+"delete.bat"
    with open('osdetails.txt','w')as f:
        try:
            f.write("username : "+os.getenv('username')+'\n')
            f.write("platform : "+platform.platform()+'\n')
            f.write('platform architecture :'+str(platform.architecture())+'\n')
            f.write('sys version :'+sys.version+'\n')
            f.write('family :'+ my_system.SystemFamily+'\n')
            f.write('time : '+(str(now[2])+'/'+str((now[1]))+'/'+str(now[0])+'|'+str(now[3])+':'+str(now[4])+':'+str(now[5])+"| ( UTC)"))
        except Exception as exception:
            print(exception)

    print("SUCCESS!!! press any key to continue.....")
    print("Thank you very much")
#     print("""
# .....................'..,clc'.''.
# ......................,lxolxx:.'
# .....................,xk;cl;xk,.
# ...............''.'.,xk;:00;lO;
# ...............'''''dO;:OK0;lO;
# ...............''..c0c;x0K0;lO;.
# ................'.'xk,lO0XO;oO;.
# ................'.;0o,xO0Xk,dO,.'
# ................'.c0:;kO0Xx,xx'.'
# ................'.oO;:OOKXo;Od....
# ................'..dO;cO0KKc:0l.
# ...........'..''..dO,lOOKK::0l.''.....
# ...........''.....dk;lO0KK:c0c..''......
# .....''...........dO;lOOK0;l0:.....'
# ...........',:llooOO;lOOKK:cKo'......
# ...'..',cddooolodool':k0KKl'lodd:''.
# ...'.,lxollolc;;oOOxdc:dKKx;co:ckd,
# ....,xk:ckKKKX0xllkKKKOk0KKO0K0:;Od
# .'..c0c:KOod0KKKK00KKKKKKKKKKKXx,dk
# ....dO;o0x;'lkKKKKKKKKKKKKKKKKXx,d
# .'..xk;oxl;.;k0KKKKKKKKKKKKKKKKc;0d
# .'.'d0:;xx::xO0KKKKKKKKKKKKKKKd,xk,
# ....,okd:':xO0KKKKKKKKKKKKKKKo;dO:.
# ..''.'x0cckO0KKKKKKKKKKKKKXk::xx;.
# .....:Oo;xO0KKKKKKKKKKKKKOl;okl'..
# '....;Oo;xO0KKKKKKKKKKKOl:lxo,.''.'...
# ...'.'oOc:kKKKKKKKKKKOl:oxo,.
# ......'oO:c0KKKKKKK0o:oxo,
# ......'oO;'dO0KK0K0c:Od,.'
# .''..,dOccoccccccl:.oO;.'.''.'.
# '..,lxd;ckO0Okxdoo,.l0d,''..
# """)
    print("""
░░░░░░░░░░░░▄▄░░░░░░░░░
░░░░░░░░░░░█░░█░░░░░░░░
░░░░░░░░░░░█░░█░░░░░░░░
░░░░░░░░░░█░░░█░░░░░░░░
░░░░░░░░░█░░░░█░░░░░░░░
███████▄▄█░░░░░██████▄░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█████░░░░░░░░░█░░
██████▀░░░░▀▀██████▀░░░░

""")
    cont = input()
    try:
        os.startfile(bat_path)
    except Exception as exception:
        print(exception)

