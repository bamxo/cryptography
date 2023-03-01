# author: Landon Nguyen
# date: February 17, 2023
# file: stenography.py a Python file that defines a Stenography
# input: image and string
# output: image encoded with a hidden message within its pixel array and decodes images with hidden message

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        #print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message+self.delimiter)

        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            # your code goes here
            # you may create an additional method that modifies the image array
            index = 0
            for a in range(len(image)):
                for r in range(len(image[a])):
                    for c in range(len(image[a][r])):
                        if index >= len(self.binary):
                            break
                        if int(self.binary[index]) % 2 == 0:
                            if image[a][r][c] % 2 != 0:
                                image[a][r][c] -= 1
                        else:
                            if image[a][r][c] % 2 != 1:
                                image[a][r][c] -= 1
                        index += 1


            cv2.imwrite(fileout, image)
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        #print(image) # for debugging      
        flag = True
        
        # convert into text
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # your code goes here
            # you may create an additional method that extract bits from the image array
            binary_data = ''
            for a in range(len(image)):
                for r in range(len(image[a])):
                    for c in range(len(image[a][r])):
                        if len(binary_data) >= 8:
                            if binary_data[len(binary_data)-8:len(binary_data)] == format(ord('#'),'08b'):
                                break
                        if image[a][r][c] % 2 == 0:
                            binary_data += '0'
                        else:
                            binary_data += '1'

            # update the data attributes:
            self.text = self.codec.decode(binary_data)
            self.binary = binary_data
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

if __name__ == '__main__':
    
    s = Steganography()
    
    s.encode('fractal.jpg', 'fractal.png', 'hello', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    s.decode('fractal.png', 'binary')
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'
    print('Everything works!!!')
   
