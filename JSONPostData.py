import json

class JSONPostData:
	
	generatedJSON = None

	def __init__(self):
		global generatedJSON

		generatedJSON = json.load(open("standardJSON.json"))

	def setWebNodeCounts(self, na=0, eu=0, ap=0):
		global generatedJSON

		generatedJSON["Servers"]["WEB"]["ServerRegions"]["NA"]["NodeCount"] = na
		generatedJSON["Servers"]["WEB"]["ServerRegions"]["EU"]["NodeCount"] = eu
		generatedJSON["Servers"]["WEB"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def setJavaNodeCounts(self, na=0, eu=0, ap=0):
		global generatedJSON

		generatedJSON["Servers"]["JAVA"]["ServerRegions"]["NA"]["NodeCount"] = na
		generatedJSON["Servers"]["JAVA"]["ServerRegions"]["EU"]["NodeCount"] = eu
		generatedJSON["Servers"]["JAVA"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def setDBNodeCounts(self, na=0, eu=0, ap=0):
		global generatedJSON

		generatedJSON["Servers"]["DB"]["ServerRegions"]["NA"]["NodeCount"] = na
		generatedJSON["Servers"]["DB"]["ServerRegions"]["EU"]["NodeCount"] = eu
		generatedJSON["Servers"]["DB"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def setShouldUpgradeInfraStructure(self, shouldUpgradeInfraStructure):
		if(shouldUpgradeInfraStructure)
			generatedJSON["Servers"]["UpgradeInfraStructure"] = "true"
		else
			generatedJSON["Servers"]["UpgradeInfraStructure"] = "false"

	def setUpgradeToResearch(self, upgrade):
		generatedJSON["Servers"]["UpgradeToResearch"] = upgrade

	def getGeneratedJSONPostData(self):
		return json.dumps(generatedJSON)
