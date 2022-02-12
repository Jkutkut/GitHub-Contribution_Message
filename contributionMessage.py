if not __name__ == '__main__':
	print("This file is not meant to be imported.")
	exit()

from scripts.text2font import *

text: str = ""
font: str = "./fonts/py_basic_font.json"
format: bool = True

i: int = 1
while i < len(sys.argv):
	if sys.argv[i] == "--font":
		font = sys.argv[i+1]
		i += 1
	elif sys.argv[i] == "--no-format":
		format = False
	elif sys.argv[i] == "--format":
		format = True
	else:
		text += sys.argv[i]
	i += 1

print(f"Information:\n\t - Font: {font}\n\t - Text: \"{text}\"")

t = Text2font.text2font(text, font)
if not t is None:
	if format:
		print (t.replace("0", " "))
	else:
		print(t)