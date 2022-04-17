# Import required packages and modules
import random

# Encryption class has all functionalities which also contains the algorithm to generate cipher
class Encryption:

    # Encryption initializer
    def __init__(self, msg):
        self.__plain_text = msg

    # Generate private key
    def _getPrivateKey(self):
        # Iterate until private key is not generated
        while True:
            # Take a random integer between 1 and message length
            self.__r = random.randint(1, len(self.__plain_text))
            
            # Take the first 4 binary bits of that random number
            self.__private_key = int(format(ord(self.__plain_text[self.__r]), "08b")[:4], 2)
            # If it is greater than 111 then take it as private key
            if self.__private_key >= 8:
                break
            
            # Take the last 4 binary bits of that random number
            self.__private_key = int(format(ord(self.__plain_text[self.__r]), "08b")[4:], 2)
            # If it is greater than 111 then take it as private key
            if self.__private_key >= 8:
                break
        
        return self.__private_key

    # Encrypt the plain text
    def _encryptMessage(self, token):
        # Add token before the message to be embedded
        self.__plain_text = token + self.__plain_text
        self.__encrypted_msg = []

        # Iterate for each character of plain text to be embedded
        for char in self.__plain_text:
            # Convert each character to a specified code
            temp = (format(ord(char) // self.__private_key, "04b") + format(ord(char) % self.__private_key, "04b"))[::-1]
            # Append that code with encrypted message
            self.__encrypted_msg.append(temp)
        
        return self.__encrypted_msg
