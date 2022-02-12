if not __name__ == '__main__':
	print("This file is not meant to be imported.")
	exit()

from scripts.text2font import *

text: str = ""
font: str = "./fonts/py_basic_font.json"

i: int = 1
while i < len(sys.argv):
	if sys.argv[i] == "--font":
		font = sys.argv[i+1]
		i += 1
	else:
		text += sys.argv[i]
	i += 1

print("\n*****************************")
print(f"Information:\n\t - Font: {font}\n\t - Text: \"{text}\"")
print("\n*****************************")
