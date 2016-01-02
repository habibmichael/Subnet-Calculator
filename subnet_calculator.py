#subnet calculator
#import appropriate modules
import random
import sys

def subnet_calc():
	#try except block to handle key interrupt ^C
	try:
		print "\n"

		#Checking the IP Address validity
		while True:
			ip_address= raw_input("Enter an IP address: ")
			#Check Octects
			octet_check=ip_address.split('.')
			#Unicast address check, exclude reserved ip addresses
			if((len(octet_check)==4) and (1<=int(octet_check[0])<=223) and (int(octet_check[0])!=127) and (int(octet_check[0])!=169 or int(octet_check[1])!=254) and (0<=int(octet_check[1])<=255) and (0<=int(octet_check[2])<=255) and (0<=int(octet_check[3])<=255)):
				break
			else:#redirect to top of while loop
				print "\nThe IP address is INVALID! Please retry!\n"
				continue