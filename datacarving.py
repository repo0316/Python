# Name: Jason O'Neal
# Class: Forensics
# Program: datacarving.py
# Description: 
#    This script can be used to discover digital forensic evidence by conducting an OS walk.
#          
#!/usr/bin/env/Python

import hashlib

class carver():
    def carve_jpg(self):
    
        inputfile = 'carveit'
        marker = chr(0xFF)+chr(0xD8)+chr(0xFF)+chr(0xe0)
        
        # Input data
        imagedumpstr = file(inputfile, "rb").read()
        
        imagedumplist = imagedumpstr.split(marker)
        
        count=0
        for photo in imagedumplist:
            name = hashlib.sha256(photo).hexdigest()[0:16]+".jpg"
            file(name, "wb").write(marker+photo)
            count=count+1
            print count
        print 'JPG Complete'
        
    def carve_pdf(self):
    
        inputfile = 'carveit'     #PDF header 25 50 44 46
        marker = chr(0x25)+chr(0x50)+chr(0x44)+chr(0x46)
        
        # Input data
        imagedump = file(inputfile, "rb").read()
        imagedumpm = imagedump.split(marker)
        count=0
        for pdf in imagedumpm:
            name = hashlib.sha256(pdf).hexdigest()[0:16]+".pdf"
            file(name, "wb").write(marker+pdf)
            count=count+1
            print count
        print 'PDF Complete'
def carve_png(self):

        inputfile = 'carveit'     #PNG header 89 50 4E 47
        marker = chr(0x89)+chr(0x50)+chr(0x4E)+chr(0x47)
        
        # Input data
        imagedump = file(inputfile, "rb").read()
        imagedumpm = imagedump.split(marker)
        count=0
        for png in imagedumpm:
            name = hashlib.sha256(png).hexdigest()[0:16]+".png"
            file(name, "wb").write(marker+png)
            count=count+1
            print count
        print 'PNG Complete'
       
x=1

while x==1:
    x=1
    s=carver()    
    pdf = s.carve_pdf()
    jpg = s.carve_jpg()
    png = s.carve_png()
   
    x=0
else:  
    print "Forensic Analysis Complete"




if __name__ == '__main__':
    carver() 
