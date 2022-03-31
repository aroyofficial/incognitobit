class Decryption:

    def __init__(self, msg=None, key=None):
        if key is not None:
            self.__encrypted_text = msg
            self.__private_key = key

    # decrypt message from the encrypted text
    def _decryptMessage(self):
        self.__plain_text = []
        for binstring in self.__encrypted_text:
            binstring = binstring[::-1]
            self.__plain_text.append(chr(int(binstring[:4], 2) * self.__private_key + int(binstring[4:], 2)))
        return "".join(self.__plain_text)