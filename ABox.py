#######################################################################################
# Author: Abhishek Singh Bisht								
# Description: ABox is a Black Box which can be used to store sensitive information,
#	      such as passwords, bank details, important phone numbers etc.
# Design: I designed this program to keep my passwords safe, at my own terms, using my	
#	  	  own Encryption algorithm. This is purely for personal use, however, you may
#	  	  use it for your own purpose, if you like it :)				
# Contact me at: abhisinghbisht04@gmail.com						
#######################################################################################

from Kryptos import *
dataDict = {}

def authenticateUser():
	c = 3
	while(c!=0):
		key = input('Enter the Passkey :')
		if (key == pk):
			#print "Passkey accepted! You may proceed..."
			return key
		else:
			c-=1
			print 'Incorrect Passkey, you have '+str(c)+' more attempts.'
	return -1

def addNew(webName):
	# to add new information
	auth = authenticateUser()
	if (auth):
		print 'User has been authenticated.\n\nEnter details for '+webName
		usr = raw_input('Enter UserID: ')
		pwd = raw_input('Enter Password: ')
		eusr = encrypt(auth,usr)
		epwd = encrypt(auth,pwd)
		tup = (eusr,epwd)
		dataDict[webName] = tup
	else:
		#Blocking, notification services to be added in future
		print 'Nice try kid! You have been blocked, and the owner has been notified.'

def retrieve(webName):
	auth = authenticateUser()	
	#to retrieve existing information
	if(auth):
		print 'User has been authenticated.\n\nRetrieving details for '+webName
		tup = dataDict.get(webName)
		if (tup==None):
			print 'No details found for '+webName+'. Please try again later.'
			return
		usr = decrypt(auth,tup[0])
		pwd = decrypt(auth, tup[1])
		print 'UserID: '+usr+'\nPassword: '+pwd
	else:
		print 'Authentication Failed.'
		exit()
	return

def updateData(webName):
	auth = authenticateUser()
	#to update existing information
	if(auth):
		print 'User has been authenticated.\n\n'
		tup = dataDict.get(webName)
		if (tup==None):
			print 'No details found for '+webName+'. Please try again later.'
			return
		usr = decrypt(auth,tup[0])
		pwd = decrypt(auth, tup[1])
		print 'UserID: '+usr
		verify = raw_input('Enter existing password: ')
		if(verify == pwd):
			new = raw_input('Enter new password: ')
			new = encrypt(auth, new)
			tup = (tup[0], new)
			dataDict[webName] = tup
			print('Updation successful!')
	else:
		print 'Authentication Failed.'
		exit()
	return

def testing():
	ans = encrypt(1234,"hello world")
	print(ans)
	print(decrypt(1234, ans))

def main():
	print '\n\n****Welcome to ABox****'
	choice = 0
	while(choice!=4):
		print'\n\n'
		choice = int(input('1. Add\n2. Retrieve\n3. Update\n4. Exit\n\nEnter choice: '))
		if choice==1:	
			web = raw_input('\nEnter website: ')
			addNew(web)

		elif choice==2:
			web = raw_input('\nEnter website: ')
			retrieve(web)

		elif choice==3:
			web = raw_input('\nEnter website: ')
			updateData(web)

		elif choice==4:
			exit()
		else:
			print("Invalid choice, please try again!\n")

if __name__ == '__main__':
	main()
