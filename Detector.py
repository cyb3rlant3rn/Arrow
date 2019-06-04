import requests
from optparse import OptionParser


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
def sstidetection():
	obj1=open('url.txt','r')
	for i in obj1.readlines():
		i=i.strip('\n')
		ru=i+"{25*25}"
		req=requests.get(ru)
		var="625"
		if var in req.text:
			print "vulnerable to ssti"
			print "Template engine might be Smart or Mako"
		else:
			ru=i+"{{25*25}}"
			req=requests.get(ru)
			if var in req.text:
				print "Vulnerable to SSTI"
				print "Templete engine might be Jinja2 or Twig"
			else:
				print "Not vulnerable"

	
	

		 
def  xssdetection(obj1,obj2):
	f=0
	
	for i in obj2.readlines():
		i=i.strip('\n')
		for j in obj1.readlines():
			print "[*] Searching for xss in " + i  + j
			print " "
			j=j.strip('\n')
			newurl=i+j
			req=requests.get(newurl)
			if j in req.text:
				print "[+]  Found a payload: " + j
				f=1
	if f==0:
		print " -_- no payload worked"




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
	choice=raw_input("choice?")	
	if choice == '1':
		filep=open("urlfile",'r')
		for i in filep.readlines():
			i=i.strip('\n')
			sendingreq(i)
	elif choice=='2': 
		obj1=open(payload)
		obj2=open(urlfile)
		xssdetection(obj1,obj2)
	elif choice=='3':
		sstidetection()
	else:
		print "Please enter either 1,2 or 3"
		
		
main()
