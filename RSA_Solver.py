#!/usr/bin/env python2
import time
from Crypto.Util.number import inverse
import sys
import requests
from bs4 import BeautifulSoup 
import re

'''
Best 'E' Limit Is '100000' --
FactorDB Is A Good Source IDK How To Get (P , Q) From 'N'
SomeTime FactorDB Can Not Got (P , Q) Do Not Use It AS Main Source
This Tool Written In Python2
'''

def PQQP(n):
	N = n
	url = "http://www.factordb.com/"
	params = {'query':N}
	PQQP = []

	TheSession = requests.Session()
	Response = TheSession.get(url , params=params)
	Content = Response.content
	Soup = BeautifulSoup(Content, 'html.parser')
	PQ = Soup.find_all('a')
	PQ = PQ[11:13]


	for line in PQ:
	    line = str(line)
	    line = line.replace('</font></a>' , '')
	    line = line.replace('<a href="index.php?id=', '')
	    line = line.replace('"><font color="#000000">' , '')
	    PQQP.append(line[19:])
	    
	# print str(PQQP) --
	print "P: " + PQQP[0]
	print "Q: " + PQQP[1]
	print "\nGot It For Uh Bruh Just Enter This Data On THE NEXT FIELDS!\n"

	TheSession.close()

def NAHCheck(Here,p,q):
	if not Here:
		n = (p * q)
		return n
	else:
		Ooh = ''
		return Ooh
		pass

def Checkk(n):
	if n == '':
		Ohh = ''
		print "Oooh You Don't Know 'N'?"
		print "It Is SO Easy To Got It Just Give Me (P , Q)"
		Here = False
		return Here
	else:
		Here = True
		return Here
		pass

def Message():
	print "\n\nNow If You Already Have 'N' Do That:"
	print "Now You Should GET (P , Q) Visit https://www.factordb.com/ And Anlyze The N"
	print "Left One Is P -- Right One Is Q"
	print "LOL IN This Update You Could GOT P And Q By Just Enter 'N' --"
	print "You Should Select The MODE -- For Manual FactorDB Using Enter (0)"
	print "for Automating Mode Select (1)"
	print "if You Do not have 'N' Just Pass And Select (0) Mode!!!\n"
	raw_input("\nAre You Ready??")
	MODE = int(raw_input("Mode: "))
	print "\n"
	return MODE

def BruteForce(e,i,p,q,n,c,FlagFormat):
	if e == '':
		print "You Do Not Know The 'E'??"
		Answer = raw_input("Start Brute Force? ")
		limit = int(raw_input("Limit: "))
		if Answer.lower() == "y":
			while i < limit:
				try:
					i += 1
					PHI = ( p - 1 ) * ( q - 1 )
					d = inverse(i,PHI)
					m = pow(c,d,int(n))
					result = hex(m)[2:-1].decode('hex')
					if FlagFormat in result:
						raw_input("Found Possible Result!!!")
						print result
						ASK =  raw_input("Wanna To Continue? ")
						if ASK == "y":
							pass
						else:
							break
					else:
						pass
				except Exception as e:
					pass
			print "Congrats If You Got It Bruh! If Not Plz Increase The Limit..."
			time.sleep(1.9)
			sys.exit()
	else:
		pass

def Program():
	# GET CTF Flag Format!
	FlagFormat = raw_input("FlagFormat: ")

	# Define Main Data
	i = 0
	Here = True

	# 
	c = int(raw_input("\n\nC: "))
	n = raw_input("N: ")

	# Check 'N' IF NOT
	Here = Checkk(n)
	# print Here --

	# Call Message
	# Message() --
	MODE = Message()
	# print MODE --
	# Check Mode
	if MODE == 0:
		pass
	elif MODE == 1:
		PQQP(n)
	else:
		print "That Is Not A Mode I Will Pass Uh To Manual Mode!!"

	# Get Data From User Input
	p = int(raw_input("P: "))
	q = int(raw_input("Q: "))
	e = raw_input("E: ")

	# Set 'N' IF NOT
	CHK = NAHCheck(Here,p,q)
	if CHK != '':
		n = CHK

	# Check 'E' For BRUTE FORCE
	BruteForce(e,i,p,q,n,c,FlagFormat)

	# Analyze Data
	PHI = ( p - 1 ) * ( q - 1 )
	d = inverse(int(e),PHI)
	m = pow(c,d,int(n))

	# Print Data
	print "\n\nHex:\n\t" + hex(m)[2:-1] + "\n\n"
	print "Text:\n\t" + hex(m)[2:-1].decode('hex') + "\n"


if __name__ == '__main__':
	Program()
