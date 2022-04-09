# Acknowledgement

<p align=justify>
It gives us immense pleasure to announce the completion of our project on <b>“An Enchanced Method for Information Hiding using Cryptography And Stenganography”</b> and we are pleased to acknowledge our indebtedness to all the persons who directly or indirectly contributed in the development of this work and who influenced our thinking, behavior and acts during the course of study. We are thankful to our <b><i>departmental Coordinator professor <a href="https://www.hetc.ac.in/faculty/dibyendu-samanta/">Mr. Dibyendu Samanta</a></i> (Assistant Professor and Coordinator, <a href="https://www.hetc.ac.in/">Hooghly Engineering and Technology College</a>)</b> who granted all the facilities of the college to us for the fulfilment of the project. We are thankful and express our sincere gratitude to our project guide <b><i>Mr. Dibyendu Samanta</i></b> who gave his/her valuable time to us for the sake of our project. He helped us each and every aspect of our project both academically and mentally. Finally, the team expressed their gratitude to our <b><i>respected Principal-In-Charge <a href="https://www.hetc.ac.in/faculty/smitadhi-ganguly/">Dr. Smitadhi Ganguly</a></i></b>. Without his support our project would not have seen the light of success.
</p>

> [Arijit Roy](https://www.linkedin.com/in/mr-arijit-roy/), CSE Dept., 7th Semester<br>
> University Roll No. – 17600118067<br>
> Academic Year 2021-‘22<br>

> [Arkadeep Roy](https://www.linkedin.com/in/royarkaofficial/), CSE Dept., 7th Semester<br>
> University Roll No. – 17600118065<br>
> Academic Year 2021-‘22<br>

> [Arkadip Basu Mallick](https://www.linkedin.com/in/abasuofficial/), CSE Dept., 7th Semester<br>
> University Roll No. – 17600118064<br>
> Academic Year 2021-‘22<br>

> [Shayani Das](https://www.linkedin.com/in/shayaniofficial/), CSE Dept., 7th Semester<br>
> University Roll No. – 17600118029<br>
> Academic Year 2021-‘22<br>

# Abstract

<p align="justify">
Digital images are being exchanged over various types of networks. With the huge growth of computer networks and the latest advances in digital technologies, a huge amount of digital data is being exchanged over various types of networks. It is often true that a large part of this information is confidential, private or both, which increase the demand for stronger encryption techniques. Steganography is a preferred technique for protecting the transmitted data. It is used to hide information to perform encryption. Steganography techniques are getting significantly more sophisticated and have been widely used. These techniques are the perfect supplement for encryption that allows a user to hide large amounts of information within an image. It seeks to provide a covert communication channel between two parties. The objective of this project is to provide a secret and secured communication between people. Many different carrier file formats can be used, but digital images are the most popular because of their frequency on the Internet. This project simply hides a text message in an image file. For hiding secret information in images, there exist a large variety of steganographic techniques some are more complex than others and all of them have respective strong and weak points. Different
applications have different requirements of the steganography technique used. For example, some applications may require absolute invisibility of the secret information, while others require a larger secret message to be hidden. This project intends to give an overview of cryptography, image steganography, their uses and techniques. In this proposed system Cryptography and Steganography are merged together. The contents of secret message are first kept secret by cryptography; whereas in image steganography the encrypted messages as payload are embedded into the cover image using a novel 3-3-2 LSB. The image steganography takes the advantage of human eye limitation. It uses colour image as cover media for embedding secret message. The important quality of a steganographic system is to be less distortive while increasing the size of the secret message. In this project a method is proposed to embed a colour secret image into a colour cover image. A 3-3-2 LSB insertion method has been used for image steganography.
</p>

# Table of contents

1. [Introduction](#desc-1)
2. [Literature Review](#desc-2)
3. [System Requirements](#desc-3)
4. [Theoretical Background](#desc-4)
5. [Overview of Cryptography](#desc-5)
6. [Types of Cryptography](#desc-6)
7. [Overview of Steganography](#desc-7)
8. [Types of Steganography](#desc-8)
9. [Proposed Method](#desc-9)
10. [Conclusion](#desc-10)
11. [Future Scopes](#desc-11)
12. [References](#desc-12)

<a name="desc-1"></a>
## Introduction
<p align="justify">
Steganography is defined as the art and science of writing hidden messages in such a way that no one else, apart from the intended recipient knows the existence of the message. The word “steganography” is basically of Greek origin which means “hidden writing”. The word is classified into two parts: “steganos” which means “secret” and “graphic” which means “writing”. However, in hiding information, the meaning of steganography is hiding text or secret messages into another media file such as image,
text, sound, or video. The word “steganography” is often considered similar to “cryptography” and “watermarking”. Whilst watermarking ensures message integrity and cryptography scrambles the message, steganography hides it. The primary objective of steganography is to avoid drawing attention to the transmission of hidden information. If suspicion is raised, then this objective has been planned to achieve the security of the secret message because if the hackers noted any change in the sent message, then this observer will try to know the hidden information inside the message.<br> 
The basic terminologies used in the steganography systems are the cover message, secret message, secret key, and embedding algorithm. The particular medium such as text, image, audio, video within which the message is to be hidden is known as cover medium.<br>
To provide an extra layer of security, the original message is also changed into some secret message and then it is hidden inside the cover medium. Finally, with the help of embedding algorithm secret message is hidden inside the cover medium. In steganography, before the hiding process, the sender must select an appropriate message carrier, an effective message to be hidden. A robust steganographic algorithm must be selected that should be able to embed the message more effectively. The sender then may send the hidden message to the receiver by using any of modern communication techniques. The receiver can extract the hidden message using the retrieval algorithm. This project proposes an algorithm to hide data inside an image using a secure steganographic technique.<br>
This project comprehends the following objectives –<br>
<pre>
1. Original message is converted into a secret message using a strong symmetric key cryptography algorithm.
2. Secret message is hidden inside the color cover image using 3-3-2 LSB insertion technique.
3. To produce security tool based on steganographic techniques.
</pre>
</p>

<a name="desc-2"></a>
## Literature Review
<p align="justify">
In <a href="#p-1">[1]</a> Shilpa Gupta, Geeta Gujral, and Neha Aggarwal proposed an enhanced approach of LSB steganography where distortion will be almost negligible. Authors are suggested to use 24 bitmap images to hide the secret message. The secret message is to be hidden only in the blue channel. Firstly, all the pixels within the cover image are filtered with a pixel selection filter and then the pixel with less distortion is selected and the LSB of the blue channel of that pixel is replaced by
message bits. The proposed method results in a high PSNR value compared to conventional LSB method.<br>
In <a href="#p-2">[2]</a> a new approach for LSB based image steganography using secret key is introduced by S. M. Masud Karim, Md. Saifur Rahman, and Md. Ismail Hossain. In this technique message bits are hidden in LSB of green and blue channel. One by one pixels are selected and XOR operation is performed between LSB of red channel and the first bit of secret message. If result is 0 then LSB of green channel is replaced by the message bit. Otherwise, LSB of blue channel is replaced by the message bit. Then again next bit of secret message and the LSB of red channel of the next pixel is selected and this process continues until the whole message is going to be hidden inside cover image. This method has also a high PSNR value.<br>
In <a href="#p-3">[3]</a> Mamta Juneja, and Parvinder S. Sandhu proposed a new method of hiding message into an image using LSB steganography. Firstly, message is converted into cipher using S-DES algorithm. Now, smooth edges of the cover image are detected by a custom filter composed of Canny filter and Hough transform. Then using a Pseudo Random Number Generator, pixels are selected randomly from the detected smooth edges. Finally, 1 LSB of red channel, 3 LSB of green channel, and 4 LSB of blue channel of the randomly selected pixel is replaced by the bits of the cipher message. This method has a high PSNR value because only smooth edges are slightly changed <br>
In <a href="#p-4">[4]</a> Marwa M. Emam, Abdelmgeid A. Aly, and Fatma A. Omara introduced a new approach on LSB steganography with random pixel selection. In this approach pixels are selected randomly using a Pseudo Random Number Generator. Channels are selected in a repeated manner of blue-3 green and blue channel. In blue channel 2 LSBs, and in green channel only 1 LSB is replaced by the message bit.<br>
In <a href="#p-5">[5]</a> Hamid M. Farhan, and Zena Ahmed Alwan proposed a method of doing LSB steganography by using 2 Exclusive-OR operation. First XOR is performed between LSB of red channel and the first message bit. Then second XOR is performed between result of the first XOR and LSB of green channel. Finally, the LSB of the blue channel is replaced by the result of second XOR. This process continue until the entire message is going to be hidden. This method has a high PSNR as of only ± 1 change in the blue channel of every pixel.<br>
In <a href="#p-6">[6]</a> Lip Yee Por, Delina Beh, Tang Fong Ang., and Sim Ying Ong proposed a method of steganography by combining stego one, two, three, four-bit LSBs and stego color cycle algorithm. By using color cycle algorithm, pixels are selected sequentially and 1-, 2-, 3-, and 4-bit LSB steganography is applied on each and every channel. The proposed method uses LSB substitution very effectively so that the relative change between RGB channel of stego image is minimal and it uses more secured multi-layered embedding effectively.<br>
In <a href="#p-7">[7]</a> a new method in image steganography with improved image quality is proposed by Atallah M. Al-Shatnawi, where secret messages are hidden within the randomly selected pixels. At first red channel is selected and then two message bits are taken. Then two least significant bits of red channel is taken and it is checked whether they are identical with the message bits or not. If identical then there is no need to hide that two message bits. If not identical then we take next two least significant bits of red channel and again they are checked with the message bits. If the message bits are not identical with any of the two contiguous bits of red channel, then the message bits are replaced with two least significant bits of red channel. Then again next two message bits are selected and this same process is applied on green and blue channel. Also, the hiding locations are saved in a binary table. This whole process is continued until the whole message is going to be hidden inside the cover image. This method has high PSNR value.<br>
In <a href="#p-8">[8]</a> a new encrypted method of image steganography by Sabyasachi Pramanik, Dr. R. P. Singh, Ramkrishna Ghosh where secret messages can be hidden by using the CAPTCHA codes within 4 a cover image using image steganography. Here the CAPTCHA image is embedded into a 24-bit color image using the LSB of Red, Green and Blue pixels of the 24-bit color image. For each and every character in the captcha a flag bit is set (flag bit is either 0 or 1 depending upon 0 to 1 which have lesser number of occurrences in 7-bit binary ASCII). Now this flag bit is concatenated with the 2-bit binary representation of number of occurrences of flag bit within the ASCII. Finally, this 3-bit binary is converted into decimal and it is concatenated with the positions of flag bit (calculated from left to right started with 1). Now, this final decimal string becomes particular code for that character. Similarly, code is calculated for other characters in the CAPTCHA. Now these codes are converted into binary and they are hidden according to conventional LSB.<br>
In <a href="#p-9">[9]</a>, This paper presents a novel 2-3-3 LSB insertion method. The image steganography takes the advantage of human eye limitation. It uses color image as cover media for embedding secret message. The important quality of a steganographic system is to be less distortive while increasing the size of the secret message. In this paper a method is proposed to embed a color secret image into a color cover image. A 2-3-3 LSB insertion method has been used for image steganography. Experimental results show an improvement in the Mean squared error (MSE) and Peak Signal to Noise Ratio (PSNR) values of the proposed technique over the base technique of
hash based 3-3-2 LSB insertion.
</p>
  
<a name="desc-3"></a>
## System Requirements
**Minimum Hardware Requirements**
<pre>
<b>Processor:</b> Intel Dual Core CPU @ 1.60 GHz
<b>RAM:</b> 512 MB of RAM @ 1.60 GHz
<b>Hard Disk:</b> 80 GB
</pre>

**Software Requirements**
<pre>
<b>Operating System:</b> Windows 7 / 8 / 10
<b>Tool Used:</b> Python 3
</pre>

<a name="desc-4"></a>
## Theoretical Background
<p align="justify">
The term Steganography refers to the art of covert communications. By implementing steganography, it is possible for Alice to send a secret message to Bob in such a way that no-one else will know that the message exists. Typically, the message is embedded within another object known as a cover Work, by tweaking its properties. The resulting output, known as a stegogramme is engineered such that it is a near identical perceptual model of the cover Work, but it will also contain the hidden message.<br>
It is this stegogramme that is sent between Alice and Bob. If anybody intercepts the communication, they will obtain the stegogramme, but as it is so similar to the cover, it is a difficult task for them to tell that the stegogramme is anything but innocent. It is therefore the duty of steganography to ensure that the adversary regards the stegogramme - and thus, the communication - as innocuous.<br>
One of the oldest examples of steganography dates back to around 440 BC in Greek History. Herodotus, a Greek historian from the 5th Century BC, revealed some examples of its use in his work entitled "The Histories of Herodotus". One elaborate example suggests that Histaeus, ruler of Miletus, tattooed a secret message on the shaven head of one of his most trusted slaves. After the hair had grown back, the slave was sent to Aristagorus where his hair was shaved and the message that commanded a revolt against the Persians was revealed In this example, the slave was used as the carrier for the secret message, and anyone who saw the slave as they were sent
to Aristagorus would have been completely unaware that they were carrying a message. As a result of this, the message reached the recipient with no suspicion of covert communication ever being raised.<br>
In modern terms, steganography is usually implemented computationally, where cover Works such as text files, images, audio files, and video files are tweaked in such a way that a secret message can be embedded within them. The techniques are very similar to that of digital watermarking; however, one big distinction must be highlighted between the two. In digital 7 watermarking, the focus is on ensuring that nobody can remove or alter the content of the watermarked data, even though it might be plainly obvious that it exists.<br>
Steganography on the other hand, focuses on making it extremely difficult to tell that a secret message exists at all. If an unauthorized third party is able to say with high confidence that a file contains a secret message, then steganography has failed.<br>
Steganography also differs from cryptography because the latter does not attempt to hide the fact that a message exists. Instead, cryptography merely obscures the integrity of the information so hat it does not make sense to anyone but the creator and the recipient. The adversary will be able to see that a message exists, and the inverse process of cryptanalysis involves trying to turn the meaningless information into its original form. With this said, it is still highly likely that a complete steganographic system might employ cryptographic measures as a safety-net to protect the content of the message in the event that the steganography is broken.
</p>

<a name="desc-5"></a>
## Overview of Cryptography
<p align="justify">
‘Cryptography’ this word is originated from the Greek words ‘kryptos’ meaning hidden and ‘graphein’ meaning writing. So, Cryptography is the practice of hiding messages into secret form and how to retrieve the original one from the secret one. Cryptography and the use of secret codes began thousands of years ago to communicate secretly and securely.<br>
The history of cryptography begins where many old tales do…. in ancient Egypt with hieroglyphics. These were not meant to hide messages so much as to give a formal and ceremonial touch to stories of everyday events. During the industrial age, cryptography was moved from a manual exercise to one done by machines. The invention of cipher disks and rotors for this use allowed for the creation of much more complex algorithms.<br>
Cryptography prior to the modern age was effectively synonymous with encryption, the conversion of information from a readable state to apparent nonsense. The originator of an encrypted message shared the decoding technique needed to recover the original information only with intended recipients, thereby precluding unwanted persons to do the same.<br>
Until modern times cryptography referred almost exclusively to encryption, which is the process of converting ordinary information (called plaintext) into unintelligible text (called cipher text). Decryption is the reverse, in other words, moving from the unintelligible cipher text back to plaintext. A cipher (or cypher) is a pair of algorithms that create the encryption and the reversing decryption. The detailed operation of a cipher is controlled both by the algorithm and in eachinstance by a "key". This is a secret (ideally known only to the communicants), usually a short string of characters, which is needed to decrypt the cipher text. A "cryptosystem" is the ordered list of elements of finite possible plaintexts, finite possible cipher texts, finite possible keys, and the encryption and decryption algorithms which correspond to each key. Keys are important, as ciphers without variable keys can be trivially broken with only the knowledge of the cipher used and are therefore useless (or even counter-productive) for most purposes.
</p>

<a name="desc-6"></a>
## Types of Cryptography
Modern Cryptography is of 3 types.<br>
<center>
<img src="https://github.com/aroyofficial/incognitobit/blob/main/images/readme/fig-1.png" style="display: block; margin-left: auto; margin-right: auto;"></img>
</center>
<p align="center">Figure I. Types of Cryptography</p>
<p align="justify">
<b>a) Symmetric / Public key cryptography</b> is a group of cryptographic algorithms where using the same key a message is encrypted on the sender side and decrypted on the receiver side. The encryption and decryption key are same; that is why this is known as public key cryptography. Again, this type of cryptography is divided into two different types. One is block cipher (plain text is divided into fixed or variable length of blocks and encryption is applied on each and every block) and another is stream cipher (a stream of keys is generated and then using them encryption is applied). This was the only kind of encryption publicly known until June 1976.Only agents with the secret key can encrypt or decrypt the data. Some popular symmetric key cryptographic algorithms are AES, DES, etc. An example is given in Figure II.
</p>
<center><img src="https://github.com/aroyofficial/incognitobit/blob/main/images/readme/fig-2.png"></img></center>
<p align="center">Figure II. Symmetric/Public key cryptography</p>
<p align="justify">
b) Asymmetric / Private key cryptography is a group of cryptographic algorithms where different keys are used for encryption and decryption process. This is also known as private key cryptography because encryption and decryption keys are not same; rather we can say they are private. A significant disadvantage of symmetric ciphers is the key management necessary to use them securely. Each distinct pair of communicating parties must, ideally, share a different key, and perhaps each cipher text exchanged as well. In a groundbreaking 1976 paper, Whitfield Diffie and Martin Hellman proposed the notion of public-key (also, more generally, called asymmetric key) cryptography in which two different but mathematically related keys are used—a public key and a private key. A public key system is so constructed that calculation of one key (the 'private key') is computationally infeasible from the other (the 'public key'), even though they are necessarily related. Instead, both keys are generated secretly, as an interrelated pair. Some popular asymmetric key cryptographic algorithms are RSA, Diffie-Hellman, etc. An example is given in Figure III.
</p>
<center><img src="https://github.com/aroyofficial/incognitobit/blob/main/images/readme/fig-3.png"></img></center>
<p align="center">Figure III. Asymmetric/Private key cryptography</p>
<p align="justify">
<b>c) Hashing</b> is a technique where a mathematical function is taken, generally known as hash function. By applying the hash function plain text is converted into cipher text. A cryptographic hash function is an algorithm that takes an arbitrary amount of data input—a credential—and produces a fixed-size output of enciphered text called a hash value, or just “hash.” That enciphered text can then be stored instead of the password itself, and later used to verify the user.<br>
Certain properties of cryptographic hash functions impact the security of password storage.<br> 
Non-reversibility, or one-way function. A good hash should make it very hard to reconstruct the original password from the output or hash.<br>
Diffusion, or avalanche effect. A change in just one bit of the original password should result in change to half the bits of its hash. In other words, when a password is changed slightly, the output of enciphered text should change significantly and unpredictably.<br>
Determinism. A given password must always generate the same hash value or enciphered text.<br>
Collision resistance. It should be hard to find two different passwords that hash to the same enciphered text.<br>
Non-predictable. The hash value should not be predictable from the password. Some popular hashing algorithms are SHA-256, MD5, etc.<br>
A particular cryptographic algorithm from any of the above categories must assure some parameters in order to consider it as a strong algorithm. The parameters are key-length, confusion and diffusion, external factors for system design, etc.<br>
<b>Cryptanalysis:</b> Cryptanalysis refers to the process of analyzing information systems in order to understand hidden aspects of the systems. Cryptanalysis is used to breach cryptographic security systems and gain access to the contents of encrypted messages, even if the cryptographic key is unknown.<br>
In addition to mathematical analysis of cryptographic algorithms, cryptanalysis includes the study of side-channel attacks that do not target weaknesses in the cryptographic algorithms themselves, but instead exploit weaknesses in their implementation.<br>
Even though the goal has been the same, the methods and techniques of cryptanalysis have changed drastically through the history of cryptography, adapting to increasing cryptographic complexity, ranging from the pen-and-paper methods of the past, through machines like the British Bombes and Colossus computers at Bletchley Park in World War II, to the mathematically advanced computerized schemes of the present. Methods for breaking modern cryptosystems often involve solving carefully constructed problems in pure mathematics, the best-known being integer factorization.<br>
</p>

<a name="desc-7"></a>
## Overview of Steganography
<p align="justify">
The word ‘steganography’ originated from the Greek word ‘steganographia’. This word was first ever founded in the year 1499 in the book of a Greek author named Johannes Trithemius. This word is basically a combination of two separate words. ‘steganos’ means hiding or hiding within something and ‘graphia’ means writing. So, steganography is the practice of hiding messages inside any medium, etc. The particular medium such as text, image, audio, video within which the message is to be hidden is known as cover medium. To provide an extra layer of security, the original message is also changed into some secret message and then it is hidden inside the cover medium. Steganography based communication over easily accessible platforms to prevent leakage of information. Here, embedding of information in a cover image is shown below:
</p>
<center><img src="https://github.com/aroyofficial/incognitobit/blob/main/images/readme/fig-4.png"></img></center>
<p align="center">Figure IV. Stego System</p>
<p align="justify">
Information is added by the sender and if the receiver wants to get the original image, then he needs to extract the embedded image with the help of the secret information provided by the sender. When the receiver will receive the file will be in the embedded form and by extracting it he or she can use or read the original object file which is sent by the sender. This embedding of the binary code is different for the different types of the files.
</p>

<a name="desc-8"></a>
## Types of Steganography
Based on the cover medium there are different types of steganography which are given below in the Figure V.
<center><img src="https://github.com/aroyofficial/incognitobit/blob/main/images/readme/fig-5.png"></img></center>
<p align="center">Figure V. Types of Steganography</p>
<p align="justify">
In modern steganography, especially digital steganography becomes popular and stand apart from others. In digital steganography, different multimedia files are used to hide the message. Due to the large media file size; it is also hard to find the message within the cover medium. There are several techniques of doing the digital steganography. They are given below in the Figure VI.
</p>
<center><img src="https://github.com/aroyofficial/incognitobit/blob/main/images/readme/fig-6.png"></img></center>
<p align="center">Figure VI. Steganography Techniques</p>
<p align="justify">
Within these techniques, spatial and transform domain techniques are mostly used.<br>
<ul>
  <li>   Image Steganography</li>
  <b>a) LSB</b> stands for Least Significant Bit steganography. In this technique, least significant bits are replaced with the message bits so that the minimum distortion will be resulted in the cover medium and which is imperceptible to the human eye. In Figure III an example is given
</ul>
</p>
  
<a name="desc-9"></a>
## Proposed Method

<a name="desc-10"></a>
## Conclusion

<a name="desc-11"></a>
## Future Scope

<a name="desc-12"></a>
## References
<p align="justify">
<a name="p-1"></a>
[1] Shilpa Gupta, Geeta Gujral, and Neha Aggarwal, “Enhanced least significant bit algorithm for image steganography,” International Journal of Computational Engineering & Management, vol. 15, issue 4, July 2012.<br>
<a name="p-2"></a>
[2] S. M. Masud Karim, Md. Saifur Rahman, Md. Ismail Hossain, “A new approach for lsb based image steganography using secret key,” Proceedings of 14th International Conference on Computer and Information Technology (ICCIT 2011), 22-24 December, 2011, Dhaka, Bangladesh.<br>
<a name="p-3"></a>
[3] Mamta Juneja, and Parvinder S. Sandhu, “An improved lsb based steganography technique for rgb color Images,” International Journal of Computer and Communication Engineering, vol. 2, no. 4, July 2013.<br>
<a name="p-4"></a>
[4] Marwa M. Emam, Abdelmgeid A. Aly, Fatma A. Omara, “An improved image steganography method based on lsb technique with random pixel selection,” International Journal of Advanced Computer Science and Applications, vol. 7, no. 3, 2016.<br>
<a name="p-5"></a>
[5] Hamid Mohammed Farhan, and Zena Ahmed Alwan, “Improved method using a two exclusive-or to binary image in rgb color image steganography,” International Journal of Engineering and Technology, vol. 7, no. 4, pp. 4295–4299, 2018.<br>
<a name="p-6"></a>
[6] Lip Yee Por, Delina Beh, Tan Fong Ang, and Sim Ying Ong, “An enhanced mechanism for image steganography using sequential colour cycle algorithm,” The International Arab Journal of Information Technology, vol. 10, no. 1, January 2013.<br>
<a name="p-7"></a>
[7] Atallah M. Al-Shatnawi, “A new method in image steganography with improved image quality,” Applied Mathemetical Sciences, vol. 6, no. 79, pp. 3907–3915, 2012.<br>
<a name="p-8"></a>
[8] Sabyasachi Pramanik, Dr. R. P. Singh, and Ramkrishna Ghosh, “A new encrypted method in image steganography,” Indonesian Journal of Electrical Engineering and Computer Science, vol. 14, no. 3, pp. 1412– 1419, June 2019.<br>
<a name="p-9"></a>
[9] G.R.Manjula and Ajit Danti; A Novel Hash Based Least Significant Bit (2-3-3) Image Steganography in Spatial Domain. International Journal of Security, Privacy and Trust Management (IJSPTM) Vol 4, No 1, February 2015.
</p>
  
# Project IncognitoBit

This project comes with a **_GUI_** using which users can hide any message within an image and also they can retrieve the message from a stego image (which contains a message). This project **_implements a secure steganographic algorithm_** which is described in this document.

# Project Description
