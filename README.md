Crypto-Dojo
=============

Materials to support a cryptography themed dojo <br/>


## How to use 

The repository contains two python programs that implement encryption and decryption using a <a href="http://en.wikipedia.org/wiki/Caesar_cipher"> Caesar Cipher.  

File [caesarCipher2_7base.py] has a cut-down version of the program that has a complete encryption function but only skeletons for decrypt and brute force functions.  The key (the value to shift letters by to encrypt) is also hard coded.  This allows coders to work out for themselves how to code decrypt, brute force, and obtaining the key.

File [caesarCipher2_7original.py] contains the complete program in case any of the coders runs out of time or finds the task too challenging.  The inner loop in the nested loop in the brute-force function could be replaced by the decrypt function, but it can be a useful way of introducing nested loops.

The repository also contains a python program that implements a Vignere cipher.  This uses the encrypt and decrypt functions from the Caesar Cipher program, so link in to the previous code.   The vigenere program also allows you to customise your program by setting the EVIL_ORGANISATION variable.


## Authors 
[Claire Quigley](https://github.com/alcluith) <br/>
Rose <br/>


## Licence

<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US">Creative Commons Attribution-NonCommercial 3.0 Unported License</a>.


