# Import required packages and modules
import os
import math
import random
import hashlib
import numpy as np
from PIL import Image
from pathlib import Path
from incognitobit.Encryption import Encryption
from incognitobit.Decryption import Decryption

# Custom exception for non-capable images
class ImageNotCapableError(Exception, Decryption):

    # Exception initializer 
    def __init__(self, msg):
        self.__msg = msg

    # Exception message generator
    def __str__(self) -> str:
        return self.__msg

# Steganography class has all functionalities to embed a message inside an image 
# Using the algorithm discussed in the README.md
class Steganography(Encryption):

    # Backend initialization for encryption
    def __init__(self, path = None, msg = None):
        if path is not None and msg is not None:
            try:
                # Open cover image from the given path
                self.__cover_image = Image.open(path, 'r')
                # Extract height and width of image
                self.__cover_image_width, self.__cover_image_height = self.__cover_image.size
                # Extract the image array from the Image object
                self.__cover_image_arr = np.array(list(self.__cover_image.getdata()))
                # Get the mode of the cover image
                self.__cover_image_mode = self.__cover_image.mode
                # Get the no. of channels present in the cover image
                self.__cover_image_channel = len(self.__cover_image.mode)
                # Get the total no of pixels present in the cover image
                self.__cover_image_net_pixels = self.__cover_image_arr.size // self.__cover_image_channel
                
                # Get stego key
                self.__getStegoKey()
                
                # Convert message into list of characters
                self.__plain_text = list(msg)
                
                # Create an object of Encryption class
                self.__encryption_object = Encryption(self.__plain_text)
                # Generate private key for encryption
                self.__private_key = self.__encryption_object._getPrivateKey()
                
                # Get authorization token
                self.__generateAuthorizationToken()

                # Store the no. of pixels required to hide the message
                self.__required_bits = (len(self.__plain_text) + 16) * 8
                
                # Get cipher from plain text
                self.__encrypted_msg = self.__encryption_object._encryptMessage(list(self.__token))
            except:
                pass
        
        # Backend initialization for decryption
        if path is not None and msg is None:
            try:
                # Open stego image from the given path
                self.__stego_image = Image.open(path, 'r')
                # Extract height and width of image
                self.__stego_image_width, self.__stego_image_height = self.__stego_image.size
                # Extract the image array from the image object
                self.__stego_image_arr = np.array(list(self.__stego_image.getdata()))
            except:
                pass

    # Generate stego key from the image width
    def __getStegoKey(self):
        # Take a random number between 0 to cover image width as stego key
        self.__stego_key = random.randint(0, self.__cover_image_width)

    # Generate authorization token
    def __generateAuthorizationToken(self):
        # Do bitwise XOR between stego key and private key
        # Then take the string representation of the XOR outcome
        # Then take the first 16 characters of that MD5 hash as authorization token
        self.__token = hashlib.sha256(str(self.__private_key ^ self.__stego_key).encode('utf-8')).hexdigest()[:16]

    # Use the last row of image to embed the necessary information
    # To decrypt the message at reciever's end
    # +--------------------+-----------+---------+
    # | message length | stego key | private key |
    # +--------------------+-----------+---------+
    # All data should be represented in the binary format
    def __getEncryptionPacket(self):
        self.__encryption_info = list(map(int, list(format(self.__private_key, '04b') + format(self.__stego_key, f"0{self.__bits_required_for_stego_key}b") + format(self.__required_bits, f"0{self.__bits_required_for_message_length}b"))))

    # hide encryption packet in the last row of cover image array
    def __hideEncryptionPacket(self):
        # Get how many bits are required to embed stego key
        self.__bits_required_for_stego_key = math.ceil(math.log(self.__cover_image_width, 2))
        # Get how many bits are required to embed private key
        self.__bits_required_for_private_key = 4
        # Get how many bits are required to embed message length
        self.__bits_required_for_message_length = self.__cover_image_width - (self.__bits_required_for_stego_key + self.__bits_required_for_private_key)
        # Get encryption packet (contains info for decryption)
        self.__getEncryptionPacket()
        index = 0
        i = -1
        inner_loop = False
        # Iterate until the encryption packet embed
        while True:
            second_for_loop = False

            # Iterate through each pixel
            for j in range(3):
                temp = list(map(int, list(format(self.__cover_image_arr[i][j], "08b"))))
                
                # Red channel
                if j == 0:
                    for k in range(3):
                        if index == self.__cover_image_width:
                            inner_loop = True
                            break
                        temp[-(k + 1)] = self.__encryption_info[index]
                        index += 1
                
                # Green channel
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
                
                # Blue channel
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

    # Hide plain text message within the cover image
    def __hideEncryptedMessage(self):
        # Embed message bits
        for i in range(self.__stego_key, self.__stego_key + (self.__required_bits // 8)):
            index = 0

            # Iterate through each pixel
            for j in range(3):
                temp = list(map(int, list(format(self.__cover_image_arr[i][j], '08b'))))
                
                # Red channel
                if j == 0:
                    for k in range(3):
                        temp[-(k + 1)] = int(self.__encrypted_msg[i - self.__stego_key][index: index + 1])
                        index += 1
                
                # Green channel
                elif j == 1:
                    temp[-4] = int(self.__encrypted_msg[i - self.__stego_key][index: index + 1])
                    index += 1
                    for k in range(2):
                        temp[-(k + 1)] = int(self.__encrypted_msg[i - self.__stego_key][index: index + 1])
                        index += 1
                
                # Blue channel
                else:
                    for k in range(2):
                        temp[-(k + 3)] = int(self.__encrypted_msg[i - self.__stego_key][index: index + 1])
                        index += 1

                temp = list(map(str, temp))
                self.__cover_image_arr[i][j] = int("".join(temp), 2)

    # Generate stego image from cover image
    def _generateStegoImage(self):
        try:
            self.__status = None

            # If image is not capable for hiding the message
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

    # Save stego image in the local machine
    def _saveStegoImage(self, filepath):
        self._stego_image.save(Path(filepath))

    # Extract authorization token from the stego image
    def __getToken(self):
        self.__received_token = []

        for i in range(self.__stego_key, self.__stego_key + 16):
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
            
            self.__received_token.append(binstring)

    # Retrieve encrypted text from the stego image
    def __retrieveEncryptedText(self):
        self.__encrypted_msg = []
        
        for i in range(self.__stego_key + 16, self.__stego_key + (self.__msg_length_in_bits // 8)):
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
            progress = (i - self.__stego_key + 16 + 1) // ((self.__msg_length_in_bits // 8) / 100)
            self.__makeProgress(progress)

    # Get encryption packet from the stego image
    # From which stego key, private key, and message length will be retrieved
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

    # Update progress bar while retrieving the message from the stego image
    def __makeProgress(self, value):
        self.__loading_bar['value'] = value
        self.__root.update_idletasks()

    # Retrieve message from stego image
    def _retrieveMessage(self, masterwidget, loadingbar):
        try:
            self.__root = masterwidget
            self.__loading_bar = loadingbar
            self.__makeProgress(0)
            self.__getEncryptionInfo()
            if self.__private_key < 8 or self.__stego_key > self.__stego_image_width:
                return ''
            self.__generateAuthorizationToken()
            self.__getToken()
            self.__decryption_object = Decryption()
            if not self.__decryption_object._matchToken(self.__received_token, self.__token, self.__private_key):
                return ''
            self.__retrieveEncryptedText()
            self.__decryptedText = self.__decryption_object._decryptMessage(self.__encrypted_msg)
            self.__makeProgress(100)
            return self.__decryptedText
        except:
            return ''