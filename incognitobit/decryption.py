class Decryption:

    def __init__(self):
        pass

    # match received token with the original token
    def _matchToken(self, received_token, original_token, private_key):
        self.__private_key = private_key
        self.__token = []
        for binstring in received_token:
            binstring = binstring[::-1]
            self.__token.append(chr(int(binstring[:4], 2) * self.__private_key + int(binstring[4:], 2)))
        temp = "".join(self.__token)
        if "".join(self.__token) == original_token:
            return True
        return False

    # decrypt message from the encrypted text
    def _decryptMessage(self, msg):
        self.__encrypted_text = msg
        self.__plain_text = []
        for binstring in self.__encrypted_text:
            binstring = binstring[::-1]
            self.__plain_text.append(chr(int(binstring[:4], 2) * self.__private_key + int(binstring[4:], 2)))
        return "".join(self.__plain_text)