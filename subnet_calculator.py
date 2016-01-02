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
		#Convert Mask to a binary string
		mask_octet_decimal=subnet_mask.split('.')
		mask_octet_binary=[]
		for octet_index in range(0,len(mask_octet_decimal)):
			#get rid of python formatting for binary numbers
			binary_octet=bin(int(mask_octet_decimal[octet_index])).split('b')[1]
			#Check to see if there are 8 bits, add to binary list
			if len(binary_octet)==8:
				mask_octet_binary.append(binary_octet)
			elif len(binary_octet)<8:
				#Pad to get 8 bits
				binary_octet_padded=binary_octet.zfill(8)
				mask_octet_binary.append(binary_octet_padded)
		#Join list
		decimal_mask="".join(binary_octet)
		#Counting host bits and calculating number of hosts/subnet
		no_of_zeros=decimal_mask.count("0")
		no_of_ones=32-no_of_zeros
		no_of_hosts=abs(2**no_of_zeros-2)
		#Obtain wildcard mask
		wildcard_octet=[]
		for w_octect in mask_octet_decimal:
			wild_octet=255-int(w_octect)
			wildcard_octet.append(str(wild_octet))
		wildcard_mask=".".join(wildcard_octet)


	except KeyboardInterrupt:
		print "\nProgram aborted by user. Exiting...\n"
		sys.exit()
subnet_calc()
