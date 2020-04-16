def prGr60(file):
	with open(file) as f:
		while True:
			line = f.readline()
			if len(line) >= 60:
				print(line)
			elif not line:
				break

file = "classworks/23.01.2020/file.txt"
prGr60(file)

	
