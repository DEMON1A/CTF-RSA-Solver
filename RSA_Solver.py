#!/usr/bin/env python

import time
from Crypto.Util.number import inverse

'''
Best 'E' Limit Is '100000' --
FactorDB Is A Good Source IDK How To Get (P , Q) From 'N'
SomeTime FactorDB Can Not Got (P , Q) Do Not Use It AS Main Source
This Tool Written In Python2
'''

def Program():
	FlagFormat = raw_input("FlagFormat: ")
	i = 0
	c = int(raw_input("\n\nC: "))
	n = raw_input("N: ")
	Here = True
	if n == '':
		print "Oooh You Don't Know 'N'?"
		print "It Is SO Easy To Got It Just Give Me (P , Q)"
		Here = False

	print "\n\nNow If You Already Have 'N' Do That:"
	print "Now You Should GET (P , Q) Visit http://factordb.com/ And Anlyze The N"
	print "Left One Is P -- Right One Is Q"
	print "if You Do not have 'N' Just Pass!!!\n"
	raw_input("\nAre You Ready??\n")

	p = int(raw_input("P: "))
	q = int(raw_input("Q: "))

	if not Here:
		n = (p * q)
	else:
		pass
	e = raw_input("E: ")
	if e == '':
		print "You Do Not Know The 'E'??"
		Answer = raw_input("Start Brute Force? ")
		limit = int(raw_input("Limit: "))
		if Answer == "y":
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
							return 0
					else:
						pass
				except Exception as e:
					pass
			print "Congrats If You Got It Bruh! If Not Plz Increase The Limit..."
			time.sleep(1.9)
			return 0

	else:
		pass

	PHI = ( p - 1 ) * ( q - 1 )
	d = inverse(int(e),PHI)
	m = pow(c,d,int(n))

	print "\n\nHex:\n\t" + hex(m)[2:-1] + "\n\n"
	print "Text:\n\t" + hex(m)[2:-1].decode('hex') + "\n"


if __name__ == '__main__':
	Program()
