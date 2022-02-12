import sys # To have control of the system

class Text2font:
	@staticmethod
	def text2font(text: str, font_path_name: str) -> str:
		return "text2font"

# If this file is run as a script, execute this as main function.
if __name__ == "__main__":

	# print ('Number of arguments:', len(sys.argv), 'arguments.')
	# print ('Argument List:', str(sys.argv))

	# Join the arguments together to get the text
	text: str = " ".join([sys.argv[i] for i in range(1, len(sys.argv))])

	print (Text2font.text2font(text, "./fonts/invalid.json"))
	# print (Text2font.text2font(text, "./fonts/py_basic_font.json"))