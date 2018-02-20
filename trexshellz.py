#!/usr/bin/env python

# Author: Joshua Arnold (@huskersec)
# License: MIT License
# Tool to meet objectives of SLAE exam

import sys
import argparse

#insert super amazing trex ascii art here

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Description: Pass args for shellcode generation', 
    usage='./trexshellz.py <payload> [<args>]' + "\n"
        'Current payloads are:' + "\n"
        '    bind_shell' + "\n"
        '    reverse_shell' + "\n"
        '    execve_stack' + "\n"
        '    custom' + "\n",
    epilog=
        '-Bind shell: ./trexshellz.py bind_shell --LPORT 4545' + "\n"
        '-Reverse shell: ./trexshellz.py reverse_shell --LHOST 192.168.1.1 --LPORT 4545' + "\n"
        '-Execve-stack: ./trexshellz.py execve_stack' + "\n"
        '-Custom: ./trexshellz.py custom --SHELLCODE <shellcode>' + "\n"
        '-EggHunter: ./trexshellz.py bind_shell --LPORT 4545 --EGG' + "\n"
        '-Encode: ./trexshellz.py bind_shell --LPORT 4545 --ENCODE' + "\n"
        '-Analyze: ./trexshellz.py custom --SHELLCODE <shellcode> --ANALYZE' + "\n"
        '-Polymorph: ./trexshellz.py bind_shell --LPORT 4545 --POLYMORPH' + "\n"
        '-Crypter: ./trexshellz.py bind_shell --LPORT --CRYPT' + "\n")  

### payload parsers ###
subparsers = parser.add_subparsers(dest='payload')

parser_bindshell = subparsers.add_parser('bind_shell')
parser_bindshell.add_argument("--LPORT", required=True, metavar='<port>', type=int, 
    help="specify port for bind shell - must be > 256 to avoid null bytes")

parser_reverseshell = subparsers.add_parser('reverse_shell')
parser_reverseshell.add_argument("--LHOST", required=True, metavar='<host>', 
    help="specify ip for reverse shell - no octet should contain a 0")
parser_reverseshell.add_argument("--LPORT", required=True, metavar='<port>', type=int, 
    help="specify port for reverse shell - must be > 256 to avoid null bytes")

parser_execvestack = subparsers.add_parser('execve_stack')

parser_custom = subparsers.add_parser('custom')
parser_custom.add_argument("--SHELLCODE", required=True, metavar='<shellcode>', 
    help="specify shellcode")

### option parsers ###
parser.add_argument("--EGG", action='store_true', 
    help="specify egg hunter technique, string is \"eggy\"")
parser.add_argument("--ENCODE", action='store_true', 
    help="specify the built-in encoding technique")
parser.add_argument("--ANALYZE", action='store_true', help="analyze a given shellcode")
parser.add_argument("--POLYMORPH", action='store_true', 
    help="specify polymorphism to use on given shellcode")
parser.add_argument("--CRYPT", action='store_true', help="specify the built-in crypter")

args = parser.parse_args()

#print args    # prints namespace and all values of args

if args.EGG is not False:
    print "EGG has been set (value is %s)" % args.EGG


if args.payload == 'bind_shell':
    #print '%s payload selected w/ %i as port' % (args.payload,args.LPORT)
    args_port = args.LPORT
    if args.LPORT <= 256:
        print "Please specify port greater than 256!"
    else:
        sys.path.insert(0,"Modules/BindShell/")
        import bind_shell

elif args.payload == 'reverse_shell':
    #print '%s payload selected w/ %s as host and %i as port' % (args.payload,args.LHOST,args.LPORT)
    args_host = args.LHOST
    args_port = args.LPORT
    if args.LPORT <= 256:
        print "Please specify port greater than 256!"
    #elif args.LHOST need to implement a check for IPs containing .0. 
    else:
        sys.path.insert(0,"Modules/ReverseShell/")
        import reverse_shell
     
elif args.payload == 'execve_stack':
    import execve_stack

elif args.payload == 'custom':
    args_shellcode = args.SHELLCODE
    print args_shellcode

else:
    print "Please select a payload!"
