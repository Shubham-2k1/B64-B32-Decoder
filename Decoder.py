#!/usr/bin/python3

import argparse
import base64
import sys

#%(prog)s -> To print the filename by Argparse

parser = argparse.ArgumentParser(description="Python script to decode Base-64/Base-32",
				usage='%(prog)s --b64/--b32 [cipher]',
				epilog="Example: %(prog)s --b64 aGk=")
				

# nargs = ? -> 1 or none | * -> none or more | + atleast 1
parser.add_argument("--b64",help="decode base64 encoding",
			metavar="base64",
			dest="b64",
			nargs="+")

parser.add_argument("--b32",help="decode base32 encoding",
			metavar="base32",
			dest="b32",
			nargs="+")

parser.add_argument("-v",help="print version",
			action="version",
			version="%(prog)s version 1.0")
			
args = parser.parse_args()

if len(sys.argv)==1:
	parser.print_help(sys.stderr)
	sys.exit(1)
	
#Calculate b64 and b32

b64 = args.b64
b32 = args.b32

if b64:
	for i in b64:
		print((base64.b64decode(i)).decode())

if b32:
	for i in b32:
		print((base64.b32decode(i)).decode())



