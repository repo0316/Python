 Name: Jason O'Neal
# Class: Forensics
# Program: project1_redo.py
# Description: 
#    This script can be used to discover digital forensic evidence.
#          
#!/usr/bin/env/Python

import subprocess, os, md5
from gnomevfs._gnomevfs import Drive

class discover():
   
    def choose_drive():
        choose_drive = subprocess.call(['sudo' + ' blkid'], shell=True)
            print "Here is the list of available drives:", choose_drive
        drive = raw_input("What device do you want to mount?")
        return drive
        
    def mount_drive(self):
        mounting = subprocess.call(["sudo" + " mount" + " -t" + " ntfs " + drive + " /mnt"], shell=True)
        mnt_dir = subprocess.call(["ls" + " /mnt"], shell=True)
    
    def dd_drive():
        dd_mounting = subprocess.call(["sudo" + " mount" + " -t" + " ntfs " + "/forensic_image" + " /mnt"], shell=True)
        mnt_dir = subprocess.call(["ls" + " /mnt"], shell=True)
        bsc = subprocess.call(['sudo' + " dd" + " if=" + drive + " of=" + "/forensic_image"], shell=True)
        print "Please wait while a bit stream copy of the device is made.  This may take several minutes..."
        
    def md5_check(self):
        checksum = subprocess.call(['sudo' + " md5sum " + drive], shell=True)
            print "Generating a MD5 hash of the original file: Please wait"
        checksum_dd = subprocess.call(['sudo' + " md5sum" + " /forensic_image"], shell=True)
            print "Generating a MD5 hash of the forensic copy file: Please wait"
        if checksum == checksum_dd:
            print "Good copy! Unmounting device..."
            unmount_drive = subprocess.call(["sudo" + " umount " + drive], shell=True)
        else:
            print "Copy error - please re-run script"
            
    def carve(self):
        print "Searching for suspicous files found during visual inspection of the file system"

        path = ["/mnt/Documents and Settings/lab/Desktop/", "/mnt/RECYCLER", "/mnt/Documents and Settings/lab/My Documents/"]
        for index in range(len(path)):
            jpgfiles = []
            bmpfiles = []
            txtfiles = []
            pdffiles = []
            
            for dirpath, subdirs, files in os.walk(path[index]):
                for x in files:
                        if x.endswith(".jpg"):
                                jpgfiles.append(os.path.join(dirpath, x))
                            print jpgfiles
                    
                        elif x.endswith(".bmp"):
                                bmpfiles.append(os.path.join(dirpath, x))
                            print bmpfiles               
        
                        elif x.endswith(".txt"):
                            txtfiles.append(os.path.join(dirpath, x))
                                print txtfiles
                       
                        elif x.endswith(".pdf"):
                                    pdffiles.append(os.path.join(dirpath, x))
                                print pdffiles
                                
                        else:
                
forensic_data = 0
forensic_data = sys.argv[2]
data=original_data

x=1

while x==1:
    x=1
    s=discover()    
    choice = s.choose_drive()
    mount = s.mount_drive(choice)
    dddrive = s.dd_drive()
    md5hash = s.md5_checksum()
    img = /mount/forensic_image
    data_carve = s.carve(img)
    x=0
else:  
    print "Forensic Analysis Complete"


if __name__ == '__main__':
    discover(): 
