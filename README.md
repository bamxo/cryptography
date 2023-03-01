# Cryptography

Description: cryptography.py imports stenography.py and codec.py to manipulate the pixel values in a given image to encode and decode secret messages

Functionality:
- messages can be hidden in the pixel values of an image by converting the secret messege into ASCII code then evaluating if the current pixel value is divisible by the ASCII code
- we encode jpg files and save them as png files to preserve the pixel count
- we can decode messages the same way until we have reached the delimiter, in our case it will be '#'
- there are 3 ways we can encode and decode messages: Codec, CaeserCypher, and HuffmanCodes
 - Codec: the process of encoding and decoding messages are the same as mentioned above
 - CaeserCypher: the process of encoding and decoding messages are the same as mentioned above, except the letters are shifted 3 letters to the right when encoding and then shifted 3 letters to the left when decoding. this preserves the secret message and adds an extra layer of security
 - HuffmanCodes: using the HuffmanCodes data compression method, we create a tree with the of the encoded messages then save that into the png file. to decode the png file, we traverse the tree going left if the bit is 0 and going right if the bit is 1, until we have reached our delimiter
