# REFERENCE TO THE CLASS IN DT228B_Lib package
import sys
import os
# Reference Class Library DT228b_lib
from DT228B_LIB.MyEncryptor import MyEncryptor

# sample string to encode
stringToEncode = "secret"
# sample file to encode
fileToEncode = "sample_file_for_lab2.txt"

# INSTANTIATE THE MyEncryptor Class
lab1 = MyEncryptor()
# PRINT OUT TO THE CONSOLE THE VARIOUS HASH VALUES by calling the different methods

print "Encoding the following string %r" % stringToEncode
print "Sha1 file encode : ", lab1.sha1Encode(stringToEncode)
print "Sha256 version : ", lab1.sha256Encode(stringToEncode)
print "Sha512 version : ", lab1.sha512Encode(stringToEncode)
print "Sha3 256 bit version OF FILE : ", lab1.sha3_256Encode(fileToEncode)
print "Sha3 512 bit version OF FILE : ", lab1.sha3_512Encode(fileToEncode)
