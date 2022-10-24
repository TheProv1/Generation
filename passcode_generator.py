def passcode_4():
	'''
	This function generates 4 digit passcodes
	'''

	with open("passcode_4.txt","w") as fobj:
		try:
			for i in range(1000,10000):
				fobj.write(str(i) + "\n")
				fobj.flush()
		
		except:
			fobj.close()

def passcode_6():
	'''
	This function generates 6 digit passcodes
	'''
	
	with open("passcode_6.txt","w") as fobj:
		try:
			for i in range(100000,1000000):
				fobj.write(str(i) + '\n')
				fobj.flush()
			
		except:
			fobj.close()

print("\t\t\t\tMain Menu\n")
print("1. 4 Digit Passcodes Generation\n2. 6 Digit Passcodes Generation\n3. Both Passcodes Generation\n4. Exit")
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
