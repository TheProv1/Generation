def passcode_4():
	'''
	This function generates 4 digit passcodes
	'''

	with open("passcode_4.txt","w") as fobj:
		try:
			for i in range(0,10000):
				if len(i) == 1:
					passcd_1 = '000' + str(i)
					fobj.write(passcd_1 + '\n')
					fobj.flush()
					
				elif len(i) == 2:
					passcd_2 = '00' + str(i)
					fobj.write(passcd_2 + '\n')
					fobj.flush()
					
				elif len(i) == 3:
					passcd_3 = '0' + str(i)
					fobj.write(passcd_3 + '\n')
					fobj.flush()
				
				elif len(i) == 4:
					passcd_4 = str(i)
					fobj.write(passcd_4 + "\n")
					fobj.flush()
		
		except:
			fobj.close()

def passcode_6():
	'''
	This function generates 6 digit passcodes
	'''
	
	with open("passcode_6.txt","w") as fobj:
		try:
			for i in range(0,1000000):
				if len(i) == 1:
					passcd_1 = '00000' + str(i)
					fobj.write(passcd + '\n')
					fobj.flush()
				
				elif len(i) == 2:
					passcd_2 = '0000' + str(i)
					fobj.write(passcd_2 + '\n')
					fobj.flush()
				
				elif len(i) == 3:
					passcd_3 = '000' + str(i)
					fobj.write(passcd + '\n')
					fobj.flush()
					
				elif len(i) == 4:
					passcd_4 = '00' + str(i)
					fobj.write(passcd_4 + '\n')
					fobj.flush()
				
				elif len(i) == 5:
					passcd_5 = '0' + str(i)
					fobj.write(passcd_5 + '\n')
					fobj.flush()
				
				elif len(i) == 6:
					passcd_6 = str(i)
					fobj.write(passcd_6 + '\n')
					fobj.flush()
			
		except:
			fobj.close()

print("\t\t\t\tMain Menu\n")
print("1. 4 Digit Passcode Generation\n2. 6 Digit Passcode Generation\n3. Both Types of Passcode Generation\n4. Exit")
print()

choice = int(input("Enter your choice: "))
if choice == 1:
	passcode_4()

elif choice == 2:
	passcode_6()
	
elif choice == 3:
	passcode_4()
	passcode_6()
	
else:
	exit()
