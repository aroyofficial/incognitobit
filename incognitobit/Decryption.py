# Decryption class has all functionalities for decryption of the cipher used in this project
class Decryption:

    def __init__(self):
        pass

    # Match received token with the original token
    def _matchToken(self, received_token, original_token, private_key):
        self.__private_key = private_key
        self.__token = []
        
        # Iterate for each 8-bit tuple of received token
        for binstring in received_token:
            # Reverse each tuple
            binstring = binstring[::-1]
            # Split the 8 bit tuple from middle 
            # Then convert it into the corresponding character using private key
            self.__token.append(chr(int(binstring[:4], 2) * self.__private_key + int(binstring[4:], 2)))
        
        # Finally convert characters to get the token in string representation 
        # Then compare it to original token
        if "".join(self.__token) == original_token:
            return True
        return False

    # Decrypt message from the encrypted text
    def _decryptMessage(self, msg):
        self.__encrypted_text = msg
        self.__plain_text = []

        # Iterate for each 8-bit tuple of received token
        for binstring in self.__encrypted_text:
            # Reverse each tuple
            binstring = binstring[::-1]
            # Split the 8-bit tuple from middle
            # Then conver it into the corresponding character using private key
            self.__plain_text.append(chr(int(binstring[:4], 2) * self.__private_key + int(binstring[4:], 2)))
        
        # Finally join characters to get the string representation of plain text
        return "".join(self.__plain_text)
