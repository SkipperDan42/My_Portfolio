global alpha,bet
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
bet = 'abcdefghijklmnopqrstuvwxyz'

## Function that allows you to enter plain text and a key and
#  encrypts it using a shift cipher.
#  returns the encrypted string.
def encrypt(text,key):
	result = ''

	# for every letter in the plaintext, check if it is upper or lower case
	# and shift it by the value of the key entered. If the place value is
	# more than the number of letters in the alphabet, make it wrap to the start
	
	for letter in text:

		if letter.isupper():
			num = alpha.find(letter)
			num += key

			if num > 25:	
				num -= len(alpha)
			result += alpha[num]

		elif letter.islower():
			num = bet.find(letter)
			num += key

			if num > 25:	
				num -= len(bet)
			result += bet[num]


		# if it is neither an upper or lower case letter, just return the letter itself
		else: 
			result += letter

	return result


## Function that decrypts a given ciphertext with a given key
#  returns the decrypted string
def decrypt(text,key):
	result = ''
	
	for letter in text:

		if letter.isupper():
			num = alpha.find(letter)
			num -= key

			if num < 0:	
				num += len(alpha)
			result += alpha[num]

		elif letter.islower():
			num = bet.find(letter)
			num -= key

			if num < 0:	
				num += len(bet)
			result += bet[num]
		
		else: 
			result += letter

	return result

## Function that outputs all possible shifts of the ciphertext given, (brute-force)
def hack(text):
	for key in range(len(alpha)):
		result = ''

		for letter in text:
			if letter in alpha:
			    num = alpha.find(letter)
			    num -= key
			    if num < 0:
			        num += len(alpha)
			        result += alpha[num]
				
			elif letter in bet:	
				num = bet.find(letter)
				num -= key
				if num < 0:	
					num += len(bet)
				result += bet[num]

			else:
				result += letter
                
		print('Hacking key #%s: %s' % (key, result))

## The main function of the program	
def main():
	print('Welcome to the Caesar Cipher!\n')
	program = input('What would you like to do? \n1. Encrypt \n2. Decrypt \n3. Hack \n>>')
	
	if program == '1':
		text = input('Enter the text to encrypt: ')
		key = int(input('Enter the encryption key: '))
		print('\nPlain Text: ' + text + ' Encryption key: ' + str(key) + ' Encrypted Text: ' + encrypt(text,key))
	
	elif program == '2':
		text = input('Enter the encrypted text to decrypt: ')
		key = int(input('Enter the encryption key: '))
		print('\nEncrypted Text: ' + text + ' Encryption key: ' + str(key) + ' Plain Text: ' + decrypt(text,key))
		
	elif program == '3':
		text = input('Enter the encrypted text to crack: ')
		print(' \n' )
		hack(text)
	
	else:
		print('MUST ENTER A VALID OPTION BETWEEN 1 AND 3')
    
	main()


main() # This is the call to start the program.
