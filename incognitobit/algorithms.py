import hashlib
import random
import numpy as np
from PIL import Image
import math
import os
from pathlib import Path
from incognitobit.encryption import Encryption
from incognitobit.decryption import Decryption

# custom exception for non-capable images
class ImageNotCapableError(Exception, Decryption):
    
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self) -> str:
        return self.__msg


class Steganography(Encryption):

    # initialization of encryption object state
    def __init__(self, path = None, msg = None):
        if path is not None and msg is not None:
            try:
                self.__stego_filename = os.path.basename(path)
                self.__cover_image = Image.open(path, 'r')  # open cover image from the given path
                self.__cover_image_width, self.__cover_image_height = self.__cover_image.size  # extract height and width of image
                self.__cover_image_arr = np.array(list(self.__cover_image.getdata()))  # extract the image array from the Image object
                self.__cover_image_mode = self.__cover_image.mode  # get the mode of the cover image
                self.__cover_image_channel = len(self.__cover_image.mode)  # get the no. of channels present in the cover image
                self.__cover_image_net_pixels = self.__cover_image_arr.size // self.__cover_image_channel  # get the total no of pixels present in the cover image
                self.__getStegoKey()  # get stego key
                self.__plain_text = list(msg)  # convert message into list of characters
                self.__encryption_object = Encryption(self.__plain_text)
                self.__private_key = self.__encryption_object._getPrivateKey()  # get private key
                self.__generateAuthorizationToken()  # get authorization token
                self.__required_bits = (len(self.__plain_text) + 16) * 8  # stores the no. of pixels required to hide the message
                self.__encrypted_msg = self.__encryption_object._encryptMessage(list(self.__token))
            except:
                pass
        if path is not None and msg is None:
            try:
                self.__stego_image = Image.open(path, 'r')
                self.__stego_image_width, self.__stego_image_height = self.__stego_image.size
                self.__stego_image_arr = np.array(list(self.__stego_image.getdata()))
            except:
                pass

    # generate stego key from the image width
    def __getStegoKey(self):
        self.__stego_key = random.randint(0, self.__cover_image_width)

    # generate authorization token
    def __generateAuthorizationToken(self):
        self.__token = hashlib.sha256(str(self.__private_key ^ self.__stego_key).encode('utf-8')).hexdigest()[:16]

    # get encryption packet which contains data related to encryption
    # +--------------------+-----------+-------------+
    # | message bit length | stego key | private key |
    # +--------------------+-----------+-------------+
    def __getEncryptionPacket(self):
        self.__encryption_info = list(map(int, list(format(self.__private_key, '04b') + format(self.__stego_key, f"0{self.__bits_required_for_stego_key}b") + format(self.__required_bits, f"0{self.__bits_required_for_message_length}b"))))

    # hide encryption packet in the last row of cover image array
    def __hideEncryptionPacket(self):
        self.__bits_required_for_stego_key = math.ceil(math.log(self.__cover_image_width, 2))
        self.__bits_required_for_private_key = 4
        self.__bits_required_for_message_length = self.__cover_image_width - (self.__bits_required_for_stego_key + self.__bits_required_for_private_key)
        self.__getEncryptionPacket()
        index = 0
        i = -1
        inner_loop = False
        while True:
            second_for_loop = False
            for j in range(3):
                temp = list(map(int, list(format(self.__cover_image_arr[i][j], "08b"))))
                if j == 0:
                    for k in range(3):
                        if index == self.__cover_image_width:
                            inner_loop = True
                            break
                        temp[-(k + 1)] = self.__encryption_info[index]
                        index += 1
                elif j == 1:
                    if index == self.__cover_image_width:
                        inner_loop = True
                        break
                    temp[-4] = self.__encryption_info[index]
                    index += 1
                    for k in range(2):
                        if index == self.__cover_image_width:
                            inner_loop = True
                            break
                        temp[-(k + 1)] = self.__encryption_info[index]
                        index += 1
                else:
                    for k in range(2):
                        if index == self.__cover_image_width:
                            inner_loop = True
                            break
                        temp[-(k + 3)] = self.__encryption_info[index]
                        index += 1
                temp = list(map(str, temp))
                self.__cover_image_arr[i][j] = int("".join(temp), 2)
                if inner_loop:
                    second_for_loop = True
                    break
            if second_for_loop:
                break
            i -= 1

    # hide plain text message within the cover image
    def __hideEncryptedMessage(self):
        for i in range(self.__stego_key, self.__stego_key + (self.__required_bits // 8)):
            index = 0
            for j in range(3):
                temp = list(map(int, list(format(self.__cover_image_arr[i][j], '08b'))))
                if j == 0:
                    for k in range(3):
                        temp[-(k + 1)] = int(self.__encrypted_msg[i - self.__stego_key][index: index + 1])
                        index += 1
                elif j == 1:
                    temp[-4] = int(self.__encrypted_msg[i - self.__stego_key][index: index + 1])
                    index += 1
                    for k in range(2):
                        temp[-(k + 1)] = int(self.__encrypted_msg[i - self.__stego_key][index: index + 1])
                        index += 1
                else:
                    for k in range(2):
                        temp[-(k + 3)] = int(self.__encrypted_msg[i - self.__stego_key][index: index + 1])
                        index += 1
                temp = list(map(str, temp))
                self.__cover_image_arr[i][j] = int("".join(temp), 2)

    def _generateStegoImage(self):
        try:
            # raise ImageNotCapableError("Image is not capable for hiding the message")
            self.__status = None
            if self.__cover_image_net_pixels - (self.__cover_image_width + self.__stego_key) < self.__required_bits // 8:
                raise ImageNotCapableError("Image is not capable for hiding the message")
            self.__hideEncryptionPacket()
            self.__hideEncryptedMessage()
            self.__cover_image_arr  = self.__cover_image_arr.reshape(self.__cover_image_height, self.__cover_image_width, self.__cover_image_channel)
            self._stego_image = Image.fromarray(self.__cover_image_arr.astype('uint8'), self.__cover_image_mode)
            self.__status = "Stego Image generated successfully"
        except ImageNotCapableError as error:
            self.__status = error.__str__()
        except Exception:
            self.__status = "Some error occured"
        finally:
            return self.__status

    def _saveStegoImage(self, filepath):
        self._stego_image.save(Path(filepath))

    def __retrieveEncryptedText(self):
        self.__encrypted_msg = []
        for i in range(self.__stego_key, self.__stego_key + (self.__msg_length_in_bits // 8)):
            index = 0
            binstring = ''
            for j in range(3):
                temp = list(format(self.__stego_image_arr[i][j], '08b'))
                if j == 0:
                    for k in range(3):
                        binstring += temp[-(k + 1)]
                elif j == 1:
                    binstring += temp[-4]
                    for k in range(2):
                        binstring += temp[-(k + 1)]
                else:
                    for k in range(2):
                        binstring += temp[-(k + 3)]
            self.__encrypted_msg.append(binstring)

    def __getEncryptionInfo(self):
        self.__encryption_info = []
        index = 0
        i = -1
        inner_loop = False
        while True:
            second_for_loop = False
            for j in range(3):
                temp = list(format(self.__stego_image_arr[i][j], "08b"))
                if j == 0:
                    for k in range(3):
                        if index == self.__stego_image_width:
                            inner_loop = True
                            break
                        self.__encryption_info.append(temp[-(k + 1)])
                        index += 1
                elif j == 1:
                    if index == self.__stego_image_width:
                        inner_loop = True
                        break
                    self.__encryption_info.append(temp[-4])
                    index += 1
                    for k in range(2):
                        if index == self.__stego_image_width:
                            inner_loop = True
                            break
                        self.__encryption_info.append(temp[-(k + 1)])
                        index += 1
                else:
                    for k in range(2):
                        if index == self.__stego_image_width:
                            inner_loop = True
                            break
                        self.__encryption_info.append(temp[-(k + 3)])
                        index += 1
                if inner_loop:
                    second_for_loop = True
                    break
            if second_for_loop:
                break
            i -= 1
        self.__private_key = int("".join(self.__encryption_info[:4]), 2)
        temp = math.ceil(math.log(self.__stego_image_width, 2))
        self.__stego_key = int("".join(self.__encryption_info[4: temp + 4]), 2)
        self.__msg_length_in_bits = int("".join(self.__encryption_info[temp + 4:]), 2)

    def _retrieveMessage(self):
        self.__getEncryptionInfo()
        self.__generateAuthorizationToken()
        self.__retrieveEncryptedText()
        self.__decryption_object = Decryption(self.__encrypted_msg, self.__private_key)
        self.__decryptedText = self.__decryption_object._decryptMessage()
        if self.__decryptedText[-(len(self.__token)):] == self.__token:
            return self.__decryptedText[:-(len(self.__token))]
        return ''