def getRateOfChangeForRepliesWithServerTypeSpecifiedAsString(replies, serverType):
	naRateOfChange = euRateOfChange = apRateOfChange = 0

	for num in range(0, len(replies) - 2):
		naRateOfChange += float(replies[num+1].executedNums("serverType")["na"]) - float(replies[num].executedNums("serverType")["na"])
		euRateOfChange += float(replies[num+1].executedNums("serverType")["eu"]) - float(replies[num].executedNums("serverType")["eu"])
		apRateOfChange += float(replies[num+1].executedNums("serverType")["ap"]) - float(replies[num].executedNums("serverType")["ap"])

	naRateOfChange /= len(replies) - 1
	euRateOfChange /= len(replies) - 1
	apRateOfChange /= len(replies) - 1

	return {'na' : naRateOfChange, 'eu' : euRateOfChange, 'ap' : apRateOfChange}