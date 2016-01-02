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
			#Check Octets
			octet_check_ip=ip_address.split('.')
			#Unicast address check, exclude reserved ip addresses
			if((len(octet_check_ip)==4) and (1<=int(octet_check_ip[0])<=223) and (int(octet_check_ip[0])!=127) and (int(octet_check_ip[0])!=169 or int(octet_check_ip[1])!=254) and (0<=int(octet_check_ip[1])<=255) and (0<=int(octet_check_ip[2])<=255) and (0<=int(octet_check_ip[3])<=255)):
				break
			else:#redirect to top of while loop
				print "\nThe IP address is INVALID! Please retry!\n"
				continue
		#Subnet Mask Validity 
		#list of valid masks
		masks=[255,254,252,248,240,224,192,128,0]
		while True:
			subnet_mask=raw_input("Enter a subnet mask: ")
			#Check Octets
			octet_check_mask=subnet_mask.split('.')
			if((len(octet_check_mask)==4) and (int(octet_check_mask[0])==255) and (int(octet_check_mask[1]) in masks) and (int(octet_check_mask[2]) in masks) and (int(octet_check_mask[3]) in masks) and (int(octet_check_mask[0])>=int(octet_check_mask[1])>=int(octet_check_mask[2])>=int(octet_check_mask[3]))):
				break
			else:#redirect to top of while loop
				print "\nThe Subnet Mask is INVALID! Please retry!\n"
				continue	


	except KeyboardInterrupt:
		print "\nProgram aborted by user. Exiting...\n"
		sys.exit()
subnet_calc()
