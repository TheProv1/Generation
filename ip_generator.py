import os
import sys

def IP_Generator():
	'''
	This function generates all the possible IP Addresses in the world
	'''
	with open("ip_list.txt","w") as fobj:
		try:
			for i in range(0,256):
				for j in range(0,256):
					for k in range(0,256):
						for l in range(0,256):
							ip = str(i) + '.' + str(j) + '.' + str(k) + '.' + str(l)
						
							fobj.write(ip + "\n")
							fobj.flush()
		
		except:
			fobj.close()

ans = 'y'
while ans.lower() == "y":
	ip_address = input("Enter the IP Address you wish to ping: (Example: 255.255.255.255 or 8.8.8.8): ")
	if sys.platform.lower() == 'linux':
		cmd = 'ping ' + ip_address + '-c 4'
		os.system(cmd)
	
	elif sys.platform.lower() == 'win32':
		cmd = 'ping ' + ip_address
		os.system(cmd)
