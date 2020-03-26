# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:16:47 2020

@author: Hp
"""
#caeser cipher algorithm


ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 4

#caesar encryption algorithm
def caesar_encrypt(plain_text):

	cipher_text = ''
	plain_text = plain_text.upper()

	for c in plain_text:
		index = ALPHABET.find(c)
		index = (index+KEY)%len(ALPHABET)
		cipher_text += ALPHABET[index]
		
	return cipher_text
	

#caesar decryption algorithm
def caesar_decrypt(cipher_text):

	plain_text = ''
	
	for c in cipher_text:
		index = ALPHABET.find(c)
		index = (index-KEY)%len(ALPHABET)
		plain_text = plain_text + ALPHABET[index]
		
	return plain_text
	
if __name__ == "__main__":
	
   print("Encryption")
   print("Plain text: This is aashish from Siliguri Institute of Technology")
   encrypted = caesar_encrypt('This is aashish from Siliguri Institute of Technology')
   print("Cipher text: ",encrypted)     
   
   print("")
   print("Decryption")
   print("Cipher text: XLMWDMWDEEWLMWLDJVSQDWMPMKYVMDMRWXMXYXIDSJDXIGLRSPSKB")
   decrypted = caesar_decrypt("XLMWDMWDEEWLMWLDJVSQDWMPMKYVMDMRWXMXYXIDSJDXIGLRSPSKB")
   print("Plain text:",decrypted)
	