import random

def encrypt(key, rawData):
	keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
	keyBaseArray = list(keyBase)
	codeKeyArray = keyBaseArray
	charArray = list(rawData)
	for count1,elem in enumerate(charArray):
		key=int(key)
		key+=count1
		random.seed(key)
		random.shuffle(codeKeyArray)
		for count2,elem2 in enumerate(keyBase):
			if elem == elem2:
				charArray[count1]=codeKeyArray[count2]
	encryptedData=''.join(charArray)
	return encryptedData

def decrypt(key, encryptedData):
	keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
	keyBaseArray = list(keyBase)
	codeKeyArray = keyBaseArray
	charArray = list(encryptedData)
	for count1,elem in enumerate(charArray):
		key=int(key)
		key+=count1
		random.seed(key)
		random.shuffle(codeKeyArray)
		for count2,elem2 in enumerate(codeKeyArray):
			if elem == elem2:
				keyBaseArray = list(keyBase)
				charArray[count1]=keyBaseArray[count2]
	rawData=''.join(charArray)
	return rawData

def main():
	print('Test string: hello world!')
	ans = encrypt(1234, 'hello world')
	print'Encrypted String: ',ans
	print'Decrypted String: ',decrypt(1234,ans)

if  __name__ == '__main__':
	main()
