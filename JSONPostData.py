import json

class JSONPostData:
	
	generatedJSON = None

	def __init__(self):
		self.generatedJSON = json.load(open("standardJSON.json"))
		print self.generatedJSON
	
	def setWebNodeCounts(self, na=0, eu=0, ap=0):
		self.generatedJSON["Servers"]["WEB"]["ServerRegions"]["NA"]["NodeCount"] = na
		self.generatedJSON["Servers"]["WEB"]["ServerRegions"]["EU"]["NodeCount"] = eu
		self.generatedJSON["Servers"]["WEB"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def setJavaNodeCounts(self, na=0, eu=0, ap=0):
		self.generatedJSON["Servers"]["JAVA"]["ServerRegions"]["NA"]["NodeCount"] = na
		self.generatedJSON["Servers"]["JAVA"]["ServerRegions"]["EU"]["NodeCount"] = eu
		self.generatedJSON["Servers"]["JAVA"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def setDBNodeCounts(self, na=0, eu=0, ap=0):
		self.generatedJSON["Servers"]["DB"]["ServerRegions"]["NA"]["NodeCount"] = na
		self.generatedJSON["Servers"]["DB"]["ServerRegions"]["EU"]["NodeCount"] = eu
		self.generatedJSON["Servers"]["DB"]["ServerRegions"]["AP"]["NodeCount"] = ap

	def upgradeInfraStructure(self):
		self.generatedJSON['Servers']['UpgradeInfraStructure'] = True

	def setUpgradeToResearch(self, upgrade):
		self.generatedJSON["Servers"]["UpgradeTosResearch"] = upgrade

	def getGeneratedJSONPostData(self):
		return self.generatedJSON
