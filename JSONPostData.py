import json

class JSONPostData:
	
	generatedJSON = None;

	def __init__(self):
		generatedJSON = json.loads(open('standardJSON.json'))
		print generatedJSON


if __name__ == '__main__':
	objectr = JSONPostData()