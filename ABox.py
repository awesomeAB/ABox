##########################################################################################
##Author: Abhishek Singh Bisht								##
##Description: ABox is a Black Box which can be used to store sensitive information,    ##
##	       such as passwords, bank details, imp phone numbers etc.			##
##Design: I designed this program to keep my passwords safe, at my own terms, using my  ##	
##	  own Encryption algorithm. This is purely for personal use, however, you may   ##
##	  use it for your own purpose, if you like it :)				##
##Contact me at: abhisinghbisht04@gmail.com						##
##########################################################################################

from Kryptos import *

def authenticateUser():
	c = 3
	while(c!=0):
		key = raw_input('Enter the Passkey :')
		if (key == '1997'):
			print "Passkey accepted! You may proceed..."
			return 1
		else:
			c-=1
			print 'Incorrect Passkey, you have '+str(c)+' more attempts.'
	return -1

def addNew(webName):
	print('Adding new website to safe!')
	auth = authenticateUser()
	if (auth == 1):
		print 'User has been authenticated\n\n'
		
	else:
		#Blocking, notification services to be added in future
		print 'Nice try kid! You have been blocked, and the owner has been notified.'

def retrieve(webName):
	auth = authenticateUser()	
	#to retrieve existing information
	return

def updateData(webName):
	auth = authenticateUser()
	#to update existing information
	return

def testing():
	ans = encrypt(1234,"hello world")
	print(ans)
	print(decrypt(1234, ans))

def main():
	print '\n\n****Welcome to ABox****\n\n'
	choice = 0
	while(choice!=4):
		choice = int(input('1. Add\n2. Retrieve\n3. Update\n4. Exit\nEnter choice: '))
		if choice==1:	
			web = raw_input('\nEnter website: ')
			addNew(web)

		elif choice==2:
			web = raw_input('\nEnter website: ')
			retrieve(web)
			testing()

		elif choice==2:
			web = raw_input('\nEnter website: ')
			updateData(web)

		elif choice==4:
			exit()
		else:
			print("Invalid choice, please try again!\n")

if __name__ == '__main__':
	main()
