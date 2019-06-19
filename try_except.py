try:
	f = open("demofile.txt", "r")
	
	print(f.read(2))
	print(f.read(5))
	print(f.readline())
	
	f = open("demofile.txt", "a")
	f.write("Now the file has more content!")
	
except Exception as e:
	print("There is some exception")
	
finally:
	f.close()
