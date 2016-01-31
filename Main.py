# REFERENCE TO THE CLASS IN DT228B_Lib package
from DT228B_LIB.MyEncryptor import MyEncryptor
# sample string to encode

stringToEncode = "secret"
# sample file to encode
fileToEncode = "sample_file_for_lab2.txt"

# INSTANTIATE THE MyEncryptor Class
lab1 = MyEncryptor()
#PRINT OUT TO THE CONSOLE THE VARIOUS HASH VALUES
print "Encoding the following string %r" %stringToEncode
print "Sha1 file encode : ", lab1.sha1Encode(stringToEncode)
print "Sha256 version : ", lab1.sha256Encode(stringToEncode)
print "Sha512 version : ", lab1.sha512Encode(stringToEncode)
print "Sha3 512 bit version OF FILE : ", lab1.sha3Encode(fileToEncode)