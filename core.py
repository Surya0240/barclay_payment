import subprocess

def core(filename):
	subprocess.run(['tesseract',filename, 'x'])

	with open("x.txt") as f:
		for line in f.readlines():
			if line.strip():
				break
	if "International" in line:
		index = line.index("International")
		sentence = line[index:]
		return "It's {}".format(sentence.encode('utf-8'))
	elif "Domestic" in line:
		index = line.index("Domestic")
		sentence = line[index:]
		return"It's {}".format(sentence.encode('utf-8'))
	else:
		return"Some other Payment"
