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
			file = open(fileName, "r")
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
		file = Text2font.readFile(fileName)
		if file is None or file.closed or not Text2font.isValidJSON(file):
			return None
		else:
			jsonObj = json.load(file)
			file.close()
			return jsonObj

	@staticmethod
	def isValidJSON(file: TextIOWrapper) -> bool:
		'''
		TODO - Check if the file is a valid JSON file.
		'''
		return True

	@staticmethod
	def text2font(text: str, font_path_name: str) -> str:
		"""
		
		"""
		font = Text2font.loadJSON(font_path_name)
		if font is None:
			return None
		return font["details"]["name"]

# If this file is run as a script, execute this as main function.
if __name__ == "__main__":

	print ('Number of arguments:', len(sys.argv), 'arguments.')
	print ('Argument List:', str(sys.argv))

	# Join the arguments together to get the text
	text: str = " ".join([sys.argv[i] for i in range(1, len(sys.argv))])

	fonts = [ # Fonts to tests
		"./fonts/invalid.json",
		"./fonts/py_basic_font.json"
	]

	for i in fonts:
		print("\n*****************************")
		print("Testing font: " + i + " with text: " + text)
		print (Text2font.text2font(text, i))
		print("*****************************")
