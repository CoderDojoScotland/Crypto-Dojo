
###################################################
#Does user want to encrypt or decrypt?
################################################### 
def askUserVig():
	invalidMode= True
	while(invalidMode):
		print 'do you want to encrypt (type encrypt and press enter) or decrypt (type decrypt and enter)?'
		mode=raw_input()
		if(mode == "encrypt" or mode == "decrypt"):
			invalidMode= False
		else:
			print "sorry, invalid input - try again!"
	return mode


###################################################
#Get a keyword for Vigenere cipher
#returns keyword if valid, false otherwise
################################################### 
def getKeyword():
  invalidKeyword = True
  cipherKeyword = ''
  while(invalidKeyword):
                  print "please enter the keyword you want to use (type in a word and press enter)"
                  cipherKeyword= raw_input()
                  #added call to method which checks
                  #if the number entered is a valid keyword, if it is
                  #set invalidKeyword to be false
                  if(isValidKeyword(cipherKeyword)):  
                    invalidKeyword = False
                  #otherwise print invalid key and start loop again    
                  else:
                  	print("sorry, invalid keyword - try again! (Keyword must only contain letters a-z)")
  return cipherKeyword
 
 ###################################################
#Check if a value is a word made up of letters a-z
#returns true if it is a valid keyword, false otherwise 
###################################################
def isValidKeyword(val):
        isValid = True
        lenKeyword = len(val)
        #check if word is made of letters a - z
        #if it is, return true, else return false
        for i in range(lenKeyword):
        	if  (ord(val[i]) < (ord('a'))) or ( ord('z') < ord(val[i])):
        		return False
        return isValid
 
##############################################
# encrypt or decrypt using vigenere cipher
###############################################
def vigenere(message, keyword, direction):
	keywordLength = len(keyword)
	msgLength = len(message)
	result = "" 
	if direction == 'encrypt':
		for i in range(0,msgLength):
			nextLetter = encrypt((message[i]), ord(keyword[(i%keywordLength)])-97)
 			result += nextLetter
	elif direction == "decrypt":
		for i in range(0,msgLength ):
			nextLetter = decrypt(message[i], ord(keyword[i%keywordLength]) - 97)
			result += nextLetter
	print result

##############################################
# decrypt message - as used in Caesar Cipher
############################################
def decrypt(msg, shiftValue):
        result = ""
        for letter in msg:
                if(letter == ' '):
                        result+= letter
                else:
                        num = ord(letter)
                        num -= shiftValue
                        if(num > ord('z')):
                           num -=ALPHABET_SIZE
                        if(num < ord('a')):
                           num +=ALPHABET_SIZE
                        decryptedLetter = chr(num)
                        result+= decryptedLetter
        return result

##############################################
# decrypt message - as used in Caesar Cipher
############################################
def encrypt(msg, shiftValue):
        result = ""
        for letter in msg:
                if(letter == ' '):
                        result+= letter
                else:
                        num = ord(letter)
                        num += shiftValue
                        if(num > ord('z')):
                           num -= ALPHABET_SIZE
                        if(num < ord('a')):
                           num += ALPHABET_SIZE     
                        encryptedLetter = chr(num)
                        result+=encryptedLetter
        return result

############################################
# main program
############################################
def main():
	print "Welcome to the E.V.I.L. Vigenere cipher program."
	#ask user if they want to encrypt or decrypt
	direction = askUserVig()
	print "first type in the message you want to " + direction + " in lower case letters > "
	#get message
	message=raw_input()
	#get keyword
	keyword = getKeyword()
	#apply cipher
	vigenere(message, keyword, direction)

	

ALPHABET_SIZE=26
main()
