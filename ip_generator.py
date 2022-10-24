with open("ip_list.txt","w") as fobj:
	try:
		for i in range(0,256):
			for j in range(0,256):
				for k in range(0,256):
					for l in range(0,256):
						ip = str(i) + '.' + str(j) + '.' + str(k) + '.' + str(l)
						
						fobj.write(ip + "\n")
						fobj.flush
		
	except:
		fobj.close()

query = input("Do you wish to ping the IP Addresses?(Y/n): ")
if query.lower() == 'y':
	
