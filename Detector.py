import requests
from optparse import OptionParser
import automate_nmap
import os

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
	

	print " Cyb3rlant3rn here to help!!!!!!!!!!!!!!!!!!!!!!! "	
	print "[1] Source code analzing"
	print "[2] XSS finder"
	print "[3] SSTI"
	print "[4] Check for http"
	print "[5] Automate the nmap scan"
	print "[6] Check for heartbleed"
	print "                           "
	choice=raw_input("choice?")	
	print ""
	if choice == '1':
		filep=open("urlfile",'r')
		for i in filep.readlines():
			i=i.strip('\n')
			sendingreq(i)
	elif choice=='4':
		httpdetection()
		automate_nmap.display()
	elif choice=='2':
	    nmap_scan()
	elif choice=='3':
	     heart_bleed()
	print "Please enter either 1,2,3,4,5 or 6"
		
		
main()
