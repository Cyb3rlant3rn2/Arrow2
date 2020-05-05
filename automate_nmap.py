#!/usr/bin/python2
import os
# please don't use python 2, it is deprecated!
# use python 3 instead

def scan():
    print "Starting the scan"
    print "=================="
    os.system("chmod +x scan.sh")
    os.system("./scan.sh")
    print "[+]Scan results saved in scan_result.txt"
    
def heartbleed():
    print "Starting the heartbleed test"
    print "============================="
    os.system("chmod +x heartbleed.sh")
    os.system("./heartbleed.sh")
    
def display():
    os.system("chmod +x display.sh")
    os.system("./display.sh")
    
    
   
