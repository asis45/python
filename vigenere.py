# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:38:07 2020

@author: Hp
"""

#we need the alphabet because we convert letters into numerical values to be able to use
#mathematical operations (note we encrypt the spaces as well)
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#the Vigenere algorithm
def vigenere_encrypt(plain_text, key):

	#this is the text we want to encrypt
	plain_text = plain_text.upper()
	# we make the algorithm case insensitive
	key = key.upper()
	
	cipher_text = ''
	#it represents the index as far as the key is concerned
	key_index = 0
	
	#we have to consider all the characters in the plain_text
	for character in plain_text:
		#number of shifts = index of the character in the alphabet + index of the character in the key
		index = (ALPHABET.find(character)+(ALPHABET.find(key[key_index])))%len(ALPHABET)
		#keep appending the encrypted character to the cipher_text
		cipher_text = cipher_text + ALPHABET[index]
		
		#increment the key index because we consider the next letter
		key_index = key_index + 1

		#if we've considered the last letter of the key we start again
		if key_index == len(key):
			key_index = 0
			
	return cipher_text
	
#decryption is the same except now we use the following formula:
#number of shifts = index of the character in the alphabet - index of the character in the key
def vigenere_decrypt(cipher_text, key):

	cipher_text = cipher_text.upper()
	key = key.upper()
	
	plain_text = ''
	key_index = 0
	
	for character in cipher_text:
        
		index = (ALPHABET.find(character)-(ALPHABET.find(key[key_index])))%len(ALPHABET)
		plain_text = plain_text + ALPHABET[index]
		
		key_index = key_index + 1
		
		if key_index == len(key):
			key_index = 0
			
	return plain_text
	
if __name__ == "__main__":
	
	plain_text = 'CRYPTOGRAPHY IS QUITE IMPORTANT IN CRYPTOCURRENCIES'
	encrypted = vigenere_encrypt(plain_text,'table')
	print('Encrypted message: %s' % encrypted)
	decrypted = vigenere_decrypt(encrypted,'table')
	print('Decrypted mesage: %s' % decrypted)