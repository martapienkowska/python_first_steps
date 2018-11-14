while True:
	try:
		n = int(input("Input number = "))
		print(1/n)
		break
	except ValueError as e:
		print("error: ", e)
	except KeyboardInterrupt:
		print("\nCtrl+c!")
		break; 


