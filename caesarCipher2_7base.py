def askUser():
	invalidMode= True
	while(invalidMode):
		print "do you want to encrypt (type encrypt and press enter), decrypt (type decrypt and enter) or brute force (type force and enter)?"
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
  #this is a function which you will write!
  #currently returns a hard coded shift value, you could change this to
  #get input from the user and return that!
  shiftValue=3      
  return shiftValue      


def force(msg):
  ##################################################
  #brute force decrypt - i.e. try all possible keys
  ##################################################
  print "attempting to force decrypt of " + msg + " now! - results are:"
  print ("oops, you haven't coded this part yet!")
  ##################################################
  #outer loop - letters of alphabet
  ##################################################
  
          ##################################################
          #inner loop - letters of message
          ##################################################
          
          ######################
          # inner loop ends here
          #######################
          #back to outer loop

          #end of outer loop



def decrypt(msg,shiftValue):
        print "decrypting " + msg + " now! - your decrypted message is:"
        print "oops you haven't written this part yet!"



def encrypt(msg, shiftValue):
        print "encrypting " + msg + " now! - your encrypted message is:"
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
        print result


ALPHABET_SIZE=26
main()