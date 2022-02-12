import sys # To have control of the system
import json # To parse the json file
from io import TextIOWrapper # The object type of files

class Text2font:
	@staticmethod
	def readFile(fileName: str) -> TextIOWrapper:
		"""
		Reads the file and returns the file object.

		If the file does not exist, it returns None.
		"""
		try:
			file = open(fileName)
		except FileNotFoundError:
			print("File not found: " + fileName)
			file = None
		finally:
			return file

	@staticmethod
	def loadJSON(fileName: str) -> dict:
		"""
		Loads a JSON file and returns the content as a dictionary.

		If the file does not exist, it returns None.
		"""
		if not Text2font.isValidJSON(fileName):
			return None

		file = Text2font.readFile(fileName)
		jsonObj = json.load(file)
		file.close()
		return jsonObj

	@staticmethod
	def isValidJSON(fileName: str) -> bool:
		'''
		TODO - Check if the file is a valid JSON-font file.
		'''
		file = Text2font.readFile(fileName)
		if file is None or file.closed or not file.readable():
			return False
		try:
			jsonObj = json.load(file)
		except json.decoder.JSONDecodeError as e:
			print(f"Invalid JSON file: {e}")
			file.close()
			return False
		for key in ("details", "font"):
			if not key in jsonObj:
				print(f"Invalid JSON file: Missing key: {key}")
				file.close()
				return False
		# Check details
		for key in ("name", "height", "width"):
			if not key in jsonObj["details"]:
				print(f"Invalid JSON file: Missing key: {key}")
				file.close()
				return False
		# Check font
		for key in ["default"]:
			if not key in jsonObj["font"]:
				print(f"Invalid JSON file: Missing key: {key}")
				file.close()
				return False
		return True

	@staticmethod
	def text2font(text: str, font_path_name: str) -> str:
		"""
		Attempts to convert the given text to the representation using the font_file.

		If the font_file is not valid, it returns None.
		"""
		font = Text2font.loadJSON(font_path_name)
		if font is None:
			return None
		print(f"{font['details']['name']} loaded.")
		str = ["" for i in range(font['details']['height'])]
		for char in text:
			f = font['font'][char] if font['font'].get(char) else font['font']['default']
			for i in range(font['details']['height']):
				str[i] += f[i]
		return "\n".join(str)

# If this file is run as a script, execute this as main function.
if __name__ == "__main__":

	print ('Number of arguments:', len(sys.argv), 'arguments.')
	print ('Argument List:', str(sys.argv))

	# Join the arguments together to get the text
	text: str = " ".join([sys.argv[i] for i in range(1, len(sys.argv))])

	fonts = [ # Fonts to tests
		"./fonts/invalid.json",
		"./fonts/invalid_font.json",
		"./fonts/py_basic_font.json"
	]

	for i in fonts:
		print("\n*****************************")
		print(f"Testing font:\n\t - Font \"{i}\"\n\t - Text: \"{text}\"")
		t = Text2font.text2font(text, i)
		if not t is None:
			print (t.replace("0", " "))
		print("*****************************")
