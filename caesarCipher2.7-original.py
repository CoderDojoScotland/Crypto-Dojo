def askUser():
	invalidMode= True
	while(invalidMode):
		print 'do you want to encrypt (type encrypt and press enter), decrypt (type decrypt and enter) or brute force (type force and enter)?'
		mode=raw_input()
		if(mode == "encrypt" or mode == "decrypt" or mode == "force"):
			invalidMode= False
		else:
			print "sorry, invalid input - try again!"
	return mode




def main():
	currentMode = askUser()
	print "you want to " + currentMode + " - awesome, let's get started!"
	print "first type in the message you want to " + currentMode + " > "
	message=raw_input()
	if(currentMode == "encrypt"):
		currentKey = getKey()
		encrypt(message, currentKey)
	elif(currentMode == "decrypt"):
		currentKey = getKey()
		decrypt(message, currentKey)
	elif(currentMode == "force"):
		force(message)

def getKey():
##################################################
#Get encryption key from user
##################################################
  invalidKey = True
  cipherKey = 0
  while(invalidKey):
                  print "please enter the key you want to use (type a number between 1 and 25 and press enter)"
                  cipherKey = raw_input()
                  #added call to method which checks
                  #if the number entered is a valid key, if it is
                  #then cast to an int and set invalidKey to be false
                  if(isValidKey(cipherKey)):
                      cipherKey = int(cipherKey)    
                      invalidKey = False
                  #otherwise print invalid key and start loop again    
                  else:
                                  print("sorry, invalid key - try again!")
  return cipherKey

###################################################
#Check if a value is an integer between 1 and 25
#returns true if it is a valid key, false otherwise 
###################################################
def isValidKey(val):
        #try to cast the value to an int, catch a Value error
        #if it casts to an int without error, then check
        #if it's between 1 an 25
        #if it is, return true, else return false
        try:
                intVal=int(val)
                if((intVal >= 1) and (intVal <= 25)):
                    return True
                else:
                    return False
        #return false if it's not a number        
        except ValueError:
                print 'try entering a number'
                return False
        
def force(msg):
  ##################################################
  #brute force decrypt - i.e. try all possible keys
  ##################################################
  print "attempting to force decrypt of " + msg + " now! - results are:"
  ##################################################
  #outer loop - letters of alphabet
  ##################################################
  for shiftValue in range(1,26):
          print "For key = " + str(shiftValue) + " the decrypted message is: "
          result = ""
          ##################################################
          #inner loop - letters of message
          ##################################################
          for letter in msg:
                if(letter == ' '):
                                result += letter
                else:
                                num = ord(letter)
                                num -= int(shiftValue)
                                if(num > ord('z')):
                                                num -= ALPHABET_SIZE
                                if(num < ord('a')):
                                                num += ALPHABET_SIZE
                                decryptedLetter = chr(num)
                                result += decryptedLetter
          ######################
          # inner loop ends here
          #######################
          #back to outer loop
          print result
          print "" 
          #end of outer loop



def decrypt(msg, shiftValue):
        print "decrypting " + msg + " now! - your decrypted message is:"
        result = ""
        for letter in msg:
                if(letter == ' '):
                        result += letter
                else:
                        num = ord(letter)
                        num -= shiftValue
                        if(num > ord('z')):
                           num -= ALPHABET_SIZE
                        if(num < ord('a')):
                           num += ALPHABET_SIZE
                        decryptedLetter = chr(num)
                        result += decryptedLetter
        print result



def encrypt(msg, shiftValue):
        print "encrypting " + msg + " now! - your encrypted message is:"
        result = ""
        for letter in msg:
                if(letter == ' '):
                        result += letter
                else:
                        num = ord(letter)
                        num += shiftValue
                        if(num > ord('z')):
                           num -= ALPHABET_SIZE
                        if(num < ord('a')):
                           num += ALPHABET_SIZE     
                        encryptedLetter = chr(num)
                        result += encryptedLetter
        print result

#get those who struggle to switch the value hard code, those who do well write a function to ask for shift value		
#shiftValue=6
ALPHABET_SIZE=26
main()
