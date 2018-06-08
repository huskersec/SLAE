#!/usr/bin/env python

# Author: Joshua Arnold (@huskersec)
# License: MIT License
# Analysis module

from trexshellz import args_shellcode
import subprocess

print "\n"
print "Input shellcode: " + args_shellcode

#Setting up a pipeline to process input shellcode with ndisasm
echo1 = subprocess.Popen(('echo', '-ne', args_shellcode), stdout=subprocess.PIPE)
ndis = subprocess.Popen(('ndisasm', '-u', '-'), stdin=echo1.stdout)
echo1.wait()

#Setup to pass shellcode to sctest
echo2 = subprocess.Popen(('echo','-ne', args_shellcode), stdout=subprocess.PIPE)
sctst = subprocess.Popen(('sctest', '-vvv', '-Ss', '100000', '-G', 'sc.dot'), stdin=echo2.stdout, stdout=subprocess.PIPE)
echo2.wait()
dot = subprocess.Popen(('dot', 'sc.dot', '-Tpng', '-o', 'sc.png'), stdin=sctst.stdout)
sctst.wait()

print "\n"
print "Displaying disassembly with visual calls: "
png = subprocess.Popen(('eog', 'sc.png', '&'))
