import requests




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
	
	
	

		 
def  xssdetection():
	f=0
	obj1=open('payload.txt','r')
	obj2=open('url.txt','r')
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
	print " Cyb3rlant3rn here to help!!!!!!!!!!!!!!!!!!!!!!! "	
	print "  _________	
	print "  \/    \/                         "
	print "  /\    /\                        "
	print "    \  /                           "
	print "     \/                           "
	
	print "[1] Source code analzing"
	print "[2] XSS finder"
	choice=raw_input("choice?")	
	if choice == '1':
		filep=open("url.txt",'r')
		for i in filep.readlines():
			i=i.strip('\n')
			sendingreq(i)
	elif choice=='2': 
		xssdetection()
	else:
		print "Please enter either 1 or 2"
		
main()

