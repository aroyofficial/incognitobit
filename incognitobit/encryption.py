import random

class Encryption:

    def __init__(self, msg):
        self.__plain_text = msg

    # generate private key
    def _getPrivateKey(self):
        while True:
            self.__r = random.randint(1, len(self.__plain_text))
            self.__private_key = int(format(ord(self.__plain_text[self.__r]), "08b")[:4], 2)
            if self.__private_key >= 8:
                break
            self.__private_key = int(format(ord(self.__plain_text[self.__r]), "08b")[4:], 2)
            if self.__private_key >= 8:
                break
        return self.__private_key

    # encrypt the plain text
    def _encryptMessage(self, token):
        self.__plain_text += token
        self.__encrypted_msg = []
        for char in self.__plain_text:
            temp = (format(ord(char) // self.__private_key, "04b") + format(ord(char) % self.__private_key, "04b"))[::-1]
            self.__encrypted_msg.append(temp)
        return self.__encrypted_msg