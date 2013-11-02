import json

class JSONPostData:
	
	generatedJSON = None

	def __init__(self):
		global generatedJSON

		generatedJSON = json.load(open("standardJSON.json"))
		print generatedJSON

	def setWebNodeCounts(na=0, eu=0, ap=0):
		global generatedJSON

		generatedJSON["WEB"]["ServerRegions"]["NA"]["NodeCount"] = na
		generatedJSON["WEB"]["ServerRegions"]["EU"]["NodeCount"] = eu
		generatedJSON["WEB"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def setJavaNodeCounts(na=0, eu=0, ap=0):
		global generatedJSON

		generatedJSON["JAVA"]["ServerRegions"]["NA"]["NodeCount"] = na
		generatedJSON["JAVA"]["ServerRegions"]["EU"]["NodeCount"] = eu
		generatedJSON["JAVA"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def setDBNodeCounts(na=0, eu=0, ap=0):
		global generatedJSON

		generatedJSON["DB"]["ServerRegions"]["NA"]["NodeCount"] = na
		generatedJSON["DB"]["ServerRegions"]["EU"]["NodeCount"] = eu
		generatedJSON["DB"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def getGeneratedJSONPostData(self):
		return generatedJSON


if __name__ == '__main__':
	test = JSONPostData()

	print test.getGeneratedJSONPostData()